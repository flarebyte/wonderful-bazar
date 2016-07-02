/*
 * Licensed under GNU Lesser General Public License Version 2.1, February 1999
 * You may not use this file except in compliance with this license.
 * You may obtain a copy of this license at:
 *           http://www.opensource.org/licenses/
 * Unless required by applicable law or agreed to in writing, software
 * distributed under this license is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See this license for the specific language governing permissions and
 * limitations under this license.
 */
package org.snowmongoose.generator.builder;

import java.util.ArrayList;
import java.util.Map;

import org.snowmongoose.generator.StringCooker;

/**
 * This method builds a string using a sequence and some variables.<p>
 * Each token of the sequence is read and the corresponding variable is added (and not replaced) in the resulting string.<p>
 * In other words, even if a variable contains another variable, only the variable in the original sequence (the script) will be replaced.<p>
 * The script to provide is just a sequence of tokens without any notion of context.<p>
 * Each token can be either a word (containing 1 or more letters or digits) or one punctuation character <p>.
 * All the spaces are ignored.<p>
 * Example 1: in this example, a and b are swapped
 * <code>
 * HashMap mapSwapValue = new HashMap();
		mapSwapValue.put("a","b");
		mapSwapValue.put("b","a");
	
	BasicStringBuilder basicStringBuilder = new BasicStringBuilder("a.b.a.b.a.a");
	basicStringBuilder.build(mapSwapValue) -> "b.a.b.a.b.b"
	//or shortly
	StringCooker.basicBuild("a.b.a.b.a.a",mapSwapValue) -> "b.a.b.a.b.b"
		
 * </code> 
 * Example 2: a very readable way to express a regular expression.
 * <code>
 * 		HashMap mapRegularExpValue = new HashMap();
		mapRegularExpValue.put("dd","([0-3][0-9])");//naive solution: accepts 00 to 39
		mapRegularExpValue.put("mm","[0-1][0-9]");//naive solution: accepts 00 to 19
		mapRegularExpValue.put("19yy","[1][9][0-9][0-9]");
		mapRegularExpValue.put("/","[\\-/.]");
		StringCooker.basicBuild("dd/mm/19yy",mapRegularExpValue) -> "([0-3][0-9])[\\-/.][0-1][0-9][\\-/.][1][9][0-9][0-9]"
 * </code>  
 * @author <a href="olivierhuin@users.sourceforge.net">Olivier Huin </a>
 */
public class BasicStringBuilder implements IStringBuilder {

	private String script;

	private transient String[] templateTokens = null;

	/**
	 * Constructor
	 * @param script the script to construct
	 */
	public BasicStringBuilder(String script) {
		super();
		this.script = script;
	}

	/**
	 * Builds the string after having parsed and loaded the script.
	 */
	public String build(Map replwithMap) {
		if (this.script == null)
			return null;
		if (replwithMap == null)
			return this.script;
		String[] keys = (String[]) replwithMap.keySet().toArray(new String[1]);
		if (templateTokens == null)
			templateTokens = parseScript(script);//lazy cache
		String[] r = new String[templateTokens.length];
		//Populates with the map
		for (int i = 0; i < templateTokens.length; i++) {
			String s = (String) replwithMap.get(templateTokens[i]);
			r[i] = (s == null ? templateTokens[i] : s);
		}

		return StringCooker.join(r, "");
	}

	/**
	 * Parse (tokenize) a script rules: <p>
	 * <ul>
	 * <li>spaces are ignored </li>
	 * <li>a token can be an alphanumeric value, a punctuation</li>
	 * <li>you must separate 2 java identifiers by a punctuation or a space.Thus alpha16 is seen as 1 token while alpha 16
	 * is seen as 2 consecutive punctuations and will be considered as 2 tokens.</li>
	 * </ul>
	 * 
	 * @param script
	 *            the script to tokenize
	 * @return a list of tokens
	 */
	private final String[] parseScript(String script) {
		ArrayList r = new ArrayList();
		StringBuffer sbuff = new StringBuffer();
		for (int i = 0; i < script.length(); i++) {
			char c = script.charAt(i);
			//If letter or digit, add it in the buffer,
			//else adds the token(s)
			if (Character.isLetterOrDigit(c)) {
				sbuff.append(c);
			} else {
				//adds the alphanumeric identifier if one
				if (sbuff.length() > 0)
					r.add(sbuff.toString());
				sbuff = new StringBuffer();
				//adds the punctuation if it is not space
				if (!Character.isWhitespace(c))
					r.add(new String("" + c));
			}
		}//end for
		if (sbuff.length() > 0) {
			r.add(sbuff.toString());
		}
		return (String[]) r.toArray(new String[0]);
	}
}
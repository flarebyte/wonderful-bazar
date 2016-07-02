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
package org.snowmongoose.generator;

import org.snowmongoose.generator.transformer.PrefixAndSuffixTransformer;
import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.generator.transformer.LowerCaseTransformer;
import org.snowmongoose.generator.transformer.RegexTransformer;
import org.snowmongoose.generator.transformer.CompositeTransformer;
import org.snowmongoose.generator.transformer.UpperCaseTransformer;

/**
 * @author Oliver Huin
 *
 */
public class StringTransformerFactory {
	private final static IStringTransformer upperCaseTransformer = new UpperCaseTransformer();
	private final static IStringTransformer lowerCaseTransformer = new LowerCaseTransformer();
	private final static IStringTransformer SQLQuoteTransformer = new CompositeTransformer(new RegexTransformer("'","''"),new PrefixAndSuffixTransformer("'","'"));
	private final static IStringTransformer SQLDoubleQuoteTransformer = new CompositeTransformer(new RegexTransformer("\"","\"\""),new PrefixAndSuffixTransformer("\"","\""));
	private final static IStringTransformer javaDoubleQuoteTransformer = new CompositeTransformer(new RegexTransformer("\"","\\\""),new PrefixAndSuffixTransformer("\"","\""));
	
	public final static IStringTransformer upperCaseTransformer(){
		return upperCaseTransformer;
	}
	public final static IStringTransformer lowerCaseTransformer(){
		return lowerCaseTransformer;
	}
	public final static IStringTransformer SQLQuoteTransformer(){
		return SQLQuoteTransformer;
	}
	public final static IStringTransformer SQLDoubleQuoteTransformer(){
		return SQLDoubleQuoteTransformer;
	}
	public final static IStringTransformer javaDoubleQuoteTransformer(){
		return javaDoubleQuoteTransformer;
	}

}

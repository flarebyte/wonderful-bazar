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
package test.org.snowmongoose.generator;

import java.sql.Date;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Locale;

import junit.framework.TestCase;

import org.snowmongoose.generator.StringCooker;
import org.snowmongoose.generator.StringTransformerFactory;
import org.snowmongoose.generator.transformer.AlignTransformer;
import org.snowmongoose.generator.transformer.CenterAlignTransformer;
import org.snowmongoose.generator.transformer.CompositeTransformer;
import org.snowmongoose.generator.transformer.DecimalFormatTransformer;
import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.generator.transformer.RightAlignTransformer;
import org.snowmongoose.generator.transformer.SimpleDateFormatTransformer;
import org.snowmongoose.generator.transformer.XmlTagTransformer;

/**
 * @author Oliver Huin
 *  
 */
public class StringCookerTest extends TestCase {
	public void testReplace() {

		assertEquals("AcAdabra", StringCooker.replaceObject("acadabra", "a",
				"A", 2));
		assertEquals("4c4dabra", StringCooker.replaceObject("acadabra", "a",
				new Integer(4), 2));
		assertEquals("keyboard=querty", StringCooker.replaceAllObject(
				"keyboard=azerty", "azerty", "querty"));
		assertEquals("kEyboard=azErty", StringCooker.replaceAllObject(
				"keyboard=azerty", "e", "E"));
		assertEquals("kEyboard=azerty", StringCooker.replaceFirstObject(
				"keyboard=azerty", "e", "E"));
		//null or empty string trap
		assertEquals("acadabra", StringCooker.replaceObject("acadabra", null,
				"A", 2));
		assertEquals("acadabra", StringCooker.replaceObject("acadabra", "",
				"A", 2));
		assertEquals("acadabra", StringCooker.replaceObject("acadabra", "a",
				null, 2));
		assertEquals("cdabra", StringCooker.replaceObject("acadabra", "a", "",
				2));
		assertEquals("acadabra", StringCooker.replaceObject("acadabra", "a",
				"A", 0));
		assertNull(StringCooker.replaceObject(null, "a", "A", 0));
	}

	public void testReplaceArray() {
		Object[] array0Value = {};
		Object[] array1Value = { "100" };
		Object[] array2Values = { "100", new Integer(200) };

		assertEquals("a100b100c200d200e", StringCooker.replaceArray(
				"a?b?c?d?e", "?", -1, array2Values, 2));
		assertEquals("a100b100c200d200e?f?g", StringCooker.replaceArray(
				"a?b?c?d?e?f?g", "?", -1, array2Values, 2));
		assertEquals("a100b200c?d?e", StringCooker.replaceFirstArray(
				"a?b?c?d?e", "?", -1, array2Values));
		assertEquals("a100b200c200d100e", StringCooker.replaceArray(
				"a$1b$2c$2d$1e", "$", 1, array2Values, 2));
		assertEquals("a100b200c200d100e$2.$1", StringCooker.replaceArray(
				"a$1b$2c$2d$1e$2.$1", "$", 1, array2Values, 2));
		assertEquals("a100b200c200d100e200.100", StringCooker.replaceAllArray(
				"a$1b$2c$2d$1e$2.$1", "$", 1, array2Values));
		assertEquals("a100b200c$2d$1e$2.$1", StringCooker.replaceFirstArray(
				"a$1b$2c$2d$1e$2.$1", "$", 1, array2Values));

		//null or empty string trap
		assertNull(StringCooker.replaceFirstArray(null, "$", 1, array2Values));
		assertEquals("", StringCooker.replaceAllArray("", "$", 1, array2Values));
		assertEquals("a?b?c?d?e", StringCooker.replaceArray("a?b?c?d?e", "?",
				-1, null, 2));
		assertEquals("a?b?c?d?e", StringCooker.replaceArray("a?b?c?d?e", "?",
				-1, new String[] {}, 2));
		assertEquals("abc?d?e", StringCooker.replaceArray("a?b?c?d?e", "?", -1,
				new String[] { "" }, 2));
		assertEquals("a?b?c?d?e", StringCooker.replaceArray("a?b?c?d?e", "?",
				-1, array2Values, 0));

	}

	public void testReplaceCollection() {
		ArrayList list0Value = new ArrayList();
		ArrayList list1Value = new ArrayList();
		list1Value.add(new Integer(100));
		ArrayList list2Values = new ArrayList();
		list2Values.add(new Integer(100));
		list2Values.add("200");

		assertEquals("a100b100c200d200e", StringCooker.replaceCollection(
				"a?b?c?d?e", "?", -1, list2Values, 2));
		assertEquals("a100b100c200d200e?f?g", StringCooker.replaceCollection(
				"a?b?c?d?e?f?g", "?", -1, list2Values, 2));
		assertEquals("a100b200c?d?e", StringCooker.replaceFirstCollection(
				"a?b?c?d?e", "?", -1, list2Values));
		assertEquals("a100b200c200d100e", StringCooker.replaceCollection(
				"a$1b$2c$2d$1e", "$", 1, list2Values, 2));
		assertEquals("a100b200c200d100e$2.$1", StringCooker.replaceCollection(
				"a$1b$2c$2d$1e$2.$1", "$", 1, list2Values, 2));
		assertEquals("a100b200c200d100e200.100",
				StringCooker.replaceAllCollection("a$1b$2c$2d$1e$2.$1", "$", 1,
						list2Values));
		assertEquals("a100b200c$2d$1e$2.$1", StringCooker
				.replaceFirstCollection("a$1b$2c$2d$1e$2.$1", "$", 1,
						list2Values));

		//null or empty string trap
		assertNull(StringCooker.replaceFirstCollection(null, "$", 1,
				list2Values));
		assertEquals("", StringCooker.replaceAllCollection("", "$", 1,
				list2Values));
		assertEquals("a?b?c?d?e", StringCooker.replaceCollection("a?b?c?d?e",
				"?", -1, null, 2));
		assertEquals("a?b?c?d?e", StringCooker.replaceCollection("a?b?c?d?e",
				"?", -1, list0Value, 2));
		assertEquals("a?b?c?d?e", StringCooker.replaceCollection("a?b?c?d?e",
				"?", -1, list2Values, 0));

	}

	public void testReplaceMap() {
		HashMap map0Value = new HashMap();
		HashMap map1Value = new HashMap();
		map1Value.put("a", "A");
		HashMap map2Values = new HashMap();
		map2Values.put("a", "A");
		map2Values.put("r", "R");

		assertEquals("AcAdabra", StringCooker.replaceMap("acadabra", map1Value,
				2));
		assertEquals("AcAdabRa", StringCooker.replaceMap("acadabra",
				map2Values, 2));
		assertEquals("keyboArd=Azerty", StringCooker.replaceAllMap(
				"keyboard=azerty", map1Value));
		assertEquals("keyboArd=azerty", StringCooker.replaceFirstMap(
				"keyboard=azerty", map1Value));
		//null or empty string trap
		assertEquals("acadabra", StringCooker.replaceMap("acadabra", null, 2));
		assertEquals("acadabra", StringCooker.replaceMap("acadabra", map0Value,
				2));
		assertEquals("acadabra", StringCooker.replaceMap("acadabra", map1Value,
				0));
		assertNull(StringCooker.replaceMap(null, map1Value, 0));
	}

	public void testBasicBuild() {
		HashMap map0Value = new HashMap();
		HashMap map1Value = new HashMap();
		map1Value.put("a", "[alpha]");
		HashMap mapxValues = new HashMap();
		mapxValues.put("a", "[alpha]");
		mapxValues.put("b16", "[beta16]");
		mapxValues.put("4", "[4]");
		mapxValues.put(".", ";");
		HashMap mapSwapValue = new HashMap();
		mapSwapValue.put("a", "b");
		mapSwapValue.put("b", "a");
		//Regular expression
		HashMap mapRegularExpValue = new HashMap();
		mapRegularExpValue.put("dd", "([0-3][0-9])");//naive solution: accepts
		// 00 to 39
		mapRegularExpValue.put("mm", "[0-1][0-9]");//naive solution: accepts 00
		// to 19
		mapRegularExpValue.put("19yy", "[1][9][0-9][0-9]");
		mapRegularExpValue.put("/", "[\\-/.]");

		assertEquals("[alpha].[alpha].b16.4.4.[alpha].b16.4.b16", StringCooker
				.basicBuild("a.a.b16.4.4.a.b16.4.b16", map1Value));
		assertEquals(
				";;[alpha][alpha][beta16][4][4][alpha][beta16][4][beta16]",
				StringCooker.basicBuild("..a a b16 4  4 a  b16 4 b16",
						mapxValues));
		assertEquals(
				"[alpha];[alpha];[beta16];[4];[4];[alpha];[beta16];[4];[beta16]",
				StringCooker.basicBuild("a.a.b16.4.4.a.b16.4.b16", mapxValues));
		assertEquals("[beta16];[alpha];charly", StringCooker.basicBuild(
				"b16.a.charly", mapxValues));
		assertEquals("([0-3][0-9])[\\-/.][0-1][0-9][\\-/.][1][9][0-9][0-9]",
				StringCooker.basicBuild("dd/mm/19yy", mapRegularExpValue));
		//null or empty string trap
		assertEquals("a.a.b16.4.4.a.b16.4.b16", StringCooker.basicBuild(
				"a.a.b16.4.4.a.b16.4.b16", map0Value));
		assertEquals("a.a.b16.4.4.a.b16.4.b16", StringCooker.basicBuild(
				"a.a.b16.4.4.a.b16.4.b16", null));
		assertEquals("b.a.b.a.b.b", StringCooker.basicBuild("a.b.a.b.a.a",
				mapSwapValue));
		assertNull(StringCooker.basicBuild(null, mapxValues));
		assertEquals("", StringCooker.basicBuild("", mapxValues));

		//[Date,Desc,Cost/a1,b1,c1/a2,b2,c2]

	}

	public void testTransformArray() {
		String[] input = new String[] { "London", null, "Tokyo" };
		String[] output = StringCooker.transformArray(StringTransformerFactory
				.upperCaseTransformer(), input);
		assertNotNull(output);
		assertEquals(3, output.length);
		assertEquals("LONDON", output[0]);
		assertNull(output[1]);
		assertEquals("TOKYO", output[2]);

	}

	public void testTransformTable() {
		String[] row0 = new String[] { "Date", "Desc", "Cost" };
		String[] row1 = new String[] { "01/01/2001", "desc1", "14 €" };
		String[] row2 = new String[] { "02/01/2001", "desc2", "26 €" };
		IStringTransformer th = new XmlTagTransformer("th");
		IStringTransformer tr = new XmlTagTransformer("tr");
		IStringTransformer td = new XmlTagTransformer("td");
		IStringTransformer tbody = new XmlTagTransformer("tbody");
		assertEquals(
				"<tbody><tr><th>Date</th><th>Desc</th><th>Cost</th></tr><tr><td>01/01/2001</td><td>desc1</td><td>14 €</td></tr><tr><td>02/01/2001</td><td>desc2</td><td>26 €</td></tr></tbody>",
				tbody.toString(StringCooker.join(new Object[] {
						StringCooker.join(row0, "", th),
						StringCooker.join(row1, "", td),
						StringCooker.join(row2, "", td) }, "", tr)));

	}

	public void testTransformTypedTable() {
		String[] row0 = new String[] { "Date", "Desc", "Cost" };
		Object[] row1 = new Object[] { new Date(System.currentTimeMillis()),
				"desc1", new Float(14.12) };
		Object[] row2 = new Object[] {
				new Date(System.currentTimeMillis() - 3600000), "description",
				new Integer(10) };
		IStringTransformer fmt_date = new CenterAlignTransformer(15, ' ');
		IStringTransformer fmt_desc = new AlignTransformer(20, ' ',AlignTransformer.CENTER_ALIGN);
		IStringTransformer fmt_cost = new RightAlignTransformer(10, ' ');
		IStringTransformer[] fmt_title = new IStringTransformer[] { fmt_date,
				fmt_desc, fmt_cost };
		IStringTransformer[] fmt_row = new IStringTransformer[] {
				new CompositeTransformer(new SimpleDateFormatTransformer(
						"dd MMMM", Locale.UK), fmt_date), fmt_desc, new CompositeTransformer(new DecimalFormatTransformer("000.00 £"),fmt_cost) };

		String r = StringCooker.join(new Object[] {
				StringCooker.join(row0, "|", fmt_title),
				StringCooker.join(row1, "|", fmt_row),
				StringCooker.join(row2, "|", fmt_row) }, "\n");
		System.out.println(r);

	}

}
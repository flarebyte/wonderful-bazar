/*
 * Created on Apr 25, 2005
 *
 */
package test.org.snowmongoose.generator;

import junit.framework.TestCase;

import org.snowmongoose.generator.StringTransformerFactory;
import org.snowmongoose.generator.transformer.PrefixAndSuffixTransformer;
import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.generator.transformer.RegexTransformer;
import org.snowmongoose.generator.transformer.CompositeTransformer;

/**
 * @author Oliver Huin
 *
 */
public class TransformerTest extends TestCase {
	public void test(){
		IStringTransformer re = new RegexTransformer("i","iiiii");
		assertEquals("Capiiiiitaliiiiize",re.toString("Capitalize"));
		assertEquals("capitalize",StringTransformerFactory.lowerCaseTransformer().toString("Capitalize"));
		IStringTransformer list = new CompositeTransformer(re,StringTransformerFactory.lowerCaseTransformer());
		assertEquals("capiiiiitaliiiiize",list.toString("Capitalize"));
		IStringTransformer prefixAndSuffix = new PrefixAndSuffixTransformer("<html>","</html>");
		assertEquals("<html>Capitalize</html>",prefixAndSuffix.toString("Capitalize"));
		
		assertEquals("'char c=''A'';'",StringTransformerFactory.SQLQuoteTransformer().toString("char c='A';"));
		
		
		
		
		
		
	}
}

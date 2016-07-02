/*
 * Created on Apr 12, 2005
 *
 */
package test.org.snowmongoose.generator;

import java.util.HashMap;

import org.snowmongoose.generator.builder.interpreter.basic.BasicInterpreterStringBuilder;
import org.snowmongoose.generator.transformer.IStringTransformer;

import junit.framework.TestCase;

/**
 * @author Oliver Huin
 *
 */
public class BasicInterpreterStringBuilderTest extends TestCase {
	public void test(){
		BasicInterpreterStringBuilder builder = new BasicInterpreterStringBuilder("a(b+(c+d))+e",null);
		HashMap map = new HashMap();
		builder.build(map);
	}
}

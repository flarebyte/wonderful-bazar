/*
 * Created on Jul 12, 2005
 *
 */
package test.org.snowmongoose.pov3d;

import junit.framework.TestCase;

import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.pov3d.PovMap;
import org.snowmongoose.pov3d.PovTransformerFactory;
import org.snowmongoose.pov3d.Vector3D;

/**
 * @author Oliver Huin
 *
 */
public class PovArgumentsTransformerTest extends TestCase {
	public void test() {
		IStringTransformer  t = PovTransformerFactory.argumentsTransformer("no_shadow");
		System.out.print(t.toString(null));
	}
	public void test2() {
		IStringTransformer  t = PovTransformerFactory.argumentsTransformer("scale", new Vector3D(12,-0.5,12));
		System.out.print(t.toString(null));
	}
	public void test3() {
		IStringTransformer  t = PovTransformerFactory.argumentsTransformer("scale", new Double(1.5));
		System.out.print(t.toString(null));
	}
	public void test4() {
		PovMap map = new PovMap();
		map.put(0,"color",new Object[]{" rgbt", new Integer(1)});
		map.put(0.4,"color",new Object[]{" rgbt", new Double(0.8)});
		map.put(1,"color",new Object[]{" rgbt", new Integer(1)});
		
		IStringTransformer  t = PovTransformerFactory.mapTransformer("color_map", map);
		System.out.print(t.toString(null));
	}
}

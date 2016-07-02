/*
 * Created on Jul 12, 2005
 *
 */
package org.snowmongoose.pov3d;

import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.pov3d.transformer.PovArgumentsTransformer;
import org.snowmongoose.pov3d.transformer.PovMapTransformer;
import org.snowmongoose.pov3d.transformer.PovObjectTransformer;

/**
 * @author Oliver Huin
 *
 */
public class PovTransformerFactory {
	public final static IStringTransformer argumentsTransformer(String name,Object[] arguments) {
		return new PovArgumentsTransformer(name, arguments);
	}
	public final static IStringTransformer argumentsTransformer(String name) {
		return new PovArgumentsTransformer(name, null);
	}
	public final static IStringTransformer argumentsTransformer(String name, Object arg1) {
		return new PovArgumentsTransformer(name, new Object[]{arg1});
	}
	public final static IStringTransformer argumentsTransformer(String name, Object arg1, Object arg2) {
		return new PovArgumentsTransformer(name, new Object[]{arg1,arg2});
	}
	public final static IStringTransformer argumentsTransformer(String name, Object arg1, Object arg2, Object arg3) {
		return new PovArgumentsTransformer(name, new Object[]{arg1,arg2,arg3});
	}
	public final static IStringTransformer argumentsTransformer(String name, Object arg1, Object arg2, Object arg3,Object arg4) {
		return new PovArgumentsTransformer(name, new Object[]{arg1,arg2,arg3,arg4});
	}
	public IStringTransformer argumentsTransformer(String name, Object arg1, Object arg2, Object arg3,Object arg4, Object arg5) {
		return new PovArgumentsTransformer(name, new Object[]{arg1,arg2,arg3,arg4,arg5});
	}
	
	public final static IStringTransformer objectTransformer(String name,Object[] nodes) {
		return new PovObjectTransformer(name, nodes);
	}
	public final static IStringTransformer objectTransformer(String name) {
		return new PovObjectTransformer(name, null);
	}
	public final static IStringTransformer objectTransformer(String name, Object node1) {
		return new PovObjectTransformer(name, new Object[]{node1});
	}
	public final static IStringTransformer objectTransformer(String name, Object node1,Object node2) {
		return new PovObjectTransformer(name, new Object[]{node1,node2});
	}
	
	public final static IStringTransformer objectTransformer(String name, Object node1,Object node2, Object node3) {
		return new PovObjectTransformer(name, new Object[]{node1,node2,node3});
	}
	public final static IStringTransformer objectTransformer(String name, Object node1,Object node2, Object node3, Object node4) {
		return new PovObjectTransformer(name, new Object[]{node1,node2,node3,node4});
	}

	public final static IStringTransformer mapTransformer(String name, PovMap map) {
		return new PovMapTransformer(name, map);
	}


	
}

/*
 * Created on Jul 12, 2005
 *
 */
package org.snowmongoose.pov3d.transformer;

import org.snowmongoose.generator.transformer.IStringTransformer;

/**
 * @author Oliver Huin
 *  
 */
public class PovObjectTransformer implements IStringTransformer {

	private Object[] nodes;
	private String name;
	public final static String INDENT="    ";
	

	/**
	 * @return Returns the name.
	 */
	protected String getName() {
		return name;
	}

	protected IStringTransformer getNode(int index) {
		return (IStringTransformer) nodes[index];
	}

	protected int nodesCount() {
		return nodes.length;
	}

	/**
	 * @param name
	 */
	public PovObjectTransformer(String name, Object[] nodes) {
		super();
		this.name = name;
		this.nodes = nodes==null?new Object[]{}: nodes;
		
		
	}
	/*
	 * (non-Javadoc)
	 * 
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		StringBuffer r = new StringBuffer();
		r.append(this.getName());
		r.append("{\n");
		for (int i = 0; i < this.nodesCount(); i++) {
			r.append(INDENT).append(getNode(i).toString(object));
			r.append("\n");
		}
		r.append("}\n");
		return r.toString();
	}

}
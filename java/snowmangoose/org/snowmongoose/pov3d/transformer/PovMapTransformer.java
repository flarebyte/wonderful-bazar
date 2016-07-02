/*
 * Created on Jul 12, 2005
 *
 */
package org.snowmongoose.pov3d.transformer;

import org.snowmongoose.generator.transformer.IStringTransformer;
import org.snowmongoose.pov3d.PovMap;

/**
 * @author Oliver Huin
 *  
 */
public class PovMapTransformer implements IStringTransformer {

	public final static String INDENT="    ";
	private PovMap map;
	private String name;
	

	/**
	 * @return Returns the name.
	 */
	protected String getName() {
		return name;
	}
	/**
	 * @param name The name to set.
	 */
	protected void setName(String name) {
		this.name = name;
	}
	
	/**
	 * @param name
	 */
	public PovMapTransformer(String name, PovMap map) {
		super();
		this.name = name;
		this.map = map;
		
		
	}
	/*
	 * (non-Javadoc)
	 * 
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		
		if (map == null)
			return "";
		StringBuffer r = new StringBuffer();
		r.append(this.getName());
		r.append("{\n");
		for (int i = 0; i < map.size(); i++) {
			r.append(INDENT).append("[").append(map.getKey(i)).append(" ").append(
					map.getName(i));
			Object[] args = map.getArguments(i);
			for (int j = 0; j < args.length; j++) {
				r.append(" ").append(args[j]);
			}
			r.append("]\n");
		}
		r.append("}\n");
		return r.toString();
	}

}
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
public class PovArgumentsTransformer implements IStringTransformer {

	private Object[] arguments;
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

	protected String getArgumentAsString(int index) {
		Object arg= arguments[index];
		if (arg==null) return "";
		return PovToStringBuilder.toString(arg);
	}

	
	/**
	 * @param name
	 */
	public PovArgumentsTransformer(String name, Object[] args) {
		super();
		this.name = name;
		this.arguments = args==null?new Object[]{}: args;
		
		
	}
	/*
	 * (non-Javadoc)
	 * 
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		StringBuffer r = new StringBuffer();
		r.append(this.getName()).append(" ");
		int args_length = arguments.length;
		for (int i = 0; i < args_length; i++) {
			if (i!=0) r.append(" ");
			r.append(getArgumentAsString(i));
		}
		r.append("\n");
		return r.toString();
	}

}
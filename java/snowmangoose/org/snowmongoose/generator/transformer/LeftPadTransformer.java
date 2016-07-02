/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class LeftPadTransformer implements IStringTransformer{

	private int size;
	private String prefix;
	/**
	 * @param size
	 * @param pad
	 */
	public LeftPadTransformer(int size, String pad) {
		super();
		if (size<=0) throw new RuntimeException("The size must be positive !"+size);
		if (pad==null) throw new RuntimeException("The pad cannot be null !");
		this.size = size;
		this.pad = pad;
		StringBuffer r = new StringBuffer(pad.length()*size);
		for (int i=size;--i>=0;){
			r.append(pad);
		}
		this.prefix=r.toString();
		
	}
	private String pad;
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		return this.prefix+object.toString();
	}

}

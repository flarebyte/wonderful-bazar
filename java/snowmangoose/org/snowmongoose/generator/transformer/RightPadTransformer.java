/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class RightPadTransformer implements IStringTransformer{

	private int size;
	private String suffix;
	/**
	 * @param size
	 * @param pad
	 */
	public RightPadTransformer(int size, String pad) {
		super();
		if (size<=0) throw new RuntimeException("The size must be positive !"+size);
		if (pad==null) throw new RuntimeException("The pad cannot be null !");
		this.size = size;
		this.pad = pad;
		StringBuffer r = new StringBuffer(pad.length()*size);
		for (int i=size;--i>=0;){
			r.append(pad);
		}
		this.suffix=r.toString();
		
	}
	private String pad;
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		return object.toString()+this.suffix;
	}

}

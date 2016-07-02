/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class CenterAlignTransformer implements IStringTransformer{

	private int size;
	/**
	 * @param size
	 * @param pad
	 */
	public CenterAlignTransformer(int size, char pad) {
		super();
		if (size<=0) throw new RuntimeException("The size must be positive !"+size);
		this.size = size;
		this.pad = pad;
	}
	private char pad;
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		String s = object.toString();
		if (s.length()>=this.size) return s.substring(0,this.size); 
		char pad = this.pad;
		int prefix_length=(this.size-s.length())/2;
		int suffix_length= this.size-s.length()-prefix_length;
		
		StringBuffer r = new StringBuffer(this.size);
		//adds prefix
		for (int i = prefix_length; --i>=0;){
			r.append(pad);
		}
		r.append(s);
		//adds suffix
		for (int i = suffix_length; --i>=0;){
			r.append(pad);
		}
		return r.toString();
		
	}

}

/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class AlignTransformer implements IStringTransformer{
	public final static int LEFT_ALIGN=1;
	public final static int RIGHT_ALIGN=2;
	public final static int CENTER_ALIGN=3;
	private int align;
	IStringTransformer alignTransformer;
	
	/**
	 * @param size
	 * @param pad
	 */
	public AlignTransformer(int size, char pad, int align) {
		super();
		this.align = align;
		switch(align){
		case LEFT_ALIGN: alignTransformer = new LeftAlignTransformer(size,pad);break;
		case RIGHT_ALIGN: alignTransformer = new RightAlignTransformer(size,pad);break;
		case CENTER_ALIGN: alignTransformer = new CenterAlignTransformer(size,pad);break;
		default: throw new RuntimeException("Invalid align value !: "+align);
		}
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		return this.alignTransformer.toString(object);
	}
	
}

/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *  
 */
public class CompositeTransformer implements IStringTransformer {

	IStringTransformer[] stringTransformerList;

	/**
	 * @param stringTransformerList
	 */
	public CompositeTransformer(IStringTransformer[] stringTransformerList) {
		super();
		this.stringTransformerList = stringTransformerList;
	}

	public CompositeTransformer(IStringTransformer t1) {
		super();
		this.stringTransformerList = new IStringTransformer[] { t1 };
	}

	public CompositeTransformer(IStringTransformer t1, IStringTransformer t2) {
		super();
		this.stringTransformerList = new IStringTransformer[] { t1, t2 };
	}

	public CompositeTransformer(IStringTransformer t1, IStringTransformer t2,
			IStringTransformer t3) {
		super();
		this.stringTransformerList = new IStringTransformer[] { t1, t2, t3 };
	}

	public CompositeTransformer(IStringTransformer t1, IStringTransformer t2,
			IStringTransformer t3, IStringTransformer t4) {
		super();
		this.stringTransformerList = new IStringTransformer[] { t1, t2,t3, t4 };
	}

	public CompositeTransformer(IStringTransformer t1, IStringTransformer t2,
			IStringTransformer t3, IStringTransformer t4, IStringTransformer t5) {
		super();
		this.stringTransformerList = new IStringTransformer[] { t1,t2,t3,t4,t5 };
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object == null)
			return null;
		if ((this.stringTransformerList == null)
				|| (this.stringTransformerList.length == 0)) {
			return object.toString();
		}
		Object r = object;
		for (int i = 0; i < this.stringTransformerList.length; i++) {
			r = stringTransformerList[i].toString(r);
		}

		return r.toString();
	}

}
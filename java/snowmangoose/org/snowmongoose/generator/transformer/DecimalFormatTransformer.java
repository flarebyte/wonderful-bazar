/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

import java.text.DecimalFormat;

/**
 * @author Oliver Huin
 *
 */
public class DecimalFormatTransformer implements IStringTransformer{
	private String pattern;
    DecimalFormat decimalFormat;


	/**
	 * @param pattern
	 * @param locale
	 */
	public DecimalFormatTransformer(String pattern) {
		super();
		this.pattern = pattern;
		this.decimalFormat = new DecimalFormat(pattern);
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		Number number = (Number) object;
		return this.decimalFormat.format(number);
	}

}

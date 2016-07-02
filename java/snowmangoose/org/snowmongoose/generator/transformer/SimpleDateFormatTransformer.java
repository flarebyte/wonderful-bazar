/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

/**
 * @author Oliver Huin
 *
 */
public class SimpleDateFormatTransformer implements IStringTransformer{
	private String pattern;
    private Locale locale;
    SimpleDateFormat simpleDateFormat;


	/**
	 * @param pattern
	 * @param locale
	 */
	public SimpleDateFormatTransformer(String pattern, Locale locale) {
		super();
		this.pattern = pattern;
		this.locale = locale;
		this.simpleDateFormat = new SimpleDateFormat(pattern,locale);
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		Date date = (Date) object;
		return this.simpleDateFormat.format(date);
	}

}

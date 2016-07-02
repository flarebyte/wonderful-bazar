/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Oliver Huin
 *
 */
public class RegexTransformer implements IStringTransformer{

	private String pattern;
	private String replacement;
	private Pattern compiledpattern;
	/**
	 * @param encloser
	 */
	public RegexTransformer(String pattern, String replacement) {
		super();
		this.pattern=pattern;
		this.replacement = replacement;
		this.compiledpattern = Pattern.compile(pattern);
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		Matcher m =  compiledpattern.matcher(object.toString());
		return m.replaceAll(replacement);
	}
	

}

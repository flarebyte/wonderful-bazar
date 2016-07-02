/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class PrefixAndSuffixTransformer implements IStringTransformer{

	private String prefix;
	private String suffix;
	/**
	 * @param prefix
	 * @param suffix
	 */
	public PrefixAndSuffixTransformer(String prefix, String suffix) {
		super();
		this.prefix = prefix;
		this.suffix = suffix;
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */
	public String toString(Object object) {
		if (object==null) return null;
		StringBuffer r = new StringBuffer(prefix).append(object).append(suffix);
		return r.toString();
	}
}

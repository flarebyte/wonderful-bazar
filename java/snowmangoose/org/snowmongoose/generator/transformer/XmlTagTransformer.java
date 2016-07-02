/*
 * Created on Apr 14, 2005
 *
 */
package org.snowmongoose.generator.transformer;

/**
 * @author Oliver Huin
 *
 */
public class XmlTagTransformer extends PrefixAndSuffixTransformer{

	private String tag;
	
	/**
	 * @param prefix
	 * @param suffix
	 */
	public XmlTagTransformer(String tag) {
		super("<"+tag+">","</"+tag+">");
		this.tag = tag;
	}
	/* (non-Javadoc)
	 * @see org.snowmongoose.generator.transformer.IStringTransformer#toString(java.lang.Object)
	 */

}

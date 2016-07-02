/*
 * Created on Apr 15, 2005
 *
 */
package org.snowmongoose.generator.builder.interpreter.basic;

/**
 * @author Oliver Huin
 *
 */
public class BasicInterpreterEventTags {
	private String startTag;
	private String endTag;
	
	/**
	 * @return Returns the endTag.
	 */
	public String getEndTag() {
		return endTag;
	}
	/**
	 * @param endTag The endTag to set.
	 */
	public void setEndTag(String endTag) {
		this.endTag = endTag;
	}
	/**
	 * @return Returns the startTag.
	 */
	public String getStartTag() {
		return startTag;
	}
	/**
	 * @param startTag The startTag to set.
	 */
	public void setStartTag(String startTag) {
		this.startTag = startTag;
	}
}

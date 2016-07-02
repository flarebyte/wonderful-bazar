/*
 * Created on Apr 15, 2005
 *
 */
package org.snowmongoose.generator.builder.interpreter.basic;

import org.snowmongoose.generator.transformer.IStringTransformer;

/**
 * @author Oliver Huin
 *
 */
public class BasicInterpreterEvent {
	private String tag;
	private BasicInterpreterTagType tagType;
	private IStringTransformer transformer;
	private String pairedTag;
	/**
	 * @param tag
	 * @param tagType
	 * @param transformer
	 */
	public BasicInterpreterEvent(String tag, BasicInterpreterTagType tagType,
			IStringTransformer transformer, String pairedTag ) {
		super();
		this.tag = tag;
		this.tagType = tagType;
		this.transformer = transformer;
		this.pairedTag = pairedTag;
	}
	/**
	 * @return Returns the tag.
	 */
	public String getTag() {
		return tag;
	}
	/**
	 * @return Returns the tagType.
	 */
	public BasicInterpreterTagType getTagType() {
		return tagType;
	}
	/**
	 * @return Returns the transformer.
	 */
	public IStringTransformer getTransformer() {
		return transformer;
	}
	/**
	 * @return Returns the pairedTag.
	 */
	public String getPairedTag() {
		return pairedTag;
	}
}

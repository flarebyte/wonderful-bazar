/*
 * Created on Apr 15, 2005
 *
 */
package org.snowmongoose.generator.builder.interpreter.basic;

/**
 * @author Oliver Huin
 *
 */
public class BasicInterpreterTagType {
	public final static BasicInterpreterTagType START_TAG= new BasicInterpreterTagType(1);
	public final static BasicInterpreterTagType END_TAG= new BasicInterpreterTagType(2);
	
	private int tagType;
	
	/**
	 * @param tagType
	 */
	private BasicInterpreterTagType(int tagType) {
		super();
		this.tagType = tagType;
	}
	
	
	/* (non-Javadoc)
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	public boolean equals(Object obj) {
		BasicInterpreterTagType r = (BasicInterpreterTagType) obj;
		return r.tagType==tagType;
	}
}

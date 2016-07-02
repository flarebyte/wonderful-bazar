package com.flarebyte.cm.com.core;

/**
 * List of documents. Ex: Topic
 * 
 * @author olivier
 * 
 */
public interface Section extends Concept {
	public SectionIterator getChildren();

	public Section getParent();

	public boolean isRoot();

}

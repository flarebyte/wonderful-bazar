package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;

/**
 * A Batch describes a set of ProductInstances of a specific ProductType that
 * are all to be tracked together, usually for quality control purposes.
 * 
 * @author olivier
 * 
 */
public interface Batch extends Concept {

	public ProductType getBatchOfProductType();

}

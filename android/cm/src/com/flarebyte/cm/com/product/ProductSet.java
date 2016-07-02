package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;

/**
 * A ProductSet represents a set of ProductIdentifiers that refer to
 * ProductTypes.
 * 
 * @author olivier
 * 
 */
public interface ProductSet extends Concept {
	public ProductType[] getProductTypeArray();
}

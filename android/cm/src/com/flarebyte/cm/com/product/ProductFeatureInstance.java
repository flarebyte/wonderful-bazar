package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.dc.PropertyValue;

/**
 * A ProductFeatureInstance represents a specific feature (such as color) of a
 * good or service and its value (e.g., blue).
 * 
 * @author olivier
 * 
 */
public interface ProductFeatureInstance {
	public ProductFeatureType getFeatureType();

	public PropertyValue getValue();
}

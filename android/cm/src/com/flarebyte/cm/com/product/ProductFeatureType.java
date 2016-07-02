package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.PropertyValueIterator;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * A ProductFeatureType represents a type of feature (such as color) of a good
 * or service and its range of possible values (e.g., {blue, green, yellow,
 * red}).
 * 
 * @author olivier
 * 
 */
public interface ProductFeatureType extends Concept {

	public PropertyValueIterator getPossibleValues(Property property);
}

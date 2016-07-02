package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.TimePeriod;

/**
 * A ProductType describes the common properties of a set of goods or services.
 * 
 * @author olivier
 * 
 */
public interface ProductType extends Concept {

	public Price[] getPriceArray(Property property);

	public Price[] getPriceArray(Property property, TimePeriod timePeriod);

	public ProductFeatureType getProductFeatureType(Property property);

	public ProductFeatureType[] getProductFeatureTypeArray(Property property);

	public ProductTypeIterator getProductTypeRelationships(Property property);

}

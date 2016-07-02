package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * A PackageType specifies a set of component ProductTypes and rules about how
 * these may be combined to create PackageInstances. A PackageType is a kind of
 * ProductType.Ex: Assigned, Aggregated
 * 
 * @author olivier
 * 
 */
public interface PackageType extends ProductType {
	PricingStrategy getPricingStrategy(Property property);

	ProductSet getProductSet(Property property);

	ProductSet[] getProductSetArray(Property property);

	ProductType getProductType(Property property);

	ProductType[] getProductTypeArray(Property property);

}

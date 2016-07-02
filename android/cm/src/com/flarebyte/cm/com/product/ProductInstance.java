package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * A ProductInstance represents a specific instance of a ProductType.
 * 
 * @author olivier
 * 
 */
public interface ProductInstance extends Concept {

	public Batch getBatch();

	public ProductFeatureInstance[] getFeatureArray(Property property);

	public Price getPrice();

	public ProductType getProductType();

	public int getReservationStatus();

}

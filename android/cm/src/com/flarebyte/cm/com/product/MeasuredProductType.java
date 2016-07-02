package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.quantity.Metric;
import com.flarebyte.cm.lang.quantity.Quantity;

/**
 * A MeasuredProductType represents a kind of ProductType that specifies
 * possible Metrics and a single preferred Metric for measuring Quantities of
 * the product.
 * 
 * @author olivier
 * 
 */
public interface MeasuredProductType extends ProductType {
	public Metric getMetric(Property property);

	public Metric[] getMetricArray(Property property);

	public Quantity getQuantity(Property property);

}

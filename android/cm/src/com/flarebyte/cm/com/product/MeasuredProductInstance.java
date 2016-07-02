package com.flarebyte.cm.com.product;

import com.flarebyte.cm.lang.quantity.Quantity;


/**
 * A MeasuredProductInstance represents a kind of ProductInstance that specifies
 * an amount of some Metric (a Quantity) of the product to be sold.
 * 
 * @author olivier
 * 
 */
public interface MeasuredProductInstance {
	public Quantity getQuantity();

}

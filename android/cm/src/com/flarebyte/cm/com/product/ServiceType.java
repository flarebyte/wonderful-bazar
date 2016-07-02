package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.TimePeriod;

/**
 * A ServiceType is a kind of ProductType that represents a type of service.
 * 
 * @author olivier
 * 
 */
public interface ServiceType extends ProductType {
	public TimePeriod getTimePeriod(Property property);
}

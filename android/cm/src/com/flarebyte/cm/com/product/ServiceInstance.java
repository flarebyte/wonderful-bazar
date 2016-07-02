package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.TimePeriod;

/**
 * A ServiceInstance represents an instance or execution of a ServiceType
 * delivered to one or more Parties.
 * 
 * @author olivier
 * 
 */
public interface ServiceInstance extends ProductInstance {
	public ServiceDeliveryStatus getServiceDeliveryStatus(Property property);

	public TimePeriod getTimePeriod(Property property);
}

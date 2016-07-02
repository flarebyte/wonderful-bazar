package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.com.order.event.OrderEventIterator;

/**
 * An Order represents a record of a request by a buyer for a seller to supply
 * some goods or services.
 * 
 * @author olivier
 * 
 */
public interface Order extends Concept {
	public AgentSummary getAgentSummary(Property property);

	public OrderLineIteraror getChargeLines();

	public OrderEventIterator getEvents();

	public OrderStatus getOrderStatus(Property property);

	public TermsAndConditions getTermsAndConditions();
}

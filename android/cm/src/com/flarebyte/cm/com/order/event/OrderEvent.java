package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.agent.AgentSignature;
import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.com.order.Order;

public interface OrderEvent extends Concept {
	public AgentSignature getAgentSignature(Property property);

	public AgentSignature[] getAgentSignatureArray(Property property);

	public Order getOrder();

	public OrderEventType getOrderEventType();

	public Boolean isProcessed(Property property);

}

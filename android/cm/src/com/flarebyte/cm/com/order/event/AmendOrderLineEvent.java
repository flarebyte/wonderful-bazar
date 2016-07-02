package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.order.OrderLine;

public interface AmendOrderLineEvent extends OrderEvent {
	public OrderLine getNewOrderLine();

	public OrderLine getOriginalOrderLine();

}

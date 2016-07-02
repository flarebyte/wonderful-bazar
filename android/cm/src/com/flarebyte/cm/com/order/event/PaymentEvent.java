package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.order.OrderLine;

public interface PaymentEvent extends OrderEvent {
	public Invoice getInvoice();

	public OrderLine getOrderLine();
}

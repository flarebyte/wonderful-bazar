package com.flarebyte.cm.com.order.event;

public interface InvoiceEvent extends PaymentEvent {
	public DespatchEvent getDespatchEvent();
}

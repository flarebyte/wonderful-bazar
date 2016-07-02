package com.flarebyte.cm.com.order.event;

public interface ReceiptEvent extends OrderEvent {
	public ReceiptLineIterator getReceiptLines();
}

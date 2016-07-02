package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.order.OrderLine;

public interface ReceiptLine extends Concept {
	public Integer getNumberAccepted();

	public Integer getNumberReceived();

	public Integer getNumberRejected();

	public OrderLine getOrderLine();

	public RejectedItemIterator getRejectedItems();

	public Boolean isAssessed();

}

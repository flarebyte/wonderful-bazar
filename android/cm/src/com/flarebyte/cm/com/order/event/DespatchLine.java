package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.order.OrderLine;

public interface DespatchLine extends Concept {
	public Integer getNumberDespatched();

	public Integer getNumberRejected();

	public OrderLine getOrderLine();

	public RejectedItemIterator getRejectedItems();

}

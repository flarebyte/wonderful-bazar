package com.flarebyte.cm.com.order.event;


public interface DespatchEvent extends OrderEvent {
	public DespatchLineIterator getDespatchLines();
}

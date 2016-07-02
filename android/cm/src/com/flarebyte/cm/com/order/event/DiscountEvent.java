package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.product.Price;

public interface DiscountEvent extends OrderEvent {
	public Price calculateDiscountedPrice(Price price);
}

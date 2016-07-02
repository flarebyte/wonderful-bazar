package com.flarebyte.cm.lang.money;

import java.math.BigDecimal;


public interface Money {
	BigDecimal getBigDecimal();

	public ZCurrency getCurrency();
}

package com.flarebyte.cm.com.product;

import com.flarebyte.cm.lang.TimePeriod;
import com.flarebyte.cm.lang.money.Money;

/**
 * The Price represents the amount of money that must be paid in order to
 * purchase a good or service.
 * 
 * @author olivier
 * 
 */
public interface Price {
	public Money getAmount();

	public TimePeriod getValidity();
}

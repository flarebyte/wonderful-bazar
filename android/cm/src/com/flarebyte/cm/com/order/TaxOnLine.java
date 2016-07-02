package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.money.Money;

public interface TaxOnLine extends Concept {
	public Money calculate(Property property, Money amount);

	public Float getRateAsFloat(Property property);

	public TaxationType getTaxationType(Property property);

}

package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

public interface SalesTaxPolicy extends Concept {
	public Float getRateAsFloat(Property property);

	public TaxationType getTaxationType(Property property);
}

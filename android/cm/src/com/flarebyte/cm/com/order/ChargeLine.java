package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.core.Fragment;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.money.Money;

public interface ChargeLine extends Fragment {
	public Money getAmount();

	public OrderLine getOrderLine();

	public TaxOnLine getTaxOnLine(Property property);

	public TaxOnLine[] getTaxOnLineArray(Property property);

}

package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.com.product.ProductType;
import com.flarebyte.cm.lang.money.Money;

public interface OrderLine extends Concept {

	public AgentSummary getAgentSummary(Property property);

	public ChargeLine getChargeLine(Property property);

	public ChargeLine[] getChargeLineArray(Property property);

	public Integer getNumberOrdered();

	public ProductType getProductType();

	public TaxOnLine getTaxOnLine(Property property);

	public TaxOnLine[] getTaxOnLineArray(Property property);

	public Money getUnitPrice();

}

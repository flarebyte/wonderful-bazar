package com.flarebyte.cm.com.order;

import com.flarebyte.cm.com.agent.Address;
import com.flarebyte.cm.com.agent.Agent;
import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

public interface AgentSummary extends Concept {
	public Address getAddress(Property property);

	public Address[] getAddressArray(Property property);

	public Agent getAgent();

}

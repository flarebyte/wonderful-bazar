package com.flarebyte.cm.com.core;

import com.flarebyte.cm.com.agent.Address;
import com.flarebyte.cm.com.agent.Agent;
import com.flarebyte.cm.com.agent.AgentIterator;
import com.flarebyte.cm.lang.TimePeriod;

public interface Event extends Concept {
	public Address getAddress();

	public Agent getCreatedBy();

	public AgentIterator getGuests(String... options);

	public TimePeriod getTimePeriod();

}

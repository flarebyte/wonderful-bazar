package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.order.AgentSummary;

public interface AmendAgentSummaryEvent extends OrderEvent {
	public AgentSummary getNewAgentSummary();

	public AgentSummary getOriginalAgentSummary();

}

package com.flarebyte.cm.com.order.event;

import com.flarebyte.cm.com.order.TermsAndConditions;

public interface AmendTermsAndConditionsEvent extends OrderEvent {
	public TermsAndConditions getNewTermsAndConditions();

	public TermsAndConditions getOriginalTermsAndConditions();

}

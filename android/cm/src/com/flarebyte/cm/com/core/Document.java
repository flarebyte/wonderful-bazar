package com.flarebyte.cm.com.core;

import com.flarebyte.cm.com.agent.Agent;
import com.flarebyte.cm.com.agent.AgentIterator;

public interface Document extends Concept {
	public Hyperlink[] getAttached();

	// public DocumentCopyright getCopyright();

	public Agent getFrom();

	// public ParentalGuidance getParentalGuidance();

	public DocumentPart[] getParts();

	public DocumentPrivacy getPrivacy();

	public AgentIterator getRecipients();

	public DocumentSignature getSignature();

	public DocumentState getState();

}

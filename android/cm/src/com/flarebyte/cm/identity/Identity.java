package com.flarebyte.cm.identity;

import com.flarebyte.cm.com.party.Party;

public interface Identity {
	public Party getParty();

	public Profile[] getProfiles();

}

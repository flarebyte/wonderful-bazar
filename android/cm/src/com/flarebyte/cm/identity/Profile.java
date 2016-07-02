package com.flarebyte.cm.identity;

import java.net.URI;

import com.flarebyte.cm.com.party.Party;

public interface Profile {
	public Credentials getCredentials();

	public Identity getIdentity();

	public Party getParty();

	public ProfilePrivacy getPrivacy();

	public URI getProfileType();

	public Role[] getRoles();

}

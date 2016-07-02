package com.flarebyte.cm.trash.admin;

import com.flarebyte.cm.com.facet.Configurable;
import com.flarebyte.cm.com.facet.UriIdentifiable;

public interface SocialAccount extends UriIdentifiable, Configurable {

	public User[] filterAdmins(final String... options);

	public UserIterator filterUsers(final String... options);

}

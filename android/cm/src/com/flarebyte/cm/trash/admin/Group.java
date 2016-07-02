package com.flarebyte.cm.trash.admin;

import com.flarebyte.cm.com.facet.Lifecycle;
import com.flarebyte.cm.com.facet.PrivacyAware;
import com.flarebyte.cm.com.facet.UriIdentifiable;


public interface Group extends Contact, UriIdentifiable, Labelled, Lifecycle,
		PrivacyAware {
	public ContactIterator getAdministrators(String... options);

	public ContactIterator getMembers(String... options);
}

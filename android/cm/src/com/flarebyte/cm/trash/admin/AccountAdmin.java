package com.flarebyte.cm.trash.admin;

import java.net.URI;

import com.flarebyte.cm.app.admin.billing.BillingInformation;
import com.flarebyte.cm.com.facet.Configurable;
import com.flarebyte.cm.com.facet.UriIdentifiable;

public interface AccountAdmin extends UriIdentifiable, Configurable {
	public Account getAccount();

	public MailBox getMailbox(String... options);

	public BillingInformation getPersonalInformation();

	public URI getType();
}

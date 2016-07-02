package com.flarebyte.cm.trash.admin;

import com.flarebyte.cm.app.admin.billing.PerformanceAware;
import com.flarebyte.cm.app.admin.billing.ProviderInformation;
import com.flarebyte.cm.app.admin.billing.TransactionIterator;
import com.flarebyte.cm.app.admin.billing.UsageAware;
import com.flarebyte.cm.com.facet.Configurable;
import com.flarebyte.cm.com.facet.UriIdentifiable;

public interface Account extends UriIdentifiable, Configurable, UsageAware,
		PerformanceAware {

	public AccountAdmin[] filterAccountAdmins(final String... options);

	public Credential[] filterCredentials(final String... options);

	public ServiceIterator filterServices(String options);

	public SocialAccountIterator filterSocialAccounts(String... options);

	public TransactionIterator filterTransactions(String options);

	public ProviderInformation getProviderInformation();
}

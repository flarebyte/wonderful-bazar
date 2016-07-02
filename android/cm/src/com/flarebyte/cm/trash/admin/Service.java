package com.flarebyte.cm.trash.admin;

import java.net.URI;

import com.flarebyte.cm.app.admin.billing.PerformanceAware;
import com.flarebyte.cm.app.admin.billing.UsageAware;
import com.flarebyte.cm.com.facet.Configurable;
import com.flarebyte.cm.com.facet.Documentable;
import com.flarebyte.cm.com.facet.Taggable;
import com.flarebyte.cm.com.facet.UriIdentifiable;
import com.flarebyte.cm.com.facet.Versionable;

public interface Service extends UriIdentifiable, Documentable, Taggable,
		Configurable, Versionable, UsageAware, PerformanceAware {
	public Account getAccount();

	public URI getStatus();

}

package com.flarebyte.cm.trash.admin;

import com.flarebyte.cm.app.admin.billing.PerformanceAware;
import com.flarebyte.cm.app.admin.billing.UsageAware;
import com.flarebyte.cm.com.facet.UriIdentifiable;

public interface Operation extends UriIdentifiable, UsageAware,
		PerformanceAware {
	public int getRequiredUnits();

}

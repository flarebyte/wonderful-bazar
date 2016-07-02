package com.flarebyte.cm.com.core;

import com.flarebyte.cm.com.core.dc.ResourceFilter;

public interface Filter {
	public String[] getOptions();

	public ResourceFilter[] getResourceFilterArray();
}

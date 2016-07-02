package com.flarebyte.cm.com.core;

import com.flarebyte.cm.com.core.dc.DublinCore;
import com.flarebyte.cm.com.core.dc.ValueAccessor;

public interface Fragment extends ValueAccessor {
	public Concept getOwner();

	public DublinCore getResourceDescription();

}

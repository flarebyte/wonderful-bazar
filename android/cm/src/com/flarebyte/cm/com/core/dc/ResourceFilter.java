package com.flarebyte.cm.com.core.dc;

import com.flarebyte.cm.com.core.dc.vocabulary.Term;

public interface ResourceFilter {
	public Term getTerm();

	public String getValueAsString();
}

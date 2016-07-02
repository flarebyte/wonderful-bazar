package com.flarebyte.cm.com.core.owl;

import java.net.URI;

public interface OwlDataLiteral {
	public Object getLanguageTag();

	public URI getTypeAsUri();

	public String getValueAsString();
}

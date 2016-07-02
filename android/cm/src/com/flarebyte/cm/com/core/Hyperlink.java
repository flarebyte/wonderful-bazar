package com.flarebyte.cm.com.core;

import java.net.URI;

public interface Hyperlink {
	public String getForwardRelationship();

	public String getMimeType();

	public String getReverseRelationship();

	public String getTitle();

	public URI getUri();
}

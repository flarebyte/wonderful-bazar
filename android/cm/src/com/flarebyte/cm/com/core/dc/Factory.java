package com.flarebyte.cm.com.core.dc;

import java.net.URI;

public interface Factory {
	@SuppressWarnings("rawtypes")
	public Class createClass(URI uri);

	public Object createObject(URI uri, String value);
}

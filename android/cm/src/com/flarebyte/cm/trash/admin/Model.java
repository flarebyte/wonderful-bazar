package com.flarebyte.cm.trash.admin;

import java.util.Locale;

import com.flarebyte.cm.com.facet.Accessible;
import com.flarebyte.cm.com.facet.Documentable;
import com.flarebyte.cm.com.facet.UriIdentifiable;
import com.flarebyte.cm.com.facet.Versionable;

public interface Model extends UriIdentifiable, Versionable,
		Accessible, Documentable {
	public String getContent();

	public String getEncoding();

	public Locale getLocale();

	public String getMimeType();

}

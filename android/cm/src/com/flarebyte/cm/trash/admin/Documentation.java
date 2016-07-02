package com.flarebyte.cm.trash.admin;

import java.net.URI;
import java.util.Calendar;

import com.flarebyte.cm.com.facet.UriIdentifiable;
import com.flarebyte.cm.com.facet.Versionable;

public interface Documentation extends UriIdentifiable, Versionable {
	public URI[] getAuthors();

	public Calendar getCreated();

	public String getDescription();

	public URI getIcon();

	public String getLabel();

	public URI[] getSeeAlso();

	public String getSince();

	public Calendar getUpdated();

	public boolean isActive();

	public boolean isDeprecated();

}

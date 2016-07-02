package com.flarebyte.cm.trash.admin;

import java.net.URI;
import java.util.Calendar;

import com.flarebyte.cm.com.facet.UriIdentifiable;


public interface Contact extends UriIdentifiable, Labelled {

	public URI getContactType();

	public Calendar getJoined();

	public Calendar getLastActive();

	public String getOnlineStatus();

	public URI[] getRoles();

}

package com.flarebyte.cm.trash.admin;

import java.util.Calendar;

import com.flarebyte.cm.com.facet.Lifecycle;
import com.flarebyte.cm.com.facet.PrivacyAware;
import com.flarebyte.cm.com.facet.UriIdentifiable;


public interface Event extends UriIdentifiable, Labelled, Lifecycle,
		PrivacyAware {

	public Contact getCreatedBy();

	public Calendar getEndTime();

	public ContactIterator getGuests(String... options);

	public String getLocation();

	public Calendar getStartTime();

}

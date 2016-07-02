package com.flarebyte.cm.com.core;

import java.net.URI;
import java.util.Calendar;

import com.flarebyte.cm.com.core.dc.DublinCore;
import com.flarebyte.cm.com.core.dc.ValueAccessor;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * 
 * @author olivier
 * 
 */
public interface Concept extends ValueAccessor, Subscribable {

	public Concept duplicate();

	public Calendar getCalendar(Property property);

	public URI getIdentifier();

	public Calendar getModified();

	public DublinCore getResourceDescription();

	public String[] getTags();

	public URI getVersion();

}

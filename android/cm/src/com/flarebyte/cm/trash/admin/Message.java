package com.flarebyte.cm.trash.admin;

import java.util.Locale;

import com.flarebyte.cm.com.facet.Lifecycle;
import com.flarebyte.cm.com.facet.Taggable;
import com.flarebyte.cm.com.facet.UriIdentifiable;
import com.flarebyte.cm.com.facet.Votable;
import com.flarebyte.cm.com.facet.WorkflowAware;

public interface Message extends UriIdentifiable, Taggable, Votable, Lifecycle,
		WorkflowAware {
	public Message copy();

	public Hyperlink[] getAttached();

	public Contact getFrom();

	public int getJunkVotes();

	public Locale getLocale();

	public Message getPrevious();

	public ContactIterator getRecipients();

	public Section[] getSections();

	public String getSubject();

	public Topic getTopic();

	public boolean isEditable();

	public boolean isMarkedJunk();

	public boolean isMarkedRead();

}

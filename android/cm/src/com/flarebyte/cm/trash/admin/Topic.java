package com.flarebyte.cm.trash.admin;

import com.flarebyte.cm.com.facet.Lifecycle;
import com.flarebyte.cm.com.facet.Taggable;
import com.flarebyte.cm.com.facet.UriIdentifiable;
import com.flarebyte.cm.com.facet.Votable;


public interface Topic extends UriIdentifiable, Labelled, Taggable,
		Votable, Lifecycle {
	public CategoryIterator getCategories();

}

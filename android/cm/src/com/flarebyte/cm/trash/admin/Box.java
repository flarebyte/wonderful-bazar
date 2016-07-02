package com.flarebyte.cm.trash.admin;

import java.net.URI;

import com.flarebyte.cm.com.facet.Configurable;
import com.flarebyte.cm.com.facet.UriIdentifiable;


public interface Box extends UriIdentifiable, Configurable {
	public CounterIterator count(String... options);

	public void delete(URI id, String... options);

	public String[] getCapabilities();

	public MainBox getMainBox();

}

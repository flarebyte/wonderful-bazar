package com.flarebyte.cm.com.facet;

import java.util.Calendar;

public interface Credential {
	public void decorate(final Object object, final String... options);

	public Calendar getValidFrom();

	public Calendar getValidTo();

	public boolean isValid();

}

package com.flarebyte.cm.com.facet;

import java.util.Calendar;

public interface Lifecycle {
	public Calendar getCreated();

	public Calendar getModified();

	public Calendar getPlannedArchivage();

	public Calendar getPlannedDeletion();
}

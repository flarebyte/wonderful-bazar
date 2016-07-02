package com.flarebyte.cm.trash.admin;

import java.net.URI;
import java.util.Calendar;

public interface Counter {
	public long getCount();

	public Calendar getLatest();

	public URI getUri();
}

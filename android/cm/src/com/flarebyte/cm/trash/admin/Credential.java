package com.flarebyte.cm.trash.admin;

import java.util.Calendar;

public interface Credential {
	public void createNew(String id);

	public Calendar getCreated(String id);

	public String getString(String id);

	public boolean isActive(String id);
}

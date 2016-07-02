package com.flarebyte.cm.trash.admin;

import java.net.URI;

public interface AccountSharable {
	public Account[] filter(String... options);

	public Account get(URI uri);

	public boolean isShared();
}

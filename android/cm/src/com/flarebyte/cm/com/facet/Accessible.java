package com.flarebyte.cm.com.facet;

import java.net.URI;

import com.flarebyte.cm.trash.admin.User;

public interface Accessible {
	boolean canRead(URI uri);

	boolean canRead(User user);

	boolean canWrite(URI uri);

	boolean canWrite(User user);

}

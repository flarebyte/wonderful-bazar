package com.flarebyte.cm.trash.admin;

import java.net.URI;

public interface SubscriptionBox extends Box {
	public SubscriptionIterator filterSubscriptions(String... options);

	public void subscribe(URI path, String... options);

	public void unsubscribe(URI path, String... options);

}

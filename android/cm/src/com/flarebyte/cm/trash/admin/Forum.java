package com.flarebyte.cm.trash.admin;

import java.net.URI;

public interface Forum {
	public CounterIterator countMessages(String... options);

	public MessageIterator filterMessages(String... options);

	public MessageIterator filterMessages(URI categoryOrTopicId,
			String... options);

	public CategoryIterator getCategories(String... options);

	public TopicIterator getTopics(String... options);

}

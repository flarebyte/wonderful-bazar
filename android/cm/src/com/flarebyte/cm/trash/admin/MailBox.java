package com.flarebyte.cm.trash.admin;

import java.net.URI;

public interface MailBox extends Box {

	public MessageIterator filter(String... options);

	public Message get(URI messageId, String... options);

	public MessageIterator getHistory(URI messageId, String... options);

	public TopicIterator getTopics(String... options);

	public MessageIterator search(String searchTerm, String... options);

	public void send(Message message, String... options);

}

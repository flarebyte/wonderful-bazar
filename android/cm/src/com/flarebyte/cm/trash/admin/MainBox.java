package com.flarebyte.cm.trash.admin;

public interface MainBox {

	public ContactBox getContactBox(String... options);

	public EventBox getEventBox(String... options);

	public ForumBox getForumBox(String... options);

	public GroupBox getGroupBox(String... options);

	public MailBox getMailBox(String... options);

	public SubscriptionBox getSubscriptionBox(String... options);

	public TaskBox getTaskBox(String... options);

}

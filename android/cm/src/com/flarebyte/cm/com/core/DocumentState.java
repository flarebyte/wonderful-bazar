package com.flarebyte.cm.com.core;

public interface DocumentState extends Concept {
	public boolean isCancelled();

	public boolean isCompleted();

	public boolean isDraft();

	public boolean isFinal();

	public boolean isInProgress();

	public boolean isRead();

	public boolean isReviewed();

	public boolean isToDo();

}

package com.flarebyte.cm.action;

public interface TimeAware {
	public long getEstimatedDuration();

	public long getMaxCachingTime();

	public long getModified();

	public long validAfter();

	public long validUntil();

}

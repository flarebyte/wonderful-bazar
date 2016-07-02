package com.flarebyte.cm.com.core;

/**
 * No Print, Destroy After Reading, Internal Use Only, Please Share,
 * Confidential, Anonymous
 * 
 * @author olivier
 * 
 */
public interface DocumentPrivacy extends Concept {
	public boolean isAnonymous();

	public boolean isConfidential();

	public boolean isDestroyedAfterReading();

	public boolean isNotPrintable();

	public boolean isShareable();

}

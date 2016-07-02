package com.flarebyte.cm.com.facet;


public interface Authenticable<E> {
	public Credential getCredential(final E profile);
}

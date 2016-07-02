package com.flarebyte.cm.trash;

import android.net.Uri;

public final class SemanticId implements Comparable<SemanticId> {
    private final Uri resourceUri;

    public SemanticId(final String resourceUriStr) {
	super();
	this.resourceUri = Uri.parse(resourceUriStr);
    }

    public SemanticId(final Uri resourceUri) {
	super();
	this.resourceUri = resourceUri;
    }

    @Override
    public int compareTo(final SemanticId another) {
	return this.resourceUri.compareTo(another == null ? null : another.resourceUri);
    }

    public Uri getCurieUri() {
	return this.resourceUri;
    }

    public Uri getResourceUri() {
	return this.resourceUri;
    }

}
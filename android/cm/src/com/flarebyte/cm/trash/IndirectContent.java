package com.flarebyte.cm.trash;

import java.net.URI;

public interface IndirectContent {
    public void free();

    public Long getLength();

    public URI getValueURI();

    boolean isAvailable();

    boolean load();

}

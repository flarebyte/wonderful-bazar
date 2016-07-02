package com.flarebyte.cm.trash;

import java.io.StringReader;

public interface IndirectString extends IndirectContent {

	public String getString();

	public StringReader getStringReader();

	public String getSubString(long pos, int length);

}

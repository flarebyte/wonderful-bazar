package com.flarebyte.cm.lang;

import java.net.URI;
import java.net.URL;

public interface StrictRecord {
	public Boolean getBolean(Enum<?> id);

	public Byte getByte(Enum<?> id);

	public String getCalendar(Enum<?> id);

	public Double getDouble(Enum<?> id);

	public Float getFloat(Enum<?> id);

	public Integer getInteger(Enum<?> id);

	public Number getNumber(Enum<?> id);

	public Short getShort(Enum<?> id);

	public String getString(Enum<?> id);

	public URI getURI(Enum<?> id);

	public URL getURL(Enum<?> id);

}

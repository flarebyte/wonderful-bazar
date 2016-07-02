package com.flarebyte.cm.conv;

public interface Converter<T> {
	T fromString(final String value);

	String toString(T value);
}

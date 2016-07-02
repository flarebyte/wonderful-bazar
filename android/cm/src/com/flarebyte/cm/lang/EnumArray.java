package com.flarebyte.cm.lang;

public interface EnumArray<E extends Enum<E>, T> {
	E get(E id);

	void set(E id, T value);

	int size();
}

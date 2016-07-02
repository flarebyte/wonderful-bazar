package com.essay.medea;

public interface Converter {
	public Element fromString(String content);
	public String toString(Element root);
}

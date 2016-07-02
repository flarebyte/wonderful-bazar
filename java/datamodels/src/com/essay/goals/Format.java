package com.essay.goals;

public enum Format {
	XML ("xml"), JSON("json");

	private final String name;
    Format(String name) {
        this.name = name;
    }

}

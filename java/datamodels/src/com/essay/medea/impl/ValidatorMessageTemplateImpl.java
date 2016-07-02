package com.essay.medea.impl;

import com.essay.medea.validators.ValidatorMessageTemplate;

public class ValidatorMessageTemplateImpl implements ValidatorMessageTemplate {
	String id;
	public ValidatorMessageTemplateImpl(String id, String name) {
		super();
		this.id = id;
		this.name = name;
	}

	String name;
	
	@Override
	public String getId() {
		return id;
	}

	@Override
	public String getName() {
		return name;
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "ValidatorMessageTemplateImpl [id=" + id + ", name=" + name
				+ "]";
	}

}

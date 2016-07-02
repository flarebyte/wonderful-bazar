package com.essay.medea.impl;

import java.util.Arrays;
import java.util.Locale;

import com.essay.medea.ValidatorMessage;
import com.essay.medea.validators.ValidatorMessageTemplate;

public class ValidatorMessageImpl implements ValidatorMessage {
	int severity = ValidatorMessage.ERROR;
	
	public ValidatorMessageImpl(int severity, String issuer, ValidatorMessageTemplate template, Object... params) {
		super();
		this.severity = severity;
		this.issuer = issuer;
		this.template=template;
		this.params=params;
	}

	String issuer;
	ValidatorMessageTemplate template;
	Object[] params;


	@Override
	public String getMessage(Locale locale) {
		return template.toString();
	}

	@Override
	public int getSeverity() {
		return severity;
	}

	@Override
	public String getIssuer() {
		return issuer;
	}

	@Override
	public ValidatorMessageTemplate getTemplate() {
		return template;
	}

	@Override
	public Object[] getParams() {
		return params;
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "ValidatorMessageImpl [issuer=" + issuer + ", params=" + Arrays.toString(params)
				+ ", severity=" + severity + ", template=" + template + "]";
	}

}

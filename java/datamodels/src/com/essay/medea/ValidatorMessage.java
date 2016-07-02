package com.essay.medea;

import java.util.Locale;

import com.essay.medea.validators.ValidatorMessageTemplate;

public interface ValidatorMessage {
	public final static int ERROR=0;
	public final static int WARNING=1;
	public String getIssuer(); 
	public ValidatorMessageTemplate getTemplate();
	public Object[] getParams();
	public String getMessage(Locale locale);
	public int getSeverity(); 
}

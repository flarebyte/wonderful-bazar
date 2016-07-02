package com.essay.medea.impl;

import com.essay.medea.validators.ValidatorMessageTemplate;

public interface ValidatorMessagesRes {
	public final static ValidatorMessageTemplate UNKNOWN_ELEMENT=new ValidatorMessageTemplateImpl("","");
	public final static ValidatorMessageTemplate UNKNOWN_ATTRIBUTE=new ValidatorMessageTemplateImpl("","");
	public final static ValidatorMessageTemplate ACCESS_FORBIDDEN_ELEMENT=new ValidatorMessageTemplateImpl("","");
	public final static ValidatorMessageTemplate ACCESS_FORBIDDEN_ATTRIBUTE=new ValidatorMessageTemplateImpl("","");
}

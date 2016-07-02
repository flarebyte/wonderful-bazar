package com.essay.medea.impl;

import java.util.ArrayList;
import java.util.List;

import com.essay.medea.ValidatorContext;
import com.essay.medea.ValidatorMessage;

public class ValidatorContextImpl implements ValidatorContext {
	
	List<ValidatorMessage> messages = new ArrayList<ValidatorMessage>();
	@Override
	public void addMessage(ValidatorMessage msg) {
		messages.add(msg);

	}

	@Override
	public List<ValidatorMessage> getMessages() {
		return messages;
	}

}

package com.essay.medea;

import java.util.List;

public interface ValidatorContext {
	public void addMessage(ValidatorMessage msg);
	public List<ValidatorMessage> getMessages();
}

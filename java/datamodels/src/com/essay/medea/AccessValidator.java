package com.essay.medea;

public interface AccessValidator {
	public boolean validate(ValidatorContext context, SubjectAccess access);
	public AccessApi getAccessAPI();
}

package com.essay.medea;

public interface ValidatorApi {
	public boolean validate(ValidatorContext context, Element element, boolean recursive);
	public boolean validate(ValidatorContext context, String xpath, String attributeName,  Object value);
	public boolean validate(ValidatorContext context, String xpath, Object value);
	public void registerElementValidatorValue(String xpath, ValueValidator valueValidator);
	public void registerValueValidator(String xpath, String attributeName, ValueValidator valueValidator);

}

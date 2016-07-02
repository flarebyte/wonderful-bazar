package com.essay.medea;

public interface ValueValidator {
	public final static String DEFAULT="::DEFAULT::";
	public final static String NONE="::NONE::";
	public boolean validate(ValidatorContext context, Object value);
	public ValidatorApi getValidatorAPI();
	public void setValidatorAPI(ValidatorApi validatorApi);


}

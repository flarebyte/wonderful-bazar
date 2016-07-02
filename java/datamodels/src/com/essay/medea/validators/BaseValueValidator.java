package com.essay.medea.validators;

import com.essay.medea.ValidatorApi;
import com.essay.medea.ValueValidator;

public abstract class BaseValueValidator implements ValueValidator {
	ValidatorApi validatorApi;
	
	@Override
	public void setValidatorAPI(ValidatorApi validatorApi){
		this.validatorApi=validatorApi;
	}
	@Override
	public ValidatorApi getValidatorAPI() {
		return validatorApi;
	}
	
	protected final boolean isNoValue(Object value){
		if (value==null) return true;
		if (value.toString().trim().isEmpty()) return true;
		if (ValueValidator.NONE.equals(value)) return true;
		if (ValueValidator.DEFAULT.equals(value)) return true;
		return false;
	}

}

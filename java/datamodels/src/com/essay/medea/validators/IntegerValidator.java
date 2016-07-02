package com.essay.medea.validators;

import com.essay.medea.ValidatorContext;

public class IntegerValidator extends BaseValueValidator {

	@Override
	public boolean validate(ValidatorContext context, Object value) {
		if (isNoValue(value)) return true;
		boolean r = false;
		try {
			Integer.parseInt(value.toString());
			r=true;
		}catch (NumberFormatException e){
			r=false;
		}
		return r;
	}

}

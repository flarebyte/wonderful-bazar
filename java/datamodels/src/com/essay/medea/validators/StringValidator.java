package com.essay.medea.validators;

import com.essay.medea.ValidatorContext;

public class StringValidator extends BaseValueValidator {

	@Override
	public boolean validate(ValidatorContext context, Object value) {
		if (isNoValue(value)) return true;
		return true;
	}

}

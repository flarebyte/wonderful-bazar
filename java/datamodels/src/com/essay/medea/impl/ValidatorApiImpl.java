package com.essay.medea.impl;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import com.essay.medea.Element;
import com.essay.medea.ValidatorApi;
import com.essay.medea.ValidatorContext;
import com.essay.medea.ValidatorMessage;
import com.essay.medea.ValueValidator;
import com.essay.medea.validators.ValidatorMessageTemplate;

public class ValidatorApiImpl implements ValidatorApi {
	Map<String,ValueValidator> valueValidators = new HashMap<String,ValueValidator>();

	@Override
	public void registerElementValidatorValue(String xpath,
			ValueValidator valueValidator) {
		valueValidator.setValidatorAPI(this);
		valueValidators.put(xpath, valueValidator);

	}

	@Override
	public void registerValueValidator(String xpath, String attributeName,
			ValueValidator valueValidator) {
		valueValidator.setValidatorAPI(this);
		valueValidators.put(xpath+"@"+attributeName, valueValidator);

	}

	@Override
	public boolean validate(ValidatorContext context, Element element, boolean recursive) {
		boolean pass = validate(context,element.getXpath(),element.getText());
		if (!pass) return false;
		Map<String, String> attrs = element.getAttributes();
		Set<String> attributeNames = attrs.keySet();
		for (String name: attributeNames){
			boolean attr_pass = validate(context,element.getXpath(),name,attrs.get(name));
			if (!attr_pass) pass=false;
		}
		if (!recursive) return pass;
		for (Element child: element.getChildren()){
			boolean attr_pass = validate(context,child,recursive);
			if (!attr_pass) pass=false;
		}
		return pass;
	}
	
	@Override
	public boolean validate(ValidatorContext context, String xpath,
			 Object value) {
		String id = xpath;
		ValueValidator validator = valueValidators.get(id);
		if (validator==null) {
			/*fails*/
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.UNKNOWN_ATTRIBUTE);
			context.addMessage(msg);
			return false;
		}
		return validator.validate(context, value);

	}

	@Override
	public boolean validate(ValidatorContext context, String xpath,
			String attributeName, Object value) {
		String id = xpath+"@"+attributeName;
		ValueValidator validator = valueValidators.get(id);
		if (validator==null) {
			/*fails*/
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.UNKNOWN_ATTRIBUTE);
			context.addMessage(msg);
			return false;
		}
		return validator.validate(context, value);

	}

	

	

}

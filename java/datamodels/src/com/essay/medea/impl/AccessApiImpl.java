package com.essay.medea.impl;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import com.essay.medea.AccessApi;
import com.essay.medea.AccessValidator;
import com.essay.medea.Element;
import com.essay.medea.SubjectAccess;
import com.essay.medea.ValidatorContext;
import com.essay.medea.ValidatorMessage;

public class AccessApiImpl implements AccessApi {
	Map<String,AccessValidator> accessValidators = new HashMap<String,AccessValidator>();


	@Override
	public void registerElementAccessValidator(String xpath,
			AccessValidator accessValidator) {
		accessValidators.put(xpath, accessValidator);

	}

	@Override
	public void registerValueAccessValidator(String xpath,
			String attributeName, AccessValidator accessValidator) {
		accessValidators.put(xpath+"@"+attributeName, accessValidator);

	}

	@Override
	public boolean validate(ValidatorContext context, 
			Element element, SubjectAccess access, boolean recursive) {
		boolean pass = validate(context,element.getXpath(),access);
		if (!pass) return false;
		Map<String, String> attrs = element.getAttributes();
		Set<String> attributeNames = attrs.keySet();
		for (String name: attributeNames){
			boolean attr_pass = validate(context,element.getXpath(),name,access);
			if (!attr_pass) pass=false;
		}
		if (!recursive) return pass;
		for (Element child: element.getChildren()){
			boolean attr_pass = validate(context,child,access,recursive);
			if (!attr_pass) pass=false;
		}
		return pass;
	}

	@Override
	public boolean validate(ValidatorContext context, String xpath,
			String attributeName, SubjectAccess access) {
		String id = xpath+"@"+attributeName;
		AccessValidator validator = accessValidators.get(id);
		if (validator==null) {
			/*fails*/
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.ACCESS_FORBIDDEN_ATTRIBUTE,xpath,attributeName);
			context.addMessage(msg);
			return false;
		}
		boolean r = validator.validate(context, access);
		if (!r){
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.ACCESS_FORBIDDEN_ATTRIBUTE,xpath,attributeName);
			context.addMessage(msg);
		}
		return r;
	}

	@Override
	public boolean validate(ValidatorContext context, String xpath,
			SubjectAccess access) {
		String id = xpath;
		AccessValidator validator = accessValidators.get(id);
		if (validator==null) {
			/*fails*/
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.ACCESS_FORBIDDEN_ELEMENT,xpath);
			context.addMessage(msg);
			return false;
		}
		boolean r = validator.validate(context, access);
		if (!r){
			ValidatorMessage msg = new ValidatorMessageImpl(ValidatorMessage.ERROR,id,ValidatorMessagesRes.ACCESS_FORBIDDEN_ELEMENT,xpath);
			context.addMessage(msg);
		}
		return r;
		
	}

	@Override
	public void registerRoleBasedValidator(String xpath, String... roles) {
		AccessValidator accessValidator = new RoleBasedValidator(this, roles);
		registerElementAccessValidator(xpath, accessValidator);
		
	}

	@Override
	public void registerRoleBasedAttributeValidator(String xpath, String attributeName,
			String... roles) {
		AccessValidator accessValidator = new RoleBasedValidator(this, roles);
		registerValueAccessValidator(xpath, attributeName,accessValidator);
	}

}

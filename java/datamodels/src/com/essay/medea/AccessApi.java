package com.essay.medea;

public interface AccessApi {
	public boolean validate(ValidatorContext context, Element element, SubjectAccess access, boolean recursive);
	public boolean validate(ValidatorContext context, String xpath, String attributeName, SubjectAccess access);
	public boolean validate(ValidatorContext context, String xpath, SubjectAccess access);
	/*register rules*/
	public void registerElementAccessValidator(String xpath, AccessValidator accessValidator);
	public void registerValueAccessValidator(String xpath, String attributeName, AccessValidator accessValidator);
	public void registerRoleBasedValidator(String xpath, String... roles);
	public void registerRoleBasedAttributeValidator(String xpath, String attributeName, String... roles);

}

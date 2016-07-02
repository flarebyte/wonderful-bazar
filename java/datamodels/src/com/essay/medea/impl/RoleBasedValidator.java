package com.essay.medea.impl;

import java.util.HashSet;
import java.util.Set;

import com.essay.medea.AccessApi;
import com.essay.medea.AccessValidator;
import com.essay.medea.SubjectAccess;
import com.essay.medea.ValidatorContext;

public class RoleBasedValidator implements AccessValidator {
	AccessApi accessApi;
	Set<String> roles=new HashSet<String>();
	
	
	public RoleBasedValidator(AccessApi accessApi, String... roles) {
		super();
		this.accessApi = accessApi;
		for (String role: roles){
			this.roles.add(role);
		}
		
	}

	@Override
	public AccessApi getAccessAPI() {
		return accessApi;
	}

	@Override
	public boolean validate(ValidatorContext context, SubjectAccess access) {
		/*Does it match any*/
		for (String role: roles){
			if(access.hasRole(role)) return true;
		}
		return false;
	}

}

package com.essay.medea.impl;

import java.util.HashSet;
import java.util.Set;

import com.essay.medea.SubjectAccess;

public class SubjectAccessImpl implements SubjectAccess{
	Set<String> roles=new HashSet<String>();
	
	public SubjectAccessImpl(String... roles) {
		super();
		for (String role: roles){
			this.roles.add(role);
		}
	}

	@Override
	public boolean hasRole(String role) {
		return roles.contains(role);
	}

}

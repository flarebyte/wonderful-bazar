package com.essay.medea;

/**
 * http://en.wikipedia.org/wiki/Role-based_access_control
 * http://en.wikipedia.org/wiki/Separation_of_duties
 * @author huino01
 *
 */
public interface SubjectAccess {
	public boolean hasRole(String role);
}

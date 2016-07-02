package com.flarebyte.cm.com.core.owls;

/**
 * The class ServiceProfile provides a superclass of every type of high-level
 * description of the service. ServiceProfile does not mandate any
 * representation of services, but it mandates the basic information to link any
 * instance of profile with an instance of service.There is a two-way relation
 * between a service and a profile, so that a service can be related to a
 * profile and a profile to a service.
 * 
 * @author olivier
 * 
 */
public interface ServiceProfile {

	/**
	 * Is the inverse of presents; it specifies that a given profile describes a
	 * service.
	 * 
	 * @return
	 */
	public Object getPresentedBy();

	/**
	 * Describes a relation between an instance of service and an instance of
	 * profile, it basically says that the service is described by the profile.
	 * 
	 * @return
	 */
	public Object getPresents();
}

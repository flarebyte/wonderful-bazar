package com.flarebyte.cm.com.core.owls;

/**
 * 
 * @author olivier
 * 
 */
public interface ServiceParameter {

	/**
	 * The service parameter name is the name of the actual parameter, which
	 * could be just a literal, or perhaps the URI of the process parameter (a
	 * property).
	 * 
	 * @return
	 */
	public Object getServiceParameterName();

	/**
	 * sParameter points to the value of the parameter within some OWL ontology.
	 * 
	 * @return
	 */
	public Object getSParameter();
}

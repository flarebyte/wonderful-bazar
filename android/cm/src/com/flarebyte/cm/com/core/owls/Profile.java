package com.flarebyte.cm.com.core.owls;

/**
 * An essential component of the profile is the specification of what
 * functionality the service provides and the specification of the conditions
 * that must be satisfied for a successful result. In addition, the profile
 * specifies what conditions result from the service, including the expected and
 * unexpected results of the service activity. The OWL-S Profile represents two
 * aspects of the functionality of the service: the information transformation
 * (represented by inputs and outputs) and the state change produced by the
 * execution of the service (represented by preconditions and effects).
 * 
 * @author olivier
 * 
 */
public interface Profile {

	/**
	 * Provides a mechanism of referring to humans or individuals responsible
	 * for the service (or some aspect of the service). The range of this
	 * property is unspecified within OWL-S, but can be restricted to some other
	 * ontology, such as FOAF, VCard, or the now depreciated Actor class
	 * provided in previous versions of OWL-S.
	 * 
	 * @return
	 */
	public Object getContactInformation();

	/**
	 * Ranges over instances of Inputs as defined in the Process Ontology.
	 * 
	 * @return
	 */
	public Object getHasInput();

	/**
	 * Ranges over instances of type Output, as defined in the Process ontology.
	 * 
	 * @return
	 */
	public Object getHasOutput();

	/**
	 * Ranges over a Parameter instance of the Process ontology. Note that the
	 * Parameter class models our intuition that Inputs and Outputs (which are
	 * kinds of Parameters) are both involved in information transformation and
	 * therefore they are different from Preconditions and Effects. As a
	 * consequence, we do not expect this class to be instantiated. It's role is
	 * solely making domain knowledge explicit.
	 * 
	 * @return
	 */
	public Object getHasParameter();

	/**
	 * Specifies one of the preconditions of the service and ranges over a
	 * Precondition instance defined according to the schema in the Process
	 * ontology.
	 * 
	 * @return
	 */
	public Object getHasPrecondition();

	/**
	 * Specifies one of the results of the service, as defined by the Result
	 * class in the Process ontology. It specifies under what conditions the
	 * outputs are generated. Furthermore, the Result specifies what domain
	 * changes are produced during the execution of the service.
	 * 
	 * @return
	 */
	public Object getHasResult();

	/**
	 * Defines a mapping from a Profile to an OWL ontology of services, such as
	 * an OWL specification of NAICS.
	 * 
	 * @return
	 */
	public Object getServiceClassification();

	/**
	 * Refers to the name of the service that is being offered. It can be used
	 * as an identifier of the service.
	 * 
	 * @return
	 */
	public Object getServiceName();

	/**
	 * Defines a mapping from a Profile to an OWL ontology of products, such as
	 * an OWL specification of UNSPSC.
	 * 
	 * @return
	 */
	public Object getServiceProduct();

	/**
	 * Provides a brief description of the service. It summarizes what the
	 * service offers, it describes what the service requires to work, and it
	 * indicates any additional information that the compiler of the profile
	 * wants to share with the receivers.
	 * 
	 * @return
	 */
	public Object getTextDescription();

}

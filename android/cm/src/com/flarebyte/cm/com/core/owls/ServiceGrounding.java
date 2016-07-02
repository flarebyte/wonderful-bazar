package com.flarebyte.cm.com.core.owls;

/**
 * The grounding of a service specifies the details of how to access the service
 * - details having mainly to do with protocol and message formats,
 * serialization, transport, and addressing. A grounding can be thought of as a
 * mapping from an abstract to a concrete specification of those service
 * description elements that are required for interacting with the service - in
 * particular, for our purposes, the inputs and outputs of atomic processes.
 * Note that in OWL-S, both the ServiceProfile and the ServiceModel are thought
 * of as abstract representations; only the ServiceGrounding deals with the
 * concrete level of specification.
 * 
 * @author olivier
 * 
 */
public interface ServiceGrounding {

}

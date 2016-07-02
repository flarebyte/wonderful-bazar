package com.flarebyte.cm.com.core.dc.vocabulary;

import java.net.URI;

import com.flarebyte.cm.com.core.Compilable;

/**
 * A term is a property (element), class, vocabulary encoding scheme, or syntax
 * encoding scheme.
 * 
 * @author olivier
 * 
 */
public interface Term extends Compilable {
	public Term[] getBroaderThanAsTermArray();

	/**
	 * A Class of which the described term is a Super-Class.
	 * 
	 * @return
	 */
	public URI[] getBroaderThanAsUriArray();

	/**
	 * Additional information about the term or its application.
	 * 
	 * @return
	 */
	public String getComment();

	/**
	 * A statement that represents the concept and essential nature of the term.
	 * 
	 * @return
	 */
	public String getDefinition();

	public Term[] getEquivalentPropertyAsTermArray();

	/**
	 * A Property to which the described term is equivalent.
	 * 
	 * @return
	 */
	public URI[] getEquivalentPropertyAsUriArray();

	/**
	 * A Class of which a resource described by the term is an Instance. Each
	 * property may be related to one or more classes by a has domain
	 * relationship. Where it is stated that a property has such a relationship
	 * with a class and the property is part of a property/value pair, it
	 * follows that the described resource is an instance of that class.
	 * 
	 * @return
	 */
	public Term[] getHasDomainAsTermArray();

	public URI[] getHasDomainAsUriArray();

	/**
	 * A Class of which a value described by the term is an Instance. Each
	 * property may be related to one or more classes by a has range
	 * relationship. Where it is stated that a property has such a relationship
	 * with a class and the property is part of a property/value pair, it
	 * follows that the value is an instance of that class.
	 * 
	 * @return
	 */
	public Term[] getHasRangeAsTermArray();

	public URI[] getHasRangeAsUriArray();

	/**
	 * A Class of which the described term is an instance.
	 * 
	 * @return
	 */
	public Term getInstanceOfAsTerm();

	public URI getInstanceOfAsUri();

	/**
	 * The human-readable label assigned to the term.
	 * 
	 * @return
	 */
	public String getLabel();

	/**
	 * An enumerated set of resources (Vocabulary Encoding Scheme) of which the
	 * term is a Member.
	 * 
	 * @return
	 */
	public Term getMemberOfAsTerm();

	public URI getMemberOfAsUri();

	/**
	 * A token appended to the URI of a DCMI namespace to create the URI of the
	 * term.
	 * 
	 * @return
	 */
	public String getName();

	/**
	 * A Class of which the described term is a Sub-Class.
	 * 
	 * @return
	 */
	public Term[] getNarrowerThanAsTermArray();

	public URI[] getNarrowerThanAsUriArray();

	/**
	 * A resource referenced in the Definition or Comment.
	 * 
	 * @return
	 */
	public String getReferences();

	/**
	 * A Property of which the described term is a Sub-Property.
	 * 
	 * @return
	 */
	public Term[] getRefinesAsTermArray();

	public URI[] getRefinesAsUriArray();

	/**
	 * Authoritative documentation related to the term.
	 * 
	 * @return
	 */
	public URI[] getSeeAsUriArray();

	/**
	 * The type of term as described in the DCMI Abstract Model [DCAM].
	 * 
	 * @return
	 */
	public URI getTypeOfTermAsUri();

	/**
	 * The Uniform Resource Identifier used to uniquely identify a term.
	 * 
	 * @return
	 */
	public String getUri();

	/**
	 * A specific historical description of a term.
	 * 
	 * @return
	 */
	public URI getVersionAsUri();

}

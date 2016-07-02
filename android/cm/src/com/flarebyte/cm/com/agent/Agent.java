package com.flarebyte.cm.com.agent;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * An agent (eg. person, group, software or physical artifact).
 * 
 * @author olivier
 * 
 */
public interface Agent extends Concept {
	public Address getAddress(Property property);

	public Address[] getAddressArray(Property property);

	public AgentIterator getAgentRelationships(Property property);

	public Company getAsCompany();

	public Group getAsGroup();

	public Organization getAsOrganization();

	public OrganizationUnit getAsOrganizationUnit();

	public Person getAsPerson();

	public CompanyIterator getCompanyRelationships(Property property);

	public GroupIterator getGroupRelationships(Property property);

	public OrganizationIterator getOrganizationRelationships(Property property);

	public OrganizationUnitIterator getOrganizationUnitRelationships(
			Property property);

	public PersonIterator getPersonRelationships(Property property);

}

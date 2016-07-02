package com.flarebyte.cm.com.agent;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * The Organization archetype represents an administrative and functional
 * structure.
 * 
 * @author olivier
 * 
 */
public interface Organization extends Agent {
	public OrganizationName getOrganizationName(Property property);

	public OrganizationName[] getOrganizationNameArray(Property property);

}

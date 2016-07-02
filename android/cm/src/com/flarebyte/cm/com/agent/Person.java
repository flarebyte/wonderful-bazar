package com.flarebyte.cm.com.agent;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * A Person represents people.
 * 
 * @author olivier
 * 
 */
public interface Person extends Agent {
	public IsoGender getIsoGender();

	public PersonName getPersonName(Property property);

	public PersonName[] getPersonNameArray(Property property);

}

package com.flarebyte.cm.com.core.dc;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;

/**
 * A record is some structured metadata about a resource, comprising one or more
 * properties and their associated values.
 * 
 * @author olivier
 * 
 */
public interface Record {
	public PropertyValueIterator getPropertyValues();

	public PropertyValueIterator getPropertyValues(Property property);

	public PropertyValueIterator getPropertyValues(Property property,
			Language language);

}

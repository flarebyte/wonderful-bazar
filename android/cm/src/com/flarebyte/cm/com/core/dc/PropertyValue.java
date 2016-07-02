package com.flarebyte.cm.com.core.dc;

import com.flarebyte.cm.com.core.dc.vocabulary.Property;
import com.flarebyte.cm.lang.Value;

/**
 * Each value is a literal string. Each value may have an associated encoding
 * scheme. Each literal string value may have an associated language (e.g.
 * en-GB).
 * 
 * @author olivier
 * 
 */
public interface PropertyValue extends Value {
	public EncodingScheme getEncodingScheme();

	public Language getLanguage();

	public Property getProperty();

}

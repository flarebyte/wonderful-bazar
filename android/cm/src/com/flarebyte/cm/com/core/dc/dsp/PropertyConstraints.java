package com.flarebyte.cm.com.core.dc.dsp;

import java.net.URI;

public interface PropertyConstraints {
	/**
	 * A set of properties that are allowed in this statement template.
	 * 
	 * @return
	 */
	public URI[] getProperty();

	/**
	 * Only sub-properties of the given property are allowed in this statement
	 * template. Note that the given property is included in this list (all
	 * properties are sub-properties of themselves).
	 * 
	 * @return
	 */
	public URI getSubPropertyOf();

}

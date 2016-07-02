package com.flarebyte.cm.com.core.dc.dsp;

import java.net.URI;

/**
 * Description template contains the statement templates that apply to a single
 * kind of description as well as constraints on the described resource.
 * 
 * @author olivier
 * 
 */
public interface DescriptionTemplate {
	public enum Standalone {
		YES, NO, BOTH;
	};

	/**
	 * A string that can be used in a Value Constraint to reference a
	 * description template that applies to the value resource.
	 * 
	 * @return
	 */
	public String getId();

	/**
	 * The maximum number of times this kind of description is allowed to appear
	 * in the Description Set.
	 * 
	 * @return
	 */
	public int getMaxOccurs();

	/**
	 * The minimum number of times this kind of description must appear in the
	 * Description Set.
	 * 
	 * @return
	 */
	public int getMinOccurs();

	/**
	 * Classes that the resource may be an instance of
	 * 
	 * @return
	 */
	public URI[] getResourceClassUri();

	/**
	 * Whether descriptions matching this template are allowed to occur
	 * standalone, i.e. without being the value of a property.
	 * 
	 * @return
	 */
	public Standalone getStandalone();

}

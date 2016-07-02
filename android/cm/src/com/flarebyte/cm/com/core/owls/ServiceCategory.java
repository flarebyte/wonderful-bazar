package com.flarebyte.cm.com.core.owls;

/**
 * ServiceCategory describes categories of services on the bases of some
 * classification that may be outside OWL-S and possibly outside OWL. In the
 * latter case, they may require some specialized reasoner if any inference has
 * to be done with it.
 * 
 * @author olivier
 * 
 */
public interface ServiceCategory {
	/**
	 * The category name is the name of the actual category, which could be just
	 * a literal, or perhaps the URI of the process parameter (a property).
	 * 
	 * @return
	 */
	public Object getCategoryName();

	/**
	 * To each type of service stores the code associated to a taxonomy.
	 * 
	 * @return
	 */
	public Object getCode();

	/**
	 * Stores a reference to the taxonomy scheme. It can be either a URI of the
	 * taxonomy, or a URL where the taxonomy resides, or the name of the
	 * taxonomy or anything else.
	 * 
	 * @return
	 */
	public Object getTaxonomy();

	/**
	 * Points to the value in a specific taxonomy There may be more than one
	 * value for each taxonomy, so no restriction is added here.
	 * 
	 * @return
	 */
	public Object getValue();

}

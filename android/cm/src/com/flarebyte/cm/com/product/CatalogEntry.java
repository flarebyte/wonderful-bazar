package com.flarebyte.cm.com.product;

import com.flarebyte.cm.com.core.Concept;

/**
 * A CatalogEntry represents information about a specific type of product held
 * in a ProductCatalog.
 * 
 * @author olivier
 * 
 */
public interface CatalogEntry extends Concept {
	public ProductCatalog getProductCatalog();

	public ProductType getProductType();
}

package com.flarebyte.cm.com.product;

import com.flarebyte.cm.lang.money.MoneyRange;

public interface ProductFinder {
	public ProductCatalogIterator findProductCatalogs(String... options);

	public ProductTypeIterator findProductTypes(ProductCatalog productCatalog,
			ProductFeatureType[] features, MoneyRange moneyRange,
			String... options);

	public ProductTypeIterator findProductTypes(ProductCatalog productCatalog,
			ProductFeatureType[] features, String... options);

	public ProductTypeIterator findProductTypes(ProductCatalog productCatalog,
			String... options);

}

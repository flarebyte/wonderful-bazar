package com.flarebyte.cm.com.core;

import com.flarebyte.cm.com.agent.AgentIterator;
import com.flarebyte.cm.com.product.Product;
import com.flarebyte.cm.com.product.ProductIterator;

public interface Space extends Concept {
	public ConceptIterator getConcepts(Filter filter);

	public DocumentIterator getDocuments(Filter filter);

	public AgentIterator getParties(Filter filter);

	public ProductIterator getProducts(Filter filter);

	public SectionIterator getSections(Filter filter);

	public void handleProduct(Product product, AgentIterator recipients,
			Filter filter);

	public void publishDocument(Document document, AgentIterator recipients,
			Filter filter);

	public void publishDocument(Document document, SectionIterator sections,
			Filter filter);

}

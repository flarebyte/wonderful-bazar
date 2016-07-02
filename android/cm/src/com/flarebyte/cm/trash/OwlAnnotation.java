package com.flarebyte.cm.trash;

import java.net.URI;

import com.flarebyte.storm.struct.SemanticLiteral;

public interface OwlAnnotation {
	enum TYPE {
		INDIVIDUAL, URI, LITERAL
	};

	public OwlIndividual getAsIndividual();

	public URI getAsUri();

	public SemanticLiteral getAsValue();

	public TYPE getTypeAsEnum();

}

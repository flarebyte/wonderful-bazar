package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlProperty extends OwlResource {
	public interface OwlAnnotationProperty extends OwlProperty {

	}

	public interface OwlOntologyProperty extends OwlProperty {

	}

	public SemanticId[] getEquivalentPropertyArray();

	public SemanticId[] getSubPropertyOfArray();

}

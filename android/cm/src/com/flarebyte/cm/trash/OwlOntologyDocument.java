package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlOntologyDocument {
	public OwlClass[] getClassArray();

	public OwlDatatypeProperty[] getDatatypePropertyArray();

	public SemanticId[] getImportArray();

	public OwlObjectProperty[] getObjectPropertyArray();

}

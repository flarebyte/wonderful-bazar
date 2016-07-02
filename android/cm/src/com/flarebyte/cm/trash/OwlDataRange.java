package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.SemanticLiteral;
import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlDataRange {
	enum ALTERNATIVE {
		DATATYPE_ID, LITERAL, ONE_OF_LITERAL
	};

	public SemanticId getDatatypeId();

	public SemanticLiteral getLiteral();

	public SemanticLiteral[] getLiteralArray();

}

package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.SemanticLiteral;

public interface OwlDatatype extends OwlResource {
	public enum ALTERNATIVE {
		DATATYPE, LITERAL, ENUMERATION
	};

	public ALTERNATIVE getAlternative();

	public Class<?> getDatatypeClass();

	public SemanticLiteral[] getEnumeration();

}

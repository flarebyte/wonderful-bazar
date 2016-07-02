package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlClassDescription {
	enum ALTERNATIVE {
		CLASS_ID, RESTRICTION, UNION, INTERSECTION, COMPLEMENT, ONE_OF
	};

	public ALTERNATIVE getAlternative();

	OwlClassDescription[] getClassDescriptionArray();

	public SemanticId getClassId();

	SemanticId[] getIndividualIdArray();

	public OwlRestriction getRestriction();

}

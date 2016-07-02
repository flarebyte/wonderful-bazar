package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.SemanticLiteral;
import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlRestriction {
	enum ALTERNATIVE {
		DATA, INDIVIDUAL
	};

	interface Cardinality {
		public int getEqual();

		public int getMax();

		public int getMin();
	}

	public interface DataRestrictionComponent {
		public OwlDataRange getAllOfDataRange();

		public Cardinality getCardinality();

		public SemanticLiteral getLiteral();

		public OwlDataRange getSomeOfDataRange();

	};

	public interface IndividualRestrictionComponent {

		public OwlClassDescription getAllOfClassDescription();

		public Cardinality getCardinality();

		public SemanticId getIndividualId();

		public OwlClassDescription getSomeOfClassDescription();

	}

	public ALTERNATIVE getAlternative();

	public DataRestrictionComponent[] getDataRestrictionArray();

	public IndividualRestrictionComponent[] getIndividualRestrictionArray();

	public SemanticId getPropertyId();
}

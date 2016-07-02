package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

public interface OwlObjectProperty extends OwlResource {

	public OwlClassDescription[] getDomainArray();

	public SemanticId[] getInverseOfArray();

	public OwlClassDescription[] getRangeArray();

	public boolean isFunctional();

	public boolean isInverseFunctional();

	public boolean isSymmetric();

	public boolean isTransitive();

}

package com.flarebyte.cm.trash;

public interface OwlDatatypeProperty extends OwlProperty {

	public OwlClassDescription[] getDomainArray();

	public OwlDataRange[] getRangeArray();

	public boolean isFunctional();

}

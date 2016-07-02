package com.flarebyte.cm.lang.quantity;

import com.flarebyte.cm.com.core.Concept;

public interface DerivedUnit extends Concept {
	String getSymbol();

	SystemOfUnits getSystemOfUnit();

	DerivedUnitTerm getUnitTerms();

}

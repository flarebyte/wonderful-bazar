package com.flarebyte.cm.lang.quantity;

import com.flarebyte.cm.com.core.Fragment;

public interface DerivedUnitTerm extends Fragment {
	Integer getPower();

	String getSymbol();

	SystemOfUnits getSystemOfUnit();

	ZUnit getUnit();
}

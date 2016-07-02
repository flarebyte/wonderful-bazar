package com.essay.medea.impl;

import com.essay.medea.Element;
import com.essay.medea.Factory;

public class FactoryImpl implements Factory {

	@Override
	public Element createRoot(String name) {
		Element r = new ElementImpl(name,null,false);
		return r;
	}
	
	public final static Factory create(){
		Factory r = new FactoryImpl();
		return r;
	}

}

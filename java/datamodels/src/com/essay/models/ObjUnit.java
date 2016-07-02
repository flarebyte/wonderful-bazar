package com.essay.models;

import java.util.EnumSet;
import java.util.HashMap;

public enum ObjUnit {
	MUST_HAVE ("must"),
	SHOULD_HAVE("should"),
	COULD_HAVE("could"),
	WONT_HAVE("wont");
	private static final HashMap<String,ObjUnit> lookup;
	   
	static {
		lookup=new HashMap<String,ObjUnit>();
		for(ObjUnit i : EnumSet.allOf(ObjUnit.class)){
            	lookup.put(i.name, i);
		}

	}
	
	private final String name;
	ObjUnit(String name) {
        this.name = name;
    }
	public static ObjUnit get(String name) { 
        return lookup.get(name); 
   }
}

package com.essay.models;

import java.util.EnumSet;
import java.util.HashMap;

public enum SectionType {
	SELECT ("select"),
	ORDER("order"),
	WRITE("could"),
	APPEND("wont");
	
	private static final HashMap<String,SectionType> lookup;
   
	static {
		lookup=new HashMap<String,SectionType>();
		for(SectionType i : EnumSet.allOf(SectionType.class)){
            	lookup.put(i.name, i);
		}

	}
	
	private final String name;
	SectionType(String name) {
        this.name = name;
    }
	public static SectionType get(String name) { 
        return lookup.get(name); 
   }

}

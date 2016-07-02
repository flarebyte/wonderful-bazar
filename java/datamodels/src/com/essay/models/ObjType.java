package com.essay.models;

import java.util.EnumSet;
import java.util.HashMap;

public enum ObjType {
	STRING ("must"),
	BOOLEAN("should"),
	INTEGER("should"),
	LONG("could"),
	FLOAT("wont"),
	DOUBLE("wont"),
	STRING_ARRAY ("must"),
	BOOLEAN_ARRAY("should"),
	INTEGER_ARRAY("should"),
	LONG_ARRAY("could"),
	FLOAT_ARRAY("wont"),
	DOUBLE_ARRAY("wont"),
	EMAIL("wont"),
	URL("wont"),
	MONEY("wont"),
	GEO_LAT_LON("wont"),
	GEOHASH("wont"),
	DATE("wont"),
	DATE_TIME("wont"),
	;
	private static final HashMap<String,ObjType> lookup;
	   
	static {
		lookup=new HashMap<String,ObjType>();
		for(ObjType i : EnumSet.allOf(ObjType.class)){
            	lookup.put(i.name, i);
		}

	}
	
	private final String name;
	ObjType(String name) {
        this.name = name;
    }
	public static ObjType get(String name) { 
        return lookup.get(name); 
   }

}

package com.essay.models;

import java.util.EnumSet;
import java.util.HashMap;

public enum GoalOperator {
	EQUAL ("equal"),
	NOT_EQUAL("not_equal"),
	GREATER_THAN("not_equal"),
	GREATER_THAN_OR_EQUAL("not_equal"),
	LESS_THAN("not_equal"),
	LESS_THAN_OR_EQUAL("not_equal"),
	BETWEEN("not_equal"),
	IN("not_equal"),
	;
	private static final HashMap<String,GoalOperator> lookup;
	   
	static {
		lookup=new HashMap<String,GoalOperator>();
		for(GoalOperator i : EnumSet.allOf(GoalOperator.class)){
            	lookup.put(i.name, i);
		}

	}
	
	private final String name;
	GoalOperator(String name) {
        this.name = name;
    }
	public static GoalOperator get(String name) { 
        return lookup.get(name); 
   }

}

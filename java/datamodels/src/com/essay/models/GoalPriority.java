package com.essay.models;

import java.util.EnumSet;
import java.util.HashMap;


/**
 * @see http://en.wikipedia.org/wiki/MoSCoW_Method
 * @author huino01
 *
 */
public enum GoalPriority {
	MUST_HAVE ("must"),
	SHOULD_HAVE("should"),
	COULD_HAVE("could"),
	WONT_HAVE("wont");
	
	private static final HashMap<String,GoalPriority> lookup;
   
	static {
		lookup=new HashMap<String,GoalPriority>();
		for(GoalPriority i : EnumSet.allOf(GoalPriority.class)){
            	lookup.put(i.name, i);
		}

	}
	
	private final String name;
	GoalPriority(String name) {
        this.name = name;
    }
	public static GoalPriority get(String name) { 
        return lookup.get(name); 
   }


}

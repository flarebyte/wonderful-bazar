/*
 * Created on Apr 15, 2005
 *
 */
package org.snowmongoose.generator.builder.interpreter.basic;

import java.util.HashMap;

import org.snowmongoose.generator.transformer.IStringTransformer;

/**
 * @author Oliver Huin
 *
 */
public class BasicInterpreterGrammar {

	private HashMap events = new HashMap();
	
	public void addEvent(String tag, BasicInterpreterTagType tagType, IStringTransformer transformer, String pairedTag){
		if (tag==null) throw new NullPointerException("tag cannot be null!");
		if (tagType==null) throw new NullPointerException("tagType cannot be null!");
		if (transformer==null) throw new NullPointerException("transformer cannot be null!");
		if (events.containsKey(tag)) throw new RuntimeException("This tag is already defined !"+tag);
		this.events.put(tag,new BasicInterpreterEvent(tag,tagType,transformer,pairedTag));
	}
	
	public BasicInterpreterEvent getEventForToken(String token){
		return (BasicInterpreterEvent) events.get(token);
	}
	
	
}

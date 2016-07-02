package com.essay.models;


public interface Goal extends Visitable{
	public String getSubject();
	public String getPredicate();
	public String getAlias();
	public GoalOperator getOperator();
	public ObjValue getObjValue();
	
	/**/
	
	
}

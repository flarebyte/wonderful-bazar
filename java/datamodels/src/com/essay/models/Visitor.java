package com.essay.models;

public interface Visitor {
	public Object visit(Script script);
	public Object visit(Block block);
	public Object visit(Goal goal);
}

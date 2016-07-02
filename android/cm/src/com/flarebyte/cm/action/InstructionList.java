package com.flarebyte.cm.action;

public interface InstructionList<A, I> extends TimeAware, Scriptable {
	public void add(DataInstruction<A, I> args);

	public void clear();

	public String[] getOptions();

	public int size();

}

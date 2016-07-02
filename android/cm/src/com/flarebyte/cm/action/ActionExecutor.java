package com.flarebyte.cm.action;

public interface ActionExecutor<A, I> extends Action<A, I> {
	public boolean cancel(InstructionList<A, I> args);

	public void clear();

	public boolean execute(InstructionList<A, I> args);

	public int size();

}

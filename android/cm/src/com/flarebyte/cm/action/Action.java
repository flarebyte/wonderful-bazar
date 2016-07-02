package com.flarebyte.cm.action;

import android.graphics.Bitmap;

import com.flarebyte.cm.lang.Node;

/**
 * Stateless
 * 
 * @author olivier
 * 
 * @param <E>
 */
public interface Action<A, I> {

	public boolean cancel(DataInstruction<A, I> args);

	public Object execute(DataInstruction<A, I> args);

	public Bitmap executeAsBitmap(DataInstruction<A, I> args);

	public Node executeAsNode(DataInstruction<A, I> args);

}

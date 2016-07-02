package com.flarebyte.cm.action;

import android.graphics.Bitmap;

import com.flarebyte.cm.lang.Node;

/**
 * Ex: localId = action(id1,id2,node1,options)
 * 
 * @author flarebyte.com - Olivier Huin
 * 
 * @param <A>
 * @param <I>
 */
public interface DataInstruction<A, I> extends TimeAware, SizeAware, Scriptable {
	public Object get(int index);

	public A getAction();

	public ActionExecutor<A, I> getActionExecutor();

	public Bitmap getAsBitmap(final int index);

	public I getAsId(final int index);

	public Node getAsNode(final int index);

	public String getAsString(final int index);

	public I getLocalId();

	public String[] getOptions();

	@SuppressWarnings("rawtypes")
	public Class getParamClass(int index);

	public int size();

}

/**
 * 
 */
package com.flarebyte.cm.action.core;

import android.graphics.Bitmap;

import com.flarebyte.cm.action.Action;
import com.flarebyte.cm.action.DataInstruction;
import com.flarebyte.cm.lang.Node;

/**
 * @author olivier
 * 
 */
public class DownloadBitmap implements Action<CoreActions, String> {

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * com.flarebyte.cm.action.Action#cancel(com.flarebyte.cm.action.DataInstruction
	 * )
	 */
	@Override
	public boolean cancel(final DataInstruction<CoreActions, String> args) {
		return false;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see com.flarebyte.cm.action.Action#execute(com.flarebyte.cm.action.
	 * DataInstruction)
	 */
	@Override
	public Object execute(final DataInstruction<CoreActions, String> args) {
		return executeAsBitmap(args);
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * com.flarebyte.cm.action.Action#executeAsBitmap(com.flarebyte.cm.action
	 * .DataInstruction)
	 */
	@Override
	public Bitmap executeAsBitmap(
			final DataInstruction<CoreActions, String> args) {
		// TODO Auto-generated method stub
		return null;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * com.flarebyte.cm.action.Action#executeAsNode(com.flarebyte.cm.action.
	 * DataInstruction)
	 */
	@Override
	public Node executeAsNode(final DataInstruction<CoreActions, String> args) {
		return null;
	}

}

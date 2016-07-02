package com.flarebyte.azalea.engine.render;

import android.content.Context;
import android.os.Handler;
import android.os.Message;
import android.util.AttributeSet;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.widget.TextView;

public abstract class GameSurfaceView extends SurfaceView implements
		SurfaceHolder.Callback {
	/** Handle to the application context, used to e.g. fetch Drawables. */
	private Context mContext;

	/** Pointer to the text view to display "Paused.." etc. */
	private TextView mStatusText;

	/** The thread that actually draws the animation */
	public GameThread thread;

	public GameSurfaceView(Context context, AttributeSet attrs) {
		super(context, attrs);
		setFocusable(true); // make sure we get key events
	}

	public void surfaceChanged(SurfaceHolder holder, int format, int width,
			int height) {
		// TODO Auto-generated method stub

	}

	@Override
	public void surfaceCreated(SurfaceHolder holder) {
		thread.running = true;
		thread.start();

	}

	@Override
	public void surfaceDestroyed(SurfaceHolder arg0) {
		boolean retry = true;
		thread.running = false;
		while (retry) {
			try {
				thread.join();
				retry = false;
			} catch (InterruptedException e) {
			}
		}
	}

}

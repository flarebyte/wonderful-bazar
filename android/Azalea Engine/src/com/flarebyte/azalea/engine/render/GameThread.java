package com.flarebyte.azalea.engine.render;

import android.content.Context;
import android.graphics.Canvas;
import android.os.Handler;
import android.view.SurfaceHolder;

public class GameThread extends Thread {
    /** Handle to the surface manager object we interact with */
    private SurfaceHolder mSurfaceHolder;
    /** Message handler used by thread to interact with TextView */
    private Handler mHandler;
    /** Indicate whether the surface has been created & is ready to draw */
    protected boolean running = false;

    public GameThread(SurfaceHolder surfaceHolder, Context context,
	    Handler handler) {
	// get handles to some important objects
	mSurfaceHolder = surfaceHolder;
	mHandler = handler;
	// mContext = context;

	// Resources res = context.getResources();
    }

    @Override
    public void run() {
	while (running) {
	    Canvas canvas = null;
	    try {
		canvas = mSurfaceHolder.lockCanvas(null);
		synchronized (mSurfaceHolder) {
		    RenderingContext renderingContext = RenderingContext
			    .create();
		    TangoPalette.createPalette(renderingContext);

		    FrameInstructionSet instructionSet = PerformanceInstructionSet
			    .createAlpha(renderingContext);
		    CanvasRenderer.render(instructionSet, canvas,
			    renderingContext);
		}
	    } finally {
		if (canvas != null) {
		    mSurfaceHolder.unlockCanvasAndPost(canvas);
		}
	    }
	}
    }

}

package com.flarebyte.azalea.engine.render;

import android.graphics.Paint;
import android.graphics.Path;

public class RenderingContext {

    public final static byte SMALL = 1;
    public final static byte MEDIUM = 2;
    public final static byte LARGE = 3;

    public byte granularity = SMALL;
    public Paint[] paintPalette;

    public int illustrationsByAnimated = 10;
    public int stepsByScene = 7;
    public int rulesByEvent = 10;
    public int illustrationsByScene = 40;
    public int animationsByScene = 40;
    public int instructionsByIllustration = 100;
    public int instructionsByFrame = 500;

    public Path createPath() {
	return new Path();
    }

    public Paint[] createPaintArray(final int size) {
	Paint[] r = new Paint[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = new Paint();
	}
	return r;
    }

    public final static RenderingContext create() {
	RenderingContext r = new RenderingContext();
	return r;
    }
}

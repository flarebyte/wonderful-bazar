package com.flarebyte.azalea.engine.scene;

import com.flarebyte.azalea.engine.render.RenderingContext;

public class Animated {
    public Illustration illustrations[];

    public void init(RenderingContext renderingContext) {
	illustrations = Illustration.createArray(renderingContext,
		renderingContext.illustrationsByAnimated);
    }

    public void reset(RenderingContext renderingContext) {
	Illustration.reset(renderingContext, illustrations);
    }

    public final static Animated create(RenderingContext renderingContext) {
	Animated r = new Animated();
	r.init(renderingContext);
	return r;
    }

    public final static Animated[] createArray(
	    RenderingContext renderingContext, int size) {
	Animated[] r = new Animated[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = Animated.create(renderingContext);
	}
	return r;
    }

    public final static void reset(RenderingContext renderingContext,
	    Animated[] anims) {
	for (Animated animated : anims) {

	    animated.reset(renderingContext);
	}
    }

}

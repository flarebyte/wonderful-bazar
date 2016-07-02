package com.flarebyte.azalea.engine.scene;

import com.flarebyte.azalea.engine.render.RenderingContext;

public class Scene {
    public int id;
    public StepDescription[] steps;
    public Illustration[] illustrations;
    public Animated[] animations;

    public void init(RenderingContext renderingContext) {
	id = -1;
	steps = StepDescription.createArray(renderingContext,
		renderingContext.stepsByScene);
	illustrations = Illustration.createArray(renderingContext,
		renderingContext.illustrationsByScene);
	animations = Animated.createArray(renderingContext,
		renderingContext.animationsByScene);
    }

    public void reset(RenderingContext renderingContext) {
	id = -1;
	StepDescription.reset(renderingContext, steps);
	Illustration.reset(renderingContext, illustrations);
	Animated.reset(renderingContext, animations);

    }

    public final static Scene create(RenderingContext renderingContext) {
	Scene r = new Scene();
	r.init(renderingContext);
	return r;

    }

    public final static Scene[] createArray(RenderingContext renderingContext,
	    int size) {
	Scene[] r = new Scene[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = Scene.create(renderingContext);
	}
	return r;

    }

    public final static void reset(RenderingContext renderingContext,
	    Scene[] scenes) {

	for (Scene scene : scenes) {
	    scene.reset(renderingContext);
	}
    }

}

package com.flarebyte.azalea.engine.scene;

import com.flarebyte.azalea.engine.render.RenderingContext;

public class Illustration {
    public int id;
    public IllustrationInstructionSet instructionSet;

    public void init(RenderingContext renderingContext) {
	id = -1;
	instructionSet = IllustrationInstructionSet.create(renderingContext);
    }

    public void reset(RenderingContext renderingContext) {
	this.id = -1;
	instructionSet.reset(renderingContext);

    }

    public final static Illustration create(RenderingContext renderingContext) {
	Illustration r = new Illustration();
	r.init(renderingContext);
	return r;
    }

    public final static Illustration[] createArray(
	    RenderingContext renderingContext, int size) {
	Illustration[] r = new Illustration[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = Illustration.create(renderingContext);
	}
	return r;
    }

    public final static void reset(RenderingContext renderingContext,
	    Illustration[] illustrations) {
	for (Illustration illustration : illustrations) {
	    illustration.reset(renderingContext);
	}
    }

}

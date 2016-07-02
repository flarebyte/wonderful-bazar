package com.flarebyte.azalea.engine.scene;

import com.flarebyte.azalea.engine.render.PathInstruction;
import com.flarebyte.azalea.engine.render.RenderingContext;

public class IllustrationInstructionSet {
    public PathInstruction[] pathInstructions;

    public void init(RenderingContext renderingContext) {
	pathInstructions = PathInstruction
		.createArray(renderingContext.instructionsByFrame);
    }

    public void reset(RenderingContext renderingContext) {
	PathInstruction.reset(pathInstructions);
    }

    public final static IllustrationInstructionSet create(
	    RenderingContext renderingContext) {
	IllustrationInstructionSet r = new IllustrationInstructionSet();
	r.init(renderingContext);
	return r;
    }

}

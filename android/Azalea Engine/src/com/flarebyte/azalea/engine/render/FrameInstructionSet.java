package com.flarebyte.azalea.engine.render;

import com.flarebyte.azalea.engine.scene.IllustrationInstructionSet;

public class FrameInstructionSet {
    public PathInstruction[] pathInstructions;
    public int pathCount = 0;

    public void init(RenderingContext renderingContext) {
	pathInstructions = PathInstruction
		.createArray(renderingContext.instructionsByIllustration);
    }

    public void reset(RenderingContext renderingContext) {
	pathCount = 0;
	PathInstruction.reset(pathInstructions);
    }

    public final static FrameInstructionSet create(
	    RenderingContext renderingContext) {
	FrameInstructionSet r = new FrameInstructionSet();
	r.init(renderingContext);
	return r;
    }

    public void add(IllustrationInstructionSet instructionSet) {
	PathInstruction[] set = instructionSet.pathInstructions;
	byte instr = set[0].instruction;
	int i = 0;
	while (instr != PathInstruction.STOP) {
	    this.pathInstructions[++pathCount] = set[i++];
	}// end while
    }

    public void stopPath() {
	this.pathInstructions[++pathCount].stop();
    }
}

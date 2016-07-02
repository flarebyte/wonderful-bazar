package com.flarebyte.azalea.engine.render;

import com.flarebyte.azalea.engine.scene.IllustrationInstructionSet;

public class PerformanceInstructionSet {
    public final static FrameInstructionSet createAlpha(
	    RenderingContext renderingContext) {
	FrameInstructionSet r = FrameInstructionSet.create(renderingContext);
	r.add(createBravo(renderingContext));
	return r;
    }

    public final static IllustrationInstructionSet createBravo(
	    RenderingContext renderingContext) {
	IllustrationInstructionSet r = IllustrationInstructionSet
		.create(renderingContext);
	PathInstruction[] p = r.pathInstructions;
	int i = 0;
	p[i++].newPath();
	p[i++].moveTo(0, 100);
	p[i++].relLineTo(0, 50);
	p[i++].draw(TangoPalette.SCARLET_RED1);

	return r;
    }

}

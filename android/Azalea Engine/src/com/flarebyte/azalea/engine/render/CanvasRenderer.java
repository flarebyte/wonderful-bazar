package com.flarebyte.azalea.engine.render;

import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Path;

public class CanvasRenderer {
    public static void render(FrameInstructionSet instructionSet,
	    Canvas canvas, RenderingContext renderingContext) {
	renderPathInstructions(instructionSet.pathInstructions, canvas,
		renderingContext);

    }

    public static void renderPathInstructions(
	    PathInstruction[] pathInstructions, Canvas canvas,
	    RenderingContext renderingContext) {
	int cursor = 0;
	boolean continueLoop = true;
	Path path = renderingContext.createPath();
	Paint paint = renderingContext.paintPalette[TangoPalette.ALUMINIUM1];
	PathInstruction pathInstruction = null;
	PathInstruction next = null;
	PathInstruction next2 = null;
	while (continueLoop) {
	    pathInstruction = pathInstructions[cursor];
	    switch (pathInstruction.instruction) {
	    case PathInstruction.NEW_PATH:
		path.reset();
		break;
	    case PathInstruction.DRAW:
		paint = renderingContext.paintPalette[pathInstruction.ref];
		canvas.drawPath(path, paint);
		break;
	    case PathInstruction.STOP:
		continueLoop = false;
		break;
	    case PathInstruction.LINE_TO:
		path.lineTo(pathInstruction.x, pathInstruction.y);
		break;
	    case PathInstruction.MOVE_TO:
		path.moveTo(pathInstruction.x, pathInstruction.y);
		break;
	    case PathInstruction.REL_LINE_TO:
		path.rLineTo(pathInstruction.x, pathInstruction.y);
		break;
	    case PathInstruction.REL_MOVE_TO:
		path.rMoveTo(pathInstruction.x, pathInstruction.y);
		break;
	    case PathInstruction.OFFSET:
		path.offset(pathInstruction.x, pathInstruction.y);
		break;
	    case PathInstruction.QUAD_TO_1:
		next = pathInstructions[++cursor];
		if (next.instruction != PathInstruction.QUAD_TO_2)
		    throw new RuntimeException("Expected QUAD_TO_2 !");
		path.quadTo(pathInstruction.x, pathInstruction.y, next.x,
			next.y);
		break;
	    case PathInstruction.REL_QUAD_TO_1:
		next = pathInstructions[++cursor];
		if (next.instruction != PathInstruction.REL_QUAD_TO_2)
		    throw new RuntimeException("Expected REL_QUAD_TO_2 !");
		path.rQuadTo(pathInstruction.x, pathInstruction.y, next.x,
			next.y);
		break;
	    case PathInstruction.CUBIC_TO_1:
		next = pathInstructions[++cursor];
		next2 = pathInstructions[++cursor];
		if (next.instruction != PathInstruction.CUBIC_TO_2)
		    throw new RuntimeException("Expected CUBIC_TO_2 !");
		if (next2.instruction != PathInstruction.CUBIC_TO_3)
		    throw new RuntimeException("Expected CUBIC_TO_3 !");
		path.cubicTo(pathInstruction.x, pathInstruction.y, next.x,
			next.y, next2.x, next2.y);
		break;
	    }
	    cursor++;
	}
	canvas.drawPath(path, paint);
    }

}

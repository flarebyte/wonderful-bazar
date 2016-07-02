package com.flarebyte.azalea.engine.render;

public class PathInstruction {
    public final static byte DRAW = -2;
    public final static byte STOP = -1;
    public final static byte NEW_PATH = 1;
    public final static byte OFFSET = 2;
    public final static byte LINE_TO = 3;
    public final static byte MOVE_TO = 4;
    public final static byte QUAD_TO_1 = 5;
    public final static byte QUAD_TO_2 = 6;
    public final static byte CUBIC_TO_1 = 7;
    public final static byte CUBIC_TO_2 = 8;
    public final static byte CUBIC_TO_3 = 8;
    public final static byte REL_LINE_TO = 9;
    public final static byte REL_MOVE_TO = 10;
    public final static byte REL_QUAD_TO_1 = 11;
    public final static byte REL_QUAD_TO_2 = 12;
    public final static byte REL_CUBIC_TO_1 = 13;
    public final static byte REL_CUBIC_TO_2 = 14;
    public final static byte REL_CUBIC_TO_3 = 15;

    public byte instruction;
    public float x;
    public float y;
    public int ref;

    public void reset() {
	instruction = STOP;
	x = 0;
	y = 0;
	ref = 0;
    }

    public final static PathInstruction create() {
	PathInstruction r = new PathInstruction();
	r.reset();
	return r;
    }

    public final static PathInstruction[] createArray(int size) {
	PathInstruction[] r = new PathInstruction[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = PathInstruction.create();
	}
	return r;
    }

    public final static void reset(PathInstruction[] instructions) {
	for (PathInstruction instruction : instructions) {
	    instruction.reset();
	}
    }

    public void draw(int reference) {
	instruction = DRAW;
	x = 0;
	y = 0;
	ref = reference;
    }

    public void stop() {
	instruction = STOP;
	x = 0;
	y = 0;
	ref = 0;
    }

    public void newPath() {
	instruction = NEW_PATH;
	x = 0;
	y = 0;
	ref = 0;
    }

    public void offset(int x, int y) {
	instruction = OFFSET;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void lineTo(int x, int y) {
	instruction = LINE_TO;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void moveTo(int x, int y) {
	instruction = MOVE_TO;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void quadTo1(int x, int y) {
	instruction = QUAD_TO_1;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void quadTo2(int x, int y) {
	instruction = QUAD_TO_2;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void cubicTo1(int x, int y) {
	instruction = CUBIC_TO_1;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void cubicTo2(int x, int y) {
	instruction = CUBIC_TO_2;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void cubicTo3(int x, int y) {
	instruction = CUBIC_TO_3;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    // Relatives

    public void relLineTo(int x, int y) {
	instruction = REL_LINE_TO;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relMoveTo(int x, int y) {
	instruction = REL_MOVE_TO;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relQuadTo1(int x, int y) {
	instruction = REL_QUAD_TO_1;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relQuadTo2(int x, int y) {
	instruction = REL_QUAD_TO_2;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relCubicTo1(int x, int y) {
	instruction = REL_CUBIC_TO_1;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relCubicTo2(int x, int y) {
	instruction = REL_CUBIC_TO_2;
	this.x = x;
	this.y = y;
	ref = 0;
    }

    public void relCubicTo3(int x, int y) {
	instruction = REL_CUBIC_TO_3;
	this.x = x;
	this.y = y;
	ref = 0;
    }

}

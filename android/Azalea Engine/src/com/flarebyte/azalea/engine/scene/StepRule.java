package com.flarebyte.azalea.engine.scene;

public class StepRule {

	public void init() {

	}

	public StepRule() {
		super();
		init();
	}

	public final static StepRule[] createArray(final int size) {
		StepRule[] r = new StepRule[size];
		for (int i = size - 1; i >= 0; i--) {
			r[i] = new StepRule();
		}
		return r;
	}

	public void reset() {

	}

	public final static void reset(StepRule[] rules) {
		for (StepRule rule : rules) {
			rule.reset();
		}

	}

}

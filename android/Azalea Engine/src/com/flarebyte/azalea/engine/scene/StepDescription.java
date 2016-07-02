package com.flarebyte.azalea.engine.scene;

import com.flarebyte.azalea.engine.render.RenderingContext;

public class StepDescription {
    public int id;
    public StepRule[] onStart;
    public StepRule[] onFinish;
    public StepRule[] onTouch;
    public StepRule[] onNotTouch;
    public StepRule[] onTouchA;
    public StepRule[] onTouchB;
    public StepRule[] onTouchC;
    public StepRule[] onTouchD;
    public StepRule[] onTouchAx;
    public StepRule[] onTouchBx;
    public StepRule[] onTouchCx;
    public StepRule[] onTouchDx;
    public StepRule[] onNotTouchA;
    public StepRule[] onNotTouchB;
    public StepRule[] onNotTouchC;
    public StepRule[] onNotTouchD;
    public StepRule[] onNotTouchAx;
    public StepRule[] onNotTouchBx;
    public StepRule[] onNotTouchCx;
    public StepRule[] onNotTouchDx;

    public void init(RenderingContext renderingContext) {
	id = -1;
	onStart = StepRule.createArray(renderingContext.rulesByEvent);
	onFinish = StepRule.createArray(renderingContext.rulesByEvent);
	onTouch = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouch = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchA = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchB = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchC = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchD = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchAx = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchBx = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchCx = StepRule.createArray(renderingContext.rulesByEvent);
	onTouchDx = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchA = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchB = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchC = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchD = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchAx = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchBx = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchCx = StepRule.createArray(renderingContext.rulesByEvent);
	onNotTouchDx = StepRule.createArray(renderingContext.rulesByEvent);
    }

    public void reset(RenderingContext renderingContext) {
	StepRule.reset(onStart);
	StepRule.reset(onFinish);
	StepRule.reset(onTouch);
	StepRule.reset(onNotTouch);
	StepRule.reset(onTouchA);
	StepRule.reset(onTouchB);
	StepRule.reset(onTouchC);
	StepRule.reset(onTouchD);
	StepRule.reset(onTouchAx);
	StepRule.reset(onTouchBx);
	StepRule.reset(onTouchCx);
	StepRule.reset(onTouchDx);
	StepRule.reset(onNotTouchA);
	StepRule.reset(onNotTouchB);
	StepRule.reset(onNotTouchC);
	StepRule.reset(onNotTouchD);
	StepRule.reset(onNotTouchAx);
	StepRule.reset(onNotTouchBx);
	StepRule.reset(onNotTouchCx);
	StepRule.reset(onNotTouchDx);
    }

    public final static StepDescription create(RenderingContext renderingContext) {
	StepDescription r = new StepDescription();
	r.init(renderingContext);
	return r;
    }

    public final static StepDescription[] createArray(
	    RenderingContext renderingContext, int size) {
	StepDescription[] r = new StepDescription[size];
	for (int i = size - 1; i >= 0; i--) {
	    r[i] = StepDescription.create(renderingContext);
	}
	return r;
    }

    public final static void reset(RenderingContext renderingContext,
	    StepDescription[] steps) {
	for (StepDescription step : steps) {
	    step.reset(renderingContext);
	}
    }
}

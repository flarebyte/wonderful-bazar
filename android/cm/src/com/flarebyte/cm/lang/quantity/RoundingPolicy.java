package com.flarebyte.cm.lang.quantity;

public interface RoundingPolicy {
	public int getNumberOfDigits();

	public int getRoundingDigit();

	public int getRoundingStep();

}

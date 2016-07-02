package com.flarebyte.cm.lang.quantity;

public interface Quantity {
	public Quantity add(Quantity... quantity);

	public Float getAmountAsFloat();

	public Metric getMetric();

	public Quantity multiply(float m);

	public Quantity multiply(int m);

	public Quantity round(RoundingPolicy roundingPolicy);

	public Quantity substract(Quantity quantity);

}

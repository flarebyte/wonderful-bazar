/*
 * Created on Jul 11, 2005
 *
  */
package org.snowmongoose.pov3d;



/**
 * @author Oliver Huin
 *
 */
public class PercentageNumber extends Number {

	double value;
	/* (non-Javadoc)
	 * @see java.lang.Number#doubleValue()
	 */
	public double doubleValue() {
		return value;
	}

	/* (non-Javadoc)
	 * @see java.lang.Number#floatValue()
	 */
	public float floatValue() {
		return (float) value;
	}

	/* (non-Javadoc)
	 * @see java.lang.Number#intValue()
	 */
	public int intValue() {
		return (int) value;
	}

	/* (non-Javadoc)
	 * @see java.lang.Number#longValue()
	 */
	public long longValue() {
		return (long) value;
	}
	
	public final int MIN_VALUE=0;
	public final int MAX_VALUE=1;
	

	/**
	 * @param value
	 */
	public PercentageNumber(double value) {
		super();
		if (value<MIN_VALUE) throw new NumberFormatException(value+" is out of range !");
		if (value>MAX_VALUE) throw new NumberFormatException(value+" is out of range !");
		this.value = value;
	}
}

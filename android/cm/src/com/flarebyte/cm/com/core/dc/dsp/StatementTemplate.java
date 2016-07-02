package com.flarebyte.cm.com.core.dc.dsp;

public interface StatementTemplate {

	enum Type {
		LITERAL, NON_LITERAL, BOTH
	}

	/**
	 * The maximum number of times this kind of statement is allowed to appear
	 * in the enclosing Description.
	 * 
	 * @return
	 */
	public int getMaxOccurs();

	/**
	 * The minimum number of times this kind of statement must appear in the
	 * enclosing Description.
	 * 
	 * @return
	 */
	public int getMinOccurs();

	/**
	 * 
	 * @return
	 */
	public PropertyConstraintsIterator getPropertyConstraints();

	/**
	 * The type of value surrogate (literal/non-literal) that is allowed in this
	 * Statement.
	 * 
	 * @return
	 */
	public Type getType();

}

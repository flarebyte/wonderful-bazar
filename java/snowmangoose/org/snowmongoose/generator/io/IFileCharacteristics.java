/*
 * Created on May 3, 2005
 *
 */
package org.snowmongoose.generator.io;

import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.CharsetEncoder;

/**
 * @author Oliver Huin
 *
 */
public interface IFileCharacteristics {

	/**
	 * @return Returns the encoderName.
	 */
	public abstract String getEncoderName();

	/**
	 * @return Returns the endOfLine.
	 */
	public abstract String getEndOfLine();

	/**
	 * @return Returns the charset.
	 */
	public abstract Charset getCharset();

	/**
	 * @return Returns the charsetDecoder.
	 */
	public abstract CharsetDecoder getCharsetDecoder();

	/**
	 * @return Returns the charsetEncoder.
	 */
	public abstract CharsetEncoder getCharsetEncoder();
}
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
public class FileCharacteristics implements IFileCharacteristics {
	private String encoderName;

	private String endOfLine;

	private CharsetEncoder charsetEncoder;

	private CharsetDecoder charsetDecoder;

	Charset charset;

	/**
	 * @param encoderName
	 * @param endOfLine
	 * @param append
	 */
	public FileCharacteristics(String encoderName, String endOfLine) {
		super();
		this.encoderName = encoderName;
		this.endOfLine = endOfLine;
		this.charset = Charset.forName(encoderName);
		this.charsetDecoder = this.charset.newDecoder();
		this.charsetEncoder = this.charset.newEncoder();

	}

	/**
	 * @return Returns the encoderName.
	 */
	public String getEncoderName() {
		return encoderName;
	}

	/**
	 * @return Returns the endOfLine.
	 */
	public String getEndOfLine() {
		return endOfLine;
	}

	/**
	 * @return Returns the charset.
	 */
	public Charset getCharset() {
		return charset;
	}

	/**
	 * @return Returns the charsetDecoder.
	 */
	public CharsetDecoder getCharsetDecoder() {
		return charsetDecoder;
	}

	/**
	 * @return Returns the charsetEncoder.
	 */
	public CharsetEncoder getCharsetEncoder() {
		return charsetEncoder;
	}
}
/*
 * Created on May 5, 2005
 *
 */
package org.snowmongoose.generator.io;

/**
 * @author Oliver Huin
 *  
 */
public class FileCharacteristicsFactory {

	public static IFileCharacteristics createWindowsUTF8() {
		return new FileCharacteristics("UTF-8", "\r\n");
	}

	public static IFileCharacteristics createMacOsUTF8() {
		return new FileCharacteristics("UTF-8", "\r");
	}

	public static IFileCharacteristics createUnixUTF8() {
		return new FileCharacteristics("UTF-8", "\n");
	}
}
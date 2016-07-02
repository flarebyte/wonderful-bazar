/*
 * Created on May 3, 2005
 *
 */
package test.org.snowmongoose.generator.io;

import java.io.File;
import java.io.IOException;

import org.snowmongoose.generator.StringTransformerFactory;
import org.snowmongoose.generator.io.FileCharacteristicsFactory;
import org.snowmongoose.generator.io.FileUtils;

import junit.framework.TestCase;

/**
 * @author Oliver Huin
 *
 */
public class FileUtilsReadTest extends TestCase {
	public void testReadFileAsString() {
		try {
			String r = FileUtils.readFileAsString(new File("testwrite.txt"),FileCharacteristicsFactory.createWindowsUTF8());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void testReadFileAsStringArray() {
		try {
			String r = FileUtils.readFileAsStringArray(new File("testwrite.txt"),FileCharacteristicsFactory.createWindowsUTF8())[0];
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void testCopyFile() {
		try {
			FileUtils.copyFile(new File("testwriteWithArray.txt"),FileCharacteristicsFactory.createWindowsUTF8(), new File("testwriteWithArray2.txt"),FileCharacteristicsFactory.createWindowsUTF8(),StringTransformerFactory.upperCaseTransformer(),false);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}

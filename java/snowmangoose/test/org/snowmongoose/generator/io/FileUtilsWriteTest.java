/*
 * Created on May 3, 2005
 *
 */
package test.org.snowmongoose.generator.io;

import java.io.File;
import java.io.IOException;

import org.snowmongoose.generator.io.FileCharacteristicsFactory;
import org.snowmongoose.generator.io.FileUtils;

import junit.framework.TestCase;

/**
 * @author Oliver Huin
 *
 */
public class FileUtilsWriteTest extends TestCase {
	String[] data1 = {"line1=data1","line2=data2","line3=data3"};
	public void testWriteFile() {
		try {
			FileUtils.writeFile(new File("testwrite.txt"),FileCharacteristicsFactory.createWindowsUTF8(),"line1 \n line2",false);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void testWriteFileWithArray() {
		try {
			FileUtils.writeFile(new File("testwriteWithArray.txt"),FileCharacteristicsFactory.createWindowsUTF8(),data1,false);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

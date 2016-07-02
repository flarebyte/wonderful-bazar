import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;

import junit.framework.TestCase;
/*
 * Created on Dec 22, 2004
 *
 * TODO To change the template for this generated file go to
 * Window - Preferences - Java - Code Style - Code Templates
 */

/**
 * @author Oliver Huin
 *
 * TODO To change the template for this generated type comment go to
 * Window - Preferences - Java - Code Style - Code Templates
 */
public class ReadExcelFile extends TestCase {
	public void test() {
		POIFSFileSystem fs=null;
		HSSFWorkbook wb=null;
		PrintWriter writer= null; 
		try {
			fs = new POIFSFileSystem(new FileInputStream("c:/temp/input.xls"));
			wb = new HSSFWorkbook(fs);
			HSSFSheet sheet = wb.getSheetAt(0);
		    writer = new PrintWriter(new OutputStreamWriter(new FileOutputStream(
		    		"c:/temp/output.csv")));
		    for (int i=1;i<100;i++){
		        System.out.println(i);
		    	HSSFRow row = sheet.getRow(i);
		        HSSFCell cell = row.getCell((short)1);
		        writer.write(cell.getStringCellValue());
		        writer.flush();
		    }
		    writer.close();
		    
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


	}
}

/*
 * Created on Apr 28, 2005
 *
 */
package org.snowmongoose.generator.io;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.CharBuffer;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.CharsetEncoder;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.snowmongoose.generator.StringCooker;
import org.snowmongoose.generator.transformer.IStringTransformer;

/**
 * @author Oliver Huin
 *  
 */
public class FileUtils {
	private static Pattern linePattern = Pattern.compile(".*\r?\n");

	public final static String readFileAsString(File file,IFileCharacteristics fileCharacteristics) throws IOException{
		CharsetDecoder decoder = fileCharacteristics.getCharsetDecoder();

		//Open the file and then get a channel from the stream
		FileInputStream fileInputStream = new FileInputStream(file);
		FileChannel fileChannel = fileInputStream.getChannel();

		int fileChannel_size = (int) fileChannel.size();
		//we will expects 64 chars by line, and reserve at least 16 
		int arrayList_size = (fileChannel_size>>6)|16;
		// Get the file's size and then map it into memory
		MappedByteBuffer mappedByteBuffer = fileChannel.map(FileChannel.MapMode.READ_ONLY, 0,
				(int) fileChannel.size());
		// Decode the file into a char buffer
		CharBuffer charBuffer = decoder.decode(mappedByteBuffer);
		return charBuffer.toString();
	}

	public final static String[] readFileAsStringArray(File file,
			IFileCharacteristics fileCharacteristics) throws IOException {
		List r = readFileAsList(file,fileCharacteristics);
		return  ((r.size()==0))? null:(String[]) r.toArray(new String[0]);
	}

	public final static List readFileAsList(File file, IFileCharacteristics fileCharacteristics) throws IOException{
		CharsetDecoder decoder = fileCharacteristics.getCharsetDecoder();

		//Open the file and then get a channel from the stream
		FileInputStream fileInputStream = new FileInputStream(file);
		FileChannel fileChannel = fileInputStream.getChannel();

		int fileChannel_size = (int) fileChannel.size();
		//we will expects 64 chars by line, and reserve at least 16 
		int arrayList_size = (fileChannel_size>>6)|16;
		// Get the file's size and then map it into memory
		MappedByteBuffer mappedByteBuffer = fileChannel.map(FileChannel.MapMode.READ_ONLY, 0,
				(int) fileChannel.size());
		// Decode the file into a char buffer
		CharBuffer charBuffer = decoder.decode(mappedByteBuffer);
		Matcher matcher = linePattern.matcher(charBuffer);
		List r = new ArrayList(arrayList_size);
		
		int end_of_last_search =0;  
		while (matcher.find()) {
			CharSequence charSequence = matcher.group();
			r.add(charSequence.toString());
			end_of_last_search = matcher.end();
		}
		r.add(charBuffer.subSequence(end_of_last_search, charBuffer.remaining()).toString());
		// Close the channel and the stream
		fileChannel.close();
		return r;
	}

	public final static void writeFile(File file, IFileCharacteristics fileCharacteristics, String content, boolean append)throws IOException {
		CharsetEncoder encoder = fileCharacteristics.getCharsetEncoder();
		
		FileOutputStream fileOutputStream = null;
		OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream(file,append),encoder);
		outputStreamWriter.write(content);
		outputStreamWriter.flush();
		outputStreamWriter.close();
	}


	public final static void writeFile(File file, IFileCharacteristics fileCharacteristics,
			String[] stringArray,boolean append) throws IOException{
		String content = StringCooker.join(stringArray,"\n");
		writeFile(file,fileCharacteristics,content,append);
	}

	public final static void copyFile(File inputfile, IFileCharacteristics inputfileCharacteristics,
			File outputfile, IFileCharacteristics outputfileCharacteristics,
			IStringTransformer transformer,boolean append) throws IOException {
		List input = readFileAsList(inputfile,inputfileCharacteristics);
		int input_size = input.size();
		List r = new ArrayList(input_size);
		for (int i=0; i<input_size;i++){
			String s = transformer.toString(input.get(i));
			if (s!=null) r.add(s);
		}
		writeFile(outputfile,outputfileCharacteristics,(String[]) r.toArray(new String[0]),append);
	}


}
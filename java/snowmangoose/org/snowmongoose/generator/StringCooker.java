/*
 * Licensed under GNU Lesser General Public License Version 2.1, February 1999
 * You may not use this file except in compliance with this license.
 * You may obtain a copy of this license at:
 *           http://www.opensource.org/licenses/
 * Unless required by applicable law or agreed to in writing, software
 * distributed under this license is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See this license for the specific language governing permissions and
 * limitations under this license.
 */
package org.snowmongoose.generator;

import java.util.Arrays;
import java.util.Collection;
import java.util.Map;

import org.snowmongoose.generator.transformer.IStringTransformer;

/**
 * @author <a href="olivierhuin@users.sourceforge.net">Olivier Huin </a>
 *  
 */
public class StringCooker {

	/**
	 * Replaces the searched text once by the given replacement in the given
	 * text
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * This method is equivalent to replaceObject(text, search, replacement, 1);
	 * 
	 * @param text
	 *            the text to process
	 * @param search
	 *            the text to search for
	 * @param replacement
	 *            the text to replace with
	 * @return
	 */
	public static String replaceFirstObject(Object text, Object search,
			Object replacement) {
		return replaceObject(text, search, replacement, 1);
	}

	/**
	 * Replaces all the searched text by the given replacement in the given text
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * This method is equivalent to replaceObject(text, search, replacement,
	 * -1);
	 * 
	 * @param text
	 *            the text to process
	 * @param search
	 *            the text to search for
	 * @param replacement
	 *            the text to replace with
	 * @return
	 */
	public static String replaceAllObject(Object text, Object search,
			Object replacement) {
		return replaceObject(text, search, replacement, -1);
	}

	/**
	 * Replaces the searched text by the given replacement in the given text a
	 * specific number of time.
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * Example:
	 * 
	 * <pre>
	 * 
	 *  
	 *   
	 *    
	 *     
	 *      StringCooker.replaceObject(&quot;acadabra&quot;,&quot;a&quot;,new Integer(4),2)) -&gt; &quot;4c4dabra&quot;
	 *      StringCooker.replaceAllObject(&quot;Today is date&quot;,&quot;date&quot;,new Date())) -&gt; Today is Fri Feb 18 17:30:59 GMT 2000
	 *      StringCooker.replaceObject(&quot;acadabra&quot;,null,&quot;A&quot;,2)); -&gt; &quot;acadabra&quot;
	 *      
	 *     
	 *    
	 *   
	 *  
	 * </pre>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * 
	 * @param text
	 *            the text to process
	 * @param search
	 *            the text to search for
	 * @param replacement
	 *            the text to replace with
	 * @param max
	 *            the maximum number of replacements. If -1, will replace all
	 * @return The resulting String
	 */
	public static String replaceObject(Object text, Object search,
			Object replacement, int max) {
		if (text == null)
			return null;
		if (text.toString().length() == 0 || isObjectEmpty(search)
				|| replacement == null || max == 0) {
			return text.toString();
		}

		StringBuffer r = new StringBuffer(text.toString().length());
		int start = 0, end = 0;
		while ((end = text.toString().indexOf(search.toString(), start)) != -1) {
			r.append(text.toString().substring(start, end)).append(replacement);
			start = end + search.toString().length();

			if (--max == 0) {
				break;
			}
		}
		r.append(text.toString().substring(start));
		return r.toString();
	}

	/**
	 * Returns true is the object id a null or an empty string
	 * 
	 * @param obj
	 *            the object to test. NB: it will be converted to a string first
	 * @return true is the object id a null or an empty string
	 */
	public final static boolean isObjectEmpty(Object obj) {
		if (obj == null)
			return true;
		return (obj.toString().length() == 0);
	}

	/**
	 * Joins the objects together using the separator to separate every object
	 * 
	 * @param array
	 *            an array of object
	 * @param separator
	 *            a separator
	 * @return the resulting String
	 */
	public static String join(Object[] array, Object separator) {
		if (array == null) {
			return null;
		}
		if (array.length == 0) {
			return "";
		}

		String l_separator = separator == null ? "" : separator.toString();

		int rowsize = array[0] == null ? 16 + l_separator.length() : array[0]
				.toString().length()
				+ l_separator.length();
		StringBuffer r = new StringBuffer(array.length * rowsize);

		for (int i = 0; i < array.length; i++) {
			if (i > 0) {
				r.append(separator);
			}
			if (array[i] != null) {
				r.append(array[i]);
			}
		}
		return r.toString();
	}
	/**
	 * Joins the objects together using the separator to separate every object
	 * 
	 * @param array
	 *            an array of object
	 * @param separator
	 *            a separator
	 * @param transformer
	 * @return the resulting String
	 */
	public static String join(Object[] array, Object separator,IStringTransformer transformer) {
		if (transformer==null)throw new RuntimeException("a transformer must be provided !");
		if (array == null) {
			return null;
		}
		if (array.length == 0) {
			return "";
		}

		String l_separator = separator == null ? "" : separator.toString();

		int rowsize = array[0] == null ? 16 + l_separator.length() : array[0]
				.toString().length()
				+ l_separator.length();
		StringBuffer r = new StringBuffer(array.length * rowsize);

		for (int i = 0; i < array.length; i++) {
			if (i > 0) {
				r.append(separator);
			}
			if (array[i] != null) {
				r.append(transformer.toString(array[i]));
			}
		}
		return r.toString();
	}
	/**
	 * Joins the objects together using the separator to separate every object
	 * 
	 * @param array
	 *            an array of object
	 * @param separator
	 *            a separator
	 * @param transformer
	 * @return the resulting String
	 */
	public static String join(Object[] array, Object separator,IStringTransformer[] transformerArray) {
		if (transformerArray==null)throw new RuntimeException("a transformer must be provided !");
		if (array == null) {
			return null;
		}
		if (array.length == 0) {
			return "";
		}
		if (array.length!=transformerArray.length) throw new RuntimeException("we should have one  transformer for each object!"+transformerArray.length+" transformer for "+array.length);

		String l_separator = separator == null ? "" : separator.toString();

		int rowsize = array[0] == null ? 16 + l_separator.length() : array[0]
				.toString().length()
				+ l_separator.length();
		StringBuffer r = new StringBuffer(array.length * rowsize);

		for (int i = 0; i < array.length; i++) {
			if (i > 0) {
				r.append(separator);
			}
			if (array[i] != null) {
				r.append(transformerArray[i].toString(array[i]));
			}
		}
		return r.toString();
	}
		
	/**
	 * Returns true if the array is null or empty
	 * 
	 * @param strArray
	 *            an array of object
	 * @return true if the array is null or empty
	 */
	public final static boolean isArrayEmpty(Object[] strArray) {
		if (strArray == null)
			return true;
		return (strArray.length == 0);
	}

	/**
	 * Replaces each key of the map by its value in the text
	 * <p>
	 * This method is equivalent to replaceMap(text, searchreplMap, -1);
	 * 
	 * @param text
	 *            the text to process
	 * @param searchreplMap
	 *            the map containing a set of pairs of key+value.
	 *            <p>
	 *            The key corresponds to the string to search while the value
	 *            corresponds to the replacement value for this key.
	 * @return the resulting String
	 */
	public static String replaceAllMap(Object text, Map searchreplMap) {
		return replaceMap(text, searchreplMap, -1);
	}

	/**
	 * Replaces once each key of the map by its value in the text
	 * <p>
	 * This method is equivalent to replaceMap(text, searchreplMap, 1);
	 * 
	 * @param text
	 *            the text to process
	 * @param searchreplMap
	 *            the map containing a set of pairs of key+value.
	 *            <p>
	 *            The key corresponds to the string to search while the value
	 *            corresponds to the replacement value for this key.
	 * @return the resulting String
	 */
	public static String replaceFirstMap(Object text, Map searchreplMap) {
		return replaceMap(text, searchreplMap, 1);
	}

	/**
	 * Replaces each key of the map by its value in the text a specific number
	 * of time.
	 * 
	 * <pre>
	 * 
	 *  
	 *   
	 *    
	 *     
	 *     HashMap map2Values = new HashMap();
	 *     map2Values.put(&quot;a&quot;,&quot;A&quot;);
	 *     map2Values.put(&quot;r&quot;,&quot;R&quot;);
	 *     StringCooker.replaceMap(&quot;acadabra&quot;,map2Values,2) -&gt; &quot;AcAdabRa&quot; 
	 *       
	 *     
	 *    
	 *   
	 *  
	 * </pre>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * 
	 * @param text
	 *            the text to process
	 * @param searchreplMap
	 *            the map containing a set of pairs of key+value.
	 *            <p>
	 *            The key corresponds to the string to search while the value
	 *            corresponds to the replacement value for this key.
	 * @param max
	 *            the maximum number of replacements. If -1, will replace all
	 * @return the resulting String
	 */
	public static String replaceMap(Object text, Map searchreplMap, int max) {
		if (text == null)
			return null;
		if (searchreplMap == null)
			return text.toString();
		String r = text.toString();
		String[] keys = (String[]) searchreplMap.keySet()
				.toArray(new String[1]);
		Arrays.sort(keys, ComparatorFactory.stringLengthComparator());
		//for each keys replace with the its value
		for (int i = 0; i < keys.length; i++) {
			if (keys[i] == null)
				continue;
			r = replaceObject(r, keys[i], searchreplMap.get(keys[i]), max);
		}
		return r;

	}

	/**
	 * Replaces once the variables found in the text by its corresponding value
	 * in the collection.
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * This method is equivalent to replaceCollection(text, variable, _startIndex, withCollection,1);
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withCollection
	 *            a collection of objects.
	 * @return the resulting String
	 */
	public static String replaceFirstCollection(Object text, String variable,
			int _startIndex, Collection withCollection) {
		return replaceCollection(text, variable, _startIndex, withCollection, 1);

	}

	/**
	 * Replaces all the variables found in the text by its corresponding value
	 * in the collection.
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * This method is equivalent to replaceCollection(text, variable, _startIndex, withCollection,-1);
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withCollection
	 *            a collection of objects.
	 * @return the resulting String
	 */
	public static String replaceAllCollection(Object text, String variable,
			int _startIndex, Collection withCollection) {
		if (_startIndex == -1)
			throw new RuntimeException("the start index must be positive !");
		return replaceCollection(text, variable, _startIndex, withCollection,
				-1);

	}

	/**
	 * Replaces all the variables found in the text by its corresponding value
	 * in the collection, a specific number of time.
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * Example:
	 * 
	 * <pre>
	 * 
	 *  
	 *  ArrayList list2Values = new ArrayList();
	 *  list2Values.add(new Integer(100));
	 *  list2Values.add("200");
	 *  
	 *  StringCooker.replaceCollection("a?b?c?d?e?f?g","?",-1,list2Values,2)); -&gt; "a100b100c200d200e?f?g"
	 *  StringCooker.replaceCollection("a$1b$2c$2d$1e$2.$1","$",1,list2Values,2)-&gt; "a100b200c200d100e$2.$1"
	 *    
	 *   
	 *  
	 * </pre>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withCollection
	 *            a collection of objects.
	 * @param max
	 *            the maximum number of replacements. If -1, will replace all
	 * @return the resulting String
	 */
	public static String replaceCollection(Object text, String variable,
			int _startIndex, Collection withCollection, int max) {
		if (text == null)
			return null;
		if (withCollection == null)
			return text.toString();
		return replaceArray(text, variable, _startIndex, withCollection
				.toArray(), max);
	}

	/**
	 * Replaces once all the variables found in the text by its corresponding
	 * value in the array.
	 * <p>
	 * This method is equivalent to replaceArray(text, variable, _startIndex,
	 * withArray, 1);
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withArray
	 *            an array of objects.
	 * @return the resulting String
	 */
	public static String replaceFirstArray(Object text, String variable,
			int _startIndex, Object[] withArray) {
		return replaceArray(text, variable, _startIndex, withArray, 1);

	}

	/**
	 * 
	 * Replaces all the variables found in the text by its corresponding value
	 * in the array.
	 * <p>
	 * This method is equivalent to replaceArray(text, variable, _startIndex,
	 * withArray, -1);
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withArray
	 *            an array of objects.
	 * @param max
	 *            the maximum number of replacements. If -1, will replace all
	 * @return the resulting String
	 */
	public static String replaceAllArray(Object text, String variable,
			int _startIndex, Object[] withArray) {
		if (_startIndex == -1)
			throw new RuntimeException("the start index must be positive !");

		return replaceArray(text, variable, _startIndex, withArray, -1);

	}

	/**
	 * Replaces all the variables found in the text by its corresponding value
	 * in the array, a specific number of time.
	 * <p>
	 * Note: All the parameters of type Object will be converted to String.
	 * <p>
	 * Example:
	 * 
	 * <pre>
	 * 
	 *   
	 *  	Object[] array2Values = {&quot;100&quot;,new Integer(200)};
	 *      StringCooker.replaceArray(&quot;a?b?c?d?e?f?g&quot;,&quot;?&quot;,-1,array2Values,2) -&gt; &quot;a100b100c200d200e?f?g&quot;
	 *      StringCooker.replaceArray(&quot;a$1b$2c$2d$1e$2.$1&quot;,&quot;$&quot;,1,array2Values,2)-&gt; &quot;a100b200c200d100e$2.$1&quot;
	 *    
	 *   
	 *  
	 * </pre>
	 * 
	 * For more examples, see the Junit tests (StringCookerTest)
	 * <p>
	 * 
	 * @param text
	 *            the text to process
	 * @param variable
	 *            the variable prefix, usually $ or ?
	 * @param _startIndex
	 *            If used, the start index can be any positive number (but
	 *            usually 0 or 1). If -1, the indexing will not be used.
	 *            <p>
	 *            The index will be incremented starting from the startIndex and
	 *            concatenated with the variable prefix
	 *            <p>
	 *            Example: $var7,$var8,$var9 would correspond to the variable
	 *            $var and the startindex 7 and an array with 3 elements could
	 *            be processed.
	 * @param withArray
	 *            an array of objects.
	 * @param max
	 *            the maximum number of replacements. If -1, will replace all
	 * @return the resulting String
	 */
	public static String replaceArray(Object text, String variable,
			int _startIndex, Object[] withArray, int max) {
		if (text == null)
			return null;
		if (text.toString().length() == 0 || isArrayEmpty(withArray)
				|| max == 0) {
			return text.toString();
		}
		if (variable == null)
			throw new NullPointerException("the variable cannot be null!");

		String r = text.toString();

		if (_startIndex == -1) {
			for (int i = 0; i < withArray.length; i++) {
				r = replaceObject(r, variable, withArray[i], max);
			}//end for

		} else {
			//Obviously, we must replace $12 before $1
			for (int i = withArray.length - 1; i >= 0; i--) {
				r = replaceObject(r, variable + (i + _startIndex),
						withArray[i], max);

			}//end for
		}

		return r;
	}

	/**
	 * Build a string using the basic builder
	 * @param script
	 * @param searchreplMap
	 * @return
	 */
	public static String basicBuild(String script, Map searchreplMap) {
		return StringBuilderFactory.basicStringBuilder(script).build(
				searchreplMap);
	}
	
	/**
	 * Apply a string transformation on an array
	 * @param transformer the string stransformer
	 * @param objectArray an array of object
	 * @return an array of string
	 */
	public static String[] transformArray(IStringTransformer transformer,Object[] objectArray){
		if (transformer==null)throw new RuntimeException("A transformer must be provided !");
		if (objectArray==null) return null;
		if (objectArray.length==0) return new String[0];
		String[] r = new String[objectArray.length];
		
		for (int i=r.length; --i>=0;){
			r[i]=transformer.toString(objectArray[i]);
		}
		return r;
	}
	/**
	 * Apply a string transformation on an array
	 * @param transformer the string stransformer
	 * @param objectArray an array of object
	 * @return an array of string
	 */
	public static String[] transformArray(IStringTransformer[] transformerArray,Object[] objectArray){
		if (transformerArray==null)throw new RuntimeException("An array of transformer must be provided !");
		if (objectArray==null) return null;
		if (objectArray.length==0) return new String[0];
		if (objectArray.length!=transformerArray.length) throw new RuntimeException("we should have one  transformer for each object!"+transformerArray.length+" transformer for "+objectArray.length);
		String[] r = new String[objectArray.length];
		
		for (int i=r.length; --i>=0;){
			r[i]=transformerArray[i].toString(objectArray[i]);
		}
		return r;
	}
	
	

}
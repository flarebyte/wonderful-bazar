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

import java.util.Comparator;

/**
 * @author Oliver Huin
 *
 */
public class ComparatorFactory {
	
	 public static Comparator stringLengthComparator() {
        return new StringLengthComparator();
    }
	private static class StringLengthComparator implements Comparator {
		/* 
		 * @see java.util.Comparator#compare(java.lang.Object, java.lang.Object)
		 */
		public int compare(Object _arg0, Object _arg1) {
			String s0 = (_arg0==null ? "": (String)_arg0 );
			String s1 = (_arg1==null ?  "": (String)_arg1 );
			//sort from the larger variable to smaller variable
			//this way, if we have 2 variables: java and java.home
			//both will be replaced
			return s1.length()-s0.length();
		}
    }
}

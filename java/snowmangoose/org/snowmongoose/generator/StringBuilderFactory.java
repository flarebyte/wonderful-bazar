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

import org.snowmongoose.generator.builder.BasicStringBuilder;
import org.snowmongoose.generator.builder.IStringBuilder;

/**
 * @author Oliver Huin
 *
 */
public class StringBuilderFactory {
	public static IStringBuilder basicStringBuilder(String script){
		return new BasicStringBuilder(script);
	}
}

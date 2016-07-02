/*
 * Created on Jul 12, 2005
 *
 */
package org.snowmongoose.pov3d.transformer;

import org.snowmongoose.pov3d.Point3D;
import org.snowmongoose.pov3d.Vector3D;

/**
 * @author Oliver Huin
 *  
 */
public class PovToStringBuilder {
	public final static String toString(Point3D point) {
		if (point == null)
			return "";
		StringBuffer r = new StringBuffer();
		r.append("<").append(point.x).append(",").append(point.y).append(",")
				.append(",").append(point.z).append(">");
		return r.toString();
	}

	public final static String toString(Vector3D vector) {
		if (vector == null)
			return "";
		StringBuffer r = new StringBuffer();
		r.append("<").append(vector.x).append(",").append(vector.y).append(",")
				.append(vector.z).append(">");
		return r.toString();
	}


	public final static String toString(Number value) {
		if (value == null)
			return "";
		return value.toString();
	}

	public final static String toString(Object arg) {
		if (arg == null)
			return "";
		if (arg instanceof Point3D)
			return toString((Point3D) arg);
		if (arg instanceof Vector3D)
			return toString((Vector3D) arg);
		if (arg instanceof Number)
			return toString((Number) arg);
		return arg.toString();
	}
}
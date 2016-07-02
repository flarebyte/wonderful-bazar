/*
 * Created on Jul 11, 2005
 *
 */
package org.snowmongoose.pov3d;

/**
 * @author Oliver Huin
 *
 */
public class Geometry3DUtils {

	/**
	 * Computes the <i>distance</i> between the two specified
	 * <code>Point3D</code>.
	 *
	 * @param p1,&nbsp;p2 the two <code>Point3D</code> to compute the
	 *                    distance between.
	 * @return the distance between the two specified <code>Point3D</code>.
	 */
	public static double distance(Point3D p1, Point3D p2)
	{
	    return Math.sqrt(Geometry3DUtils.distanceSq(p1, p2));
	}

	/**
	 * Computes the <i>square of the distance</i> between the two specified
	 * <code>Point3D</code>.
	 *
	 * @param p1,&nbsp;p2 the two <code>Point3D</code> to compute the
	 *                    square of the distance between.
	 * @return the square of the distance between the two specified
	 *         <code>Point3D</code>.
	 */
	public static double distanceSq(Point3D p1, Point3D p2)
	{
	    double dx, dy, dz;
	
	    dx = p1.x - p2.x;
	    dy = p1.y - p2.y;
	    dz = p1.z - p2.z;
	
	    return (dx*dx + dy*dy + dz*dz);
	}

	/**
	 * Computes the <i>cross product</i> of the two specified
	 * <code>vector3D</code>.
	 *
	 * @param v1,&nbsp;v2 the two <code>vector3D</code> to cross product.
	 * @return an instance of <code>vector3D</code> that is the cross
	 * product of the two specified <code>vector3D</code>.
	 */
	public static Vector3D crossProduct(Vector3D v1, Vector3D v2)
	{
	    return new Vector3D((v1.y * v2.z) - (v1.z * v2.y),
	                        (v1.z * v2.x) - (v1.x * v2.z),
	                        (v1.x * v2.y) - (v1.y * v2.x));
	}

	/**
	 * Computes the <i>dot product</i> of the two specified
	 * <code>vector3D</code>.
	 *
	 * @param v1,&nbsp;v2 the two <code>vector3D</code> to dot product.
	 * @return the dot product of the two specified
	 * <code>vector3D</code>.
	 */
	public static double dotProduct(Vector3D v1, Vector3D v2)
	{
	    return ((v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z));
	}

	/**
	 * Computes a normed version of the specified <code>Vector3D</code>.
	 * The norm of the <code>Vector3D</code> argument is assumed to be non
	 * zero.
	 *
	 * @param v a <code>Vector3D</code> object, whose norm is non zero.
	 * @return a normed version of the specified <code>Vector3D</code>.
	 */
	public static Vector3D normalization(Vector3D v)
	{
	    return Geometry3DUtils.product(v, 1.0 / v.norm());
	}

	/**
	 * Computes the <i>opposite</i> of the specified <code>vector3D</code>.
	 *
	 * @param v the <code>vector3D</code> to compute the opposite of.
	 * @return an instance of <code>vector3D</code> that is the
	 *         opposite of the specified <code>vector3D</code>.
	 */
	public static Vector3D opposite(Vector3D v)
	{
	    return new Vector3D(- v.x,
	                        - v.y,
	                        - v.z);
	}

	/**
	 * Computes the <i>product</i> of the specified <code>vector3D</code>
	 * with the specified double factor.
	 *
	 * @param v the <code>vector3D</code> product with.
	 * @param f the double factor.
	 * @return an instance of <code>vector3D</code> that is the product of
	 * the specified <code>vector3D</code> with the specified double factor.
	 */
	public static Vector3D product(Vector3D v, double f)
	{
	    return new Vector3D(f * v.x,
	                        f * v.y,
	                        f * v.z);
	}

	/**
	 * Computes the <i>projection</i> of the specified <code>vector3D</code>
	 * on the hyperplane given by the specified normal.
	 *
	 * @param v the <code>vector3D</code> project.
	 * @param n the normal of the hyperplane to project the specified
	 *        <code>vector3D</code> on.
	 * @return an instance of <code>vector3D</code> that is the projection
	 * of the specified <code>vector3D</code> on the hyperplane given by the
	 * specified normal.
	 */
	public static Vector3D projection(Vector3D v, Vector3D n)
	{
	    double sc = dotProduct(v, n);
	    return Geometry3DUtils.sum(v, product(n, -sc));
	}

	/**
	 * Computes the <i>sum</i> of the two specified <code>vector3D</code>.
	 *
	 * @param v1,&nbsp;v2 the two <code>vector3D</code> to sum.
	 * @return an instance of <code>vector3D</code> that is the sum of the
	 * two specified <code>vector3D</code>.
	 */
	public static Vector3D sum(Vector3D v1, Vector3D v2)
	{
	    return new Vector3D((v1.x + v2.x),
	                        (v1.y + v2.y),
	                        (v1.z + v2.z));
	}

}

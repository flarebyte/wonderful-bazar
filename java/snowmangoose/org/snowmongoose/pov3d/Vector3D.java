/*
 * Created on Jul 11, 2005
 *
 */
package org.snowmongoose.pov3d;

/**
 * The <code>Vector3D</code> class defines a high precision vector in the 3
 * dimensional space, given by its 3D coordinates.  This class provides
 * most of the classical operations on vectors (norm, dot product, cross
 * product, projection...).
 *
 * @see Point3D
 *
 */
public class Vector3D implements java.io.Serializable
{
    /**
     * The <i>x</i> coordinate.
     * @serial
     */
    public double x;

    /**
     * The <i>y</i> coordinate.
     * @serial
     */
    public double y;

    /**
     * The <i>z</i> coordinate.
     * @serial
     */
    public double z;

    /**
     * Creates a <code>Vector3D</code> object initialized with the
     * specified 3D coordinates.
     * 
     * @param x,&nbsp;y,&nbsp;z the coordinates to which to set the newly
     *                          constructed <code>Vector3D</code>.
     */
    public Vector3D(double x, double y, double z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /**
     * Initializes a newly created <code>Vector3D</code> object so that it
     * represents the same 3 dimensional vector as the argument.  In other
     * words, the newly created <code>Vector3D</code> is a copy of the
     * specified <code>Vector3D</code>.
     * 
     * @param p a <code>Vector3D</code> object.
     */
    public Vector3D(Vector3D v)
    {
        this(v.x, v.y, v.z);
    }

    /**
     * Initializes a newly created <code>Vector3D</code> object so that it
     * represents the vector <i>connecting</i> the two specified 3D points.
     * 
     * @param source the source <code>Point3D</code>.
     * @param dest the destination <code>Point3D</code>.
     */
    public Vector3D(Point3D source, Point3D dest)
    {
        this(dest.x - source.x,
             dest.y - source.y,
             dest.z - source.z);
    }

    

    /**
     * Computes the <i>norm</i> of this <code>Vector3D</code>.
     *
     * @return the norm of this <code>Vector3D</code>.
     */
    public double norm()
    {
        return Math.sqrt(normSq());
    }

    /**
     * Computes the <i>square of the norm</i> of this <code>Vector3D</code>.
     *
     * @return the square of the norm of this <code>Vector3D</code>.
     */
    public double normSq()
    {
        return (x*x + y*y + z*z);
    }

    
}
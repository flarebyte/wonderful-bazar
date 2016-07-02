/*
 * Created on Jul 11, 2005
 *
 * TODO To change the template for this generated file go to
 * Window - Preferences - Java - Code Style - Code Templates
 */
package org.snowmongoose.pov3d;

/**
 * The <code>Point3D</code> class defines a high precision point in the 3
 * dimensional space, given by its 3D coordinates.  This class provides
 * most of the classical operations on points (translation, distance...).
 *
 * @see java.awt.geom.Point2D
 * @see Vector3D
 *
 */
public class Point3D implements java.io.Serializable
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
     * Creates a <code>Point3D</code> object initialized with the specified
     * 3D coordinates.
     *
     * @param x,&nbsp;y,&nbsp;z the coordinates to which to set the newly
     *                          constructed <code>Point3D</code>.
     */
    public Point3D(double x, double y, double z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /**
     * Initializes a newly created <code>Point3D</code> object so that it
     * represents the same 3 dimensional point as the argument.  In other
     * words, the newly created <code>Point3D</code> is a copy of the
     * specified <code>Point3D</code>.
     *
     * @param p a <code>Point3D</code> object.
     */
    public Point3D(Point3D p)
    {
        this(p.x, p.y, p.z);
    }

    /**
     * Initializes a newly created <code>Point3D</code> object so that it
     * represents the <i>translation</i> of the specified
     * <code>Point3D</code> by the specified <code>Vector3D</code>.
     *
     * @param p a <code>Point3D</code> object.
     * @param v a <code>Vector3D</code> object.
     */
    public Point3D(Point3D p, Vector3D v)
    {
        this(p.x + v.x,
             p.y + v.y,
             p.z + v.z);
    }


    /**
     * Translates this <code>Point3D</code> by the specified
     * <code>Vector3D</code>.
     *
     * @param v the <code>Vector3D</code> to translate this
     *          <code>Point3D</code> by.
     */
    public void translate(Vector3D v)
    {
        x += v.x;
        y += v.y;
        z += v.z;
    }

}

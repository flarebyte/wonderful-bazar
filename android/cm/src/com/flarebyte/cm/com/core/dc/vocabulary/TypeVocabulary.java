package com.flarebyte.cm.com.core.dc.vocabulary;

/**
 * @See http://dublincore.org/documents/dcmi-type-vocabulary/
 * @author olivier
 * @deprecated
 */
@Deprecated
public interface TypeVocabulary {
	/** An aggregation of resources. */
	public final static String COLLECTION = "Collection";
	/** Data encoded in a defined structure. */
	public final static String DATASET = "Dataset";
	/** A non-persistent, time-based occurrence. */
	public final static String EVENT = "Event";
	/** A visual representation other than text. */
	public final static String IMAGE = "Image";
	/**
	 * A resource requiring interaction from the user to be understood,
	 * executed, or experienced.
	 */
	public final static String INTERACTIVE_RESOURCE = "Interactive Resource";
	/**
	 * A series of visual representations imparting an impression of motion when
	 * shown in succession.
	 */
	public final static String MOVING_IMAGE = "Moving Image";
	/** An inanimate, three-dimensional object or substance. */
	public final static String PHYSICAL_OBJECT = "Physical Object";
	/** A system that provides one or more functions. */
	public final static String SERVICE = "Service";
	/** A computer program in source or compiled form. */
	public final static String SOFTWARE = "Software";
	/** A resource primarily intended to be heard. */
	public final static String SOUND = "Sound";
	/** Image, A static visual representation. */
	public final static String STILL = "Still";
	/** A resource consisting primarily of words for reading. */
	public final static String TEXT = "Text";
}

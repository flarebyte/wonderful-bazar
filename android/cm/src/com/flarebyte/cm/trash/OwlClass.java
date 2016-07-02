package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

/**
 * OWL distinguishes six types of class descriptions:
 * 
 * <ul>
 * a class identifier (a URI reference)
 * <li>an exhaustive enumeration of individuals</li>
 * that together form the instances of a class</li>
 * <li>a property restriction
 * <li>the intersection of two or more class descriptions</li>
 * <li>the union of two or more class descriptions</li>
 * <li>the complement of a class description</li>
 * </ul>
 * 
 * @author olivier
 * 
 */
public interface OwlClass extends OwlResource {
	enum ALTERNATIVE {
		CLASS, ENUMERATED
	};

	enum MODALITY {
		COMPLETE, PARTIAL
	};

	public ALTERNATIVE getAlternative();

	public OwlClassDescription[] getClassDescriptionArray();

	public OwlClassDescription[] getDisjointClassArray();

	public OwlClassDescription[] getEquivalentClassArray();

	public SemanticId[] getIndividualIdArray();

	public MODALITY getModality();

	public OwlClassDescription[] getSubClassOfArray();

}

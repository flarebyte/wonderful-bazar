package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.immutable.SemanticId;

/**
 * classID, restriction, or description
 * 
 * @author olivier
 * 
 */
public interface OwlType {
	public SemanticId getAsId();

	public OwlRestriction getAsRestriction();

}

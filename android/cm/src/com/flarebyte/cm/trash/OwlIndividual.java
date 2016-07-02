package com.flarebyte.cm.trash;

import com.flarebyte.storm.struct.data.DataLifecycle;
import com.flarebyte.storm.struct.data.DataConfidentiality;

public interface OwlIndividual extends OwlResource {
	public OwlIndividual[] getAllDifferentAndDistinctArray();

	public OwlIndividual[] getDifferentFromArray();

	public DataLifecycle getLifecycle();

	public DataConfidentiality getPrivacy();

	public OwlIndividual[] getSameAsArray();

}

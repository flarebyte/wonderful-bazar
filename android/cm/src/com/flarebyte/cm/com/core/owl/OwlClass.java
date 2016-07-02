package com.flarebyte.cm.com.core.owl;

public interface OwlClass extends OwlId {
	public OwlAnnotation[] getAnnotationArray();

	public Object[] getDescriptionArray();

	public OwlIndividualId[] getIndividualIdArray();

	public OwlModality getModality();

	public Boolean isDeprecated();

}

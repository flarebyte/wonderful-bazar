package com.flarebyte.cm.trash;

import com.flarebyte.storm.facet.SemanticIdentifiable;
import com.flarebyte.storm.struct.dc.DublinCore;
import com.flarebyte.storm.struct.immutable.SemanticId;
import com.flarebyte.storm.struct.skos.SkosDocumentation;
import com.flarebyte.storm.struct.skos.SkosLabel;

public interface OwlResource extends SemanticIdentifiable {
	public OwlAnnotation[] getAnnotations();

	public String getComment();

	public DublinCore getDublinCore();

	public String getLabel();

	public SemanticId[] getSeeAlsoArray();

	public SkosDocumentation getSkosDocumentation();

	public SkosLabel getSkosLabel();

	public OwlType getType();

	public boolean isDeprecated();

}

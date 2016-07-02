package com.flarebyte.cm.com.core.dc;

import java.net.URI;

import com.flarebyte.cm.com.core.dc.vocabulary.Term;
import com.flarebyte.cm.com.core.dc.vocabulary.Vocabulary;

public interface MetadataRegistry {
	public DescriptionSet getDescriptionSet(URI uri);

	public DublinCore getResourceDescription(URI uri);

	public Term getTerm(URI uri);

	public Vocabulary getVocabulary(URI uri);

}

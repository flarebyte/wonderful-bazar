package com.flarebyte.cm.com.core.dc.vocabulary;

import com.flarebyte.cm.com.core.Compilable;

public interface Vocabulary extends Compilable {
	public Clazz[] getClazzArray();

	public Datatype[] getDatatypeArray();

	public Property[] getPropertyArray();

	public Term[] getTermArray();

	public VocabularyEncodingScheme[] getVocabularyEncodingSchemeArray();

}

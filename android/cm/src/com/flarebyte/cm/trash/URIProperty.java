package com.flarebyte.cm.trash;

import java.net.URI;
import java.net.URISyntaxException;

import com.flarebyte.storm.struct.dc.DublinCore;
import com.flarebyte.storm.struct.owl.OwlAnnotation;
import com.flarebyte.storm.struct.owl.OwlClassDescription;
import com.flarebyte.storm.struct.owl.OwlObjectProperty;
import com.flarebyte.storm.struct.owl.OwlType;
import com.flarebyte.storm.struct.skos.SkosDocumentation;
import com.flarebyte.storm.struct.skos.SkosLabel;

public class URIProperty implements OwlObjectProperty {

    private final URI identifier;
    private final SemanticId parent;

    public URIProperty(final String identifier) {
	super();
	try {
	    this.identifier = new URI(identifier);
	} catch (URISyntaxException e) {
	    throw new RuntimeException("Invalid identifier: " + identifier);
	}
	this.parent = null;
    }

    public SemanticId add(final String identifier) {
	return null;
    }

    @Override
    public SemanticId getAbout() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public OwlAnnotation[] getAnnotations() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public String getComment() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public OwlClassDescription[] getDomainArray() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public DublinCore getDublinCore() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public SemanticId[] getInverseOfArray() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public String getLabel() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public OwlClassDescription[] getRangeArray() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public SemanticId[] getSeeAlsoArray() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public SkosDocumentation getSkosDocumentation() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public SkosLabel getSkosLabel() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public OwlType getType() {
	// TODO Auto-generated method stub
	return null;
    }

    @Override
    public boolean isDeprecated() {
	// TODO Auto-generated method stub
	return false;
    }

    @Override
    public boolean isFunctional() {
	// TODO Auto-generated method stub
	return false;
    }

    @Override
    public boolean isInverseFunctional() {
	// TODO Auto-generated method stub
	return false;
    }

    @Override
    public boolean isSymmetric() {
	// TODO Auto-generated method stub
	return false;
    }

    @Override
    public boolean isTransitive() {
	// TODO Auto-generated method stub
	return false;
    }

}

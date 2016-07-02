package com.flarebyte.cm.trash;

import java.util.Locale;

import android.net.Uri;

import com.flarebyte.storm.action.DataRef;
import com.flarebyte.storm.struct.immutable.LocalisedUnitValue;
import com.flarebyte.storm.struct.immutable.SemanticId;

public class SemanticLiteral extends LocalisedUnitValue {
    public final static SemanticLiteral NULL_LITERAL = new SemanticLiteral(null, UNKNOWN_DATATYPE, null);

    protected SemanticLiteral(final Object value, final Uri datatype, final Locale locale) {
	super(value, datatype, locale);
    }

    public DataRef getDataRef() {
	return (DataRef) this.value;
    }

    public DataRef[] getDataRefArray() {
	return (DataRef[]) this.value;

    }

    public IndirectNode getIndirectNode() {
	return (IndirectNode) this.value;

    }

    public IndirectNode[] getIndirectNodeArray() {
	return (IndirectNode[]) this.value;

    }

    public SemanticLiteral[] getLiteralArray() {
	return (SemanticLiteral[]) this.value;
    }

    public SemanticId getSemanticId() {
	return (SemanticId) this.value;
    }

    public SemanticId[] getSemanticIdArray() {
	return (SemanticId[]) this.value;

    }

}

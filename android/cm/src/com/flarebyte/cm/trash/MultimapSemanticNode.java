package com.flarebyte.cm.trash;

import java.util.Collection;
import java.util.Iterator;
import java.util.Locale;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import android.net.Uri;

import com.flarebyte.storm.struct.SemanticNode;
import com.flarebyte.storm.struct.Value;
import com.flarebyte.storm.struct.immutable.NullSemanticNode;
import com.google.common.base.Preconditions;
import com.google.common.base.Predicate;
import com.google.common.collect.HashMultimap;
import com.google.common.collect.Iterables;
import com.google.common.collect.Multimap;
import com.google.common.collect.Multiset;

public class MultimapSemanticNode implements SemanticNode<MultimapSemanticNode> {

    private final static Value[] getValueArray(final Collection<MultimapSemanticNode> nodeCollection) {
	if (nodeCollection == null)
	    return null;
	Value[] r = new Value[nodeCollection.size()];
	int i = 0;
	for (MultimapSemanticNode node : nodeCollection) {
	    r[i] = node.getNodeValue();
	    i++;
	}
	return r;
    }

    MultimapSemanticNode parent;
    Uri nodeId;
    Value nodeValue;

    Multimap<Uri, MultimapSemanticNode> nodeMultimap = HashMultimap.create();

    protected MultimapSemanticNode(final MultimapSemanticNode parent) {
	super();
	this.parent = parent;
    }

    protected Map<Uri, Collection<MultimapSemanticNode>> asMap() {
	return this.nodeMultimap.asMap();
    }

    @Override
    public void clear() {
	this.nodeMultimap.clear();

    }

    @Override
    public boolean containsEntry(final Uri arg0, final MultimapSemanticNode arg1) {
	return this.nodeMultimap.containsEntry(arg0, arg1);
    }

    @Override
    public boolean containsKey(final Uri id) {
	return this.nodeMultimap.containsKey(id);
    }

    @Override
    public boolean containsValue(final MultimapSemanticNode value) {
	return this.nodeMultimap.containsValue(value);
    }

    @Override
    public MultimapSemanticNode createChildNode() {
	MultimapSemanticNode r = new MultimapSemanticNode(this);
	return r;
    }

    protected Collection<Entry<Uri, MultimapSemanticNode>> entries() {
	return this.nodeMultimap.entries();
    }

    @Override
    public Iterable<MultimapSemanticNode> filter(final Predicate<MultimapSemanticNode> predicate) {
	Preconditions.checkNotNull(predicate, PREDICATE_SHOULD_NOT_BE_NULL);
	Iterable<MultimapSemanticNode> r = Iterables.filter(this.nodeMultimap.values(), predicate);
	return r;
    }

    @Override
    public MultimapSemanticNode filterFirst(final Predicate<MultimapSemanticNode> predicate) {
	Iterator<MultimapSemanticNode> r = filter(predicate).iterator();
	return !r.hasNext() ? null : r.next();

    }

    @Override
    public Collection<MultimapSemanticNode> get(final Uri id) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	return this.nodeMultimap.get(id);
    }

    @Override
    public MultimapSemanticNode getFirst(final Uri id) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	Collection<MultimapSemanticNode> nodeCollection = get(id);
	if (nodeCollection.isEmpty())
	    return NullSemanticNode.NULL;
	MultimapSemanticNode r = nodeCollection.iterator().next();
	return r;
    }

    @Override
    public MultimapSemanticNode getFirst(final Uri id, final Locale locale) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	Preconditions.checkNotNull(locale, LOCALE_SHOULD_NOT_BE_NULL);
	Collection<MultimapSemanticNode> nodeCollection = get(id);
	if (nodeCollection.isEmpty())
	    return null;
	MultimapSemanticNode r = null;
	for (MultimapSemanticNode node : nodeCollection) {
	    if (locale.equals(node.nodeValue.getLanguageAsLocale()))
		return node;
	}
	return r;
    }

    @Override
    public Value getFirstValue(final Uri id) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	Collection<MultimapSemanticNode> nodeCollection = get(id);
	if (nodeCollection.isEmpty())
	    return null;
	Value r = nodeCollection.iterator().next().nodeValue;
	return r;
    }

    @Override
    public Value getFirstValue(final Uri id, final Locale locale) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	Preconditions.checkNotNull(locale, LOCALE_SHOULD_NOT_BE_NULL);
	Collection<MultimapSemanticNode> nodeCollection = get(id);
	if (nodeCollection.isEmpty())
	    return null;
	Value r = null;
	for (MultimapSemanticNode node : nodeCollection) {
	    if (locale.equals(node.nodeValue.getLanguageAsLocale()))
		return node.nodeValue;
	}
	return r;
    }

    @Override
    public int getLevel() {
	int r = 0;
	MultimapSemanticNode p = this;
	while (p != null) {
	    r++;
	    p = p.parent;
	}
	return r;

    }

    @Override
    public Uri getNodeId() {
	return this.nodeId;
    }

    @Override
    public Value getNodeValue() {
	return this.nodeValue;
    }

    @Override
    public MultimapSemanticNode getParentNode() {
	return this.parent;
    }

    @Override
    public MultimapSemanticNode getRoot() {
	MultimapSemanticNode r = this;
	do {
	    if (r.parent == null)
		return r;
	    r = r.parent;
	} while (true);
    }

    @Override
    public Value[] getValueArray(final Uri id) {
	Preconditions.checkNotNull(id, ID_SHOULD_NOT_BE_NULL);
	Collection<MultimapSemanticNode> nodeCollection = get(id);
	if (nodeCollection.isEmpty())
	    return null;
	Value[] r = MultimapSemanticNode.getValueArray(nodeCollection);
	return r;
    }

    @Override
    public boolean isEmpty() {
	return this.nodeMultimap.isEmpty();
    }

    @Override
    public boolean isRoot() {
	return this.parent == null;
    }

    protected Multiset<Uri> keys() {
	return this.nodeMultimap.keys();
    }

    protected Set<Uri> keySet() {
	return this.nodeMultimap.keySet();
    }

    @Override
    public boolean put(final Uri id, final MultimapSemanticNode node) {
	return this.nodeMultimap.put(id, node);
    }

    protected boolean putAll(final Multimap<? extends Uri, ? extends MultimapSemanticNode> nodes) {
	return this.nodeMultimap.putAll(nodes);
    }

    protected boolean putAll(final Uri id, final Iterable<? extends MultimapSemanticNode> multimap) {
	return this.nodeMultimap.putAll(id, multimap);
    }

    @Override
    public boolean remove(final Uri key, final MultimapSemanticNode node) {
	return this.nodeMultimap.remove(key, node);
    }

    protected Collection<MultimapSemanticNode> removeAll(final Object key) {
	return this.nodeMultimap.removeAll(key);
    }

    protected Collection<MultimapSemanticNode> replaceValues(final Uri id,
	    final Iterable<? extends MultimapSemanticNode> nodes) {
	return this.nodeMultimap.replaceValues(id, nodes);
    }

    @Override
    public void setNodeId(final Uri nodeId) {
	this.nodeId = nodeId;
    }

    @Override
    public void setNodeValue(final Value nodeValue) {
	this.nodeValue = nodeValue;
    }

    @Override
    public void setParentNode(final MultimapSemanticNode parent) {
	this.parent = parent;

    }

    @Override
    public int size() {
	return this.nodeMultimap.size();
    }

    protected Collection<MultimapSemanticNode> values() {
	return this.nodeMultimap.values();
    }
}

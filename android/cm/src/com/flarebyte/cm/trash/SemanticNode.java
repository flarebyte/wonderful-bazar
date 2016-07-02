package com.flarebyte.cm.trash;

import java.util.Collection;
import java.util.Locale;

import android.net.Uri;

import com.google.common.base.Predicate;

public interface SemanticNode<K, N, L> {
    public static final String LOCALE_SHOULD_NOT_BE_NULL = "The locale should not be null !";
    public static final String ID_SHOULD_NOT_BE_NULL = "The id should not be null !";
    public static final String NODE_SHOULD_NOT_BE_NULL = "The node should not be null !";
    public static final String PREDICATE_SHOULD_NOT_BE_NULL = "The predicate should not be null !";

    void clear();

    boolean containsEntry(K id, N node);

    boolean containsKey(K id);

    boolean containsValue(N value);

    public N createChildNode();

    Iterable<N> filter(Predicate<N> predicate);

    N filterFirst(Predicate<N> predicate);

    Collection<N> get(K id);

    N getFirst(K id);

    N getFirst(K id, Locale locale);

    public Value getFirstValue(final K id);

    public Value getFirstValue(final K id, final Locale locale);

    public int getLevel();

    public K getNodeId();

    public L getNodeValue();

    public N getParentNode();

    public N getRoot();

    public L[] getValueArray(final K id);

    boolean isEmpty();

    public boolean isRoot();

    boolean put(Uri id, N node);

    boolean remove(K key, N node);

    public void setNodeId(K id);

    public void setNodeValue(L literal);

    public void setParentNode(N parent);

    int size();

}

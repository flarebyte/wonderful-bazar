public static final Uri __label/upper()__ = Uri.parse("__about__");

/**
 * Gets the value for the __ontology__ term __label/strong()__. If there are more than one value, just returns the first one.
 * __comment/p()__
 * __desc/p()__
 * __example/p()__
 * __rdftype/p()/strong()__
 * __domain/p()/strong()__
 * __range/p()/strong()__
 * __inverseOf/p()/strong()__
 * __subPropertyOf/p()/strong()__
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value get__label/capitalize()__Value(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(__label/upper()__);
return r;
}

/**
 * Gets the value for the __ontology__ term __label/strong()__ matching a given locale. If there are more than one value,
 * just returns the first one.
 * __comment/p()__
 * __desc/p()__
 * __example/p()__
 * __rdftype/p()/strong()__
 * __domain/p()/strong()__
 * __range/p()/strong()__
 * __inverseOf/p()/strong()__
 * __subPropertyOf/p()/strong()__
 * @param node
 *            a node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a Value object or null if no value is matching the term and the locale.
 */
public final static Value get__label/capitalize()__Value(final SemanticNode node, final Locale locale) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(__label/upper()__, locale);
return r;
}

/**
 * Gets all the values for the __ontology__ term __label/strong()__.
 * __comment/p()__
 * __desc/p()__
 * __example/p()__
 * __rdftype/p()/strong()__
 * __domain/p()/strong()__
 * __range/p()/strong()__
 * __inverseOf/p()/strong()__
 * __subPropertyOf/p()/strong()__
 * @param a
 *            node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value[] get__label/capitalize()__ValueArray(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
return node.getValueArray(__label/upper()__);
}

public static final Uri __label/upper()__ = Uri.parse("__about__");

/**
 * Gets the node for the __ontology__ term __label/strong()__. If there are more than one node, just returns the first one.
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
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode get__label/capitalize()__Node(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(__label/upper()__);
	return r;
  }

/**
 * Gets the node for the __ontology__ term __label/strong()__ matching a given locale. If there are more than one node, just returns the first one.
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
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode get__label/capitalize()__Node(final SemanticNode node, final Locale locale) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(__label/upper()__, locale);
	return r;
  }

/**
 * Gets all the nodes for the __ontology__ term __label/strong()__.
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
 * @return a collection of semantic nodes.
 */
  public final static Collection<? extends SemanticNode> get__label/capitalize()__NodeCollection(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Collection<? extends SemanticNode> r = node.get(__label/upper()__);
	return r;
  }

/**
 * Gets the node for the __ontology__ term __label/strong()__ matching a given predicate. If there are more than one node, just returns the first one.
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
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode filter__label/capitalize()__Node(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.filterFirst(predicate);
	return r;
  }

/**
 * Gets the nodes for the __ontology__ term __label/strong()__ matching a given predicate.
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
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a collection of semantic nodes.
 */
  public final static Iterable<? extends SemanticNode> filter__label/capitalize()__NodeIterable(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Iterable<? extends SemanticNode> r = node.filter(predicate);
	return r;
  }


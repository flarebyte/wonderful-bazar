/**
* None
* <p>None</p>
 */public class SIOCAccess {public static final Uri PERMISSION = Uri.parse("http://rdfs.org/sioc/access#Permission");

/**
 * Gets the node for the None term <strong>Permission</strong>. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode getPermissionNode(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(PERMISSION);
	return r;
  }

/**
 * Gets the node for the None term <strong>Permission</strong> matching a given locale. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode getPermissionNode(final SemanticNode node, final Locale locale) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(PERMISSION, locale);
	return r;
  }

/**
 * Gets all the nodes for the None term <strong>Permission</strong>.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a collection of semantic nodes.
 */
  public final static Collection<? extends SemanticNode> getPermissionNodeCollection(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Collection<? extends SemanticNode> r = node.get(PERMISSION);
	return r;
  }

/**
 * Gets the node for the None term <strong>Permission</strong> matching a given predicate. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode filterPermissionNode(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.filterFirst(predicate);
	return r;
  }

/**
 * Gets the nodes for the None term <strong>Permission</strong> matching a given predicate.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a collection of semantic nodes.
 */
  public final static Iterable<? extends SemanticNode> filterPermissionNodeIterable(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Iterable<? extends SemanticNode> r = node.filter(predicate);
	return r;
  }

public static final Uri STATUS = Uri.parse("http://rdfs.org/sioc/access#Status");

/**
 * Gets the node for the None term <strong>Status</strong>. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode getStatusNode(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(STATUS);
	return r;
  }

/**
 * Gets the node for the None term <strong>Status</strong> matching a given locale. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode getStatusNode(final SemanticNode node, final Locale locale) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.getFirst(STATUS, locale);
	return r;
  }

/**
 * Gets all the nodes for the None term <strong>Status</strong>.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a collection of semantic nodes.
 */
  public final static Collection<? extends SemanticNode> getStatusNodeCollection(final SemanticNode node) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Collection<? extends SemanticNode> r = node.get(STATUS);
	return r;
  }

/**
 * Gets the node for the None term <strong>Status</strong> matching a given predicate. If there are more than one node, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a semantic node or a null semantic node if no node is matching the term.
 */
  public final static SemanticNode filterStatusNode(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	SemanticNode r = node.filterFirst(predicate);
	return r;
  }

/**
 * Gets the nodes for the None term <strong>Status</strong> matching a given predicate.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>Class</strong>></p>
 * 
 * 
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @param predicate
 *            a predicate to filter the nodes.
 * @return a collection of semantic nodes.
 */
  public final static Iterable<? extends SemanticNode> filterStatusNodeIterable(final SemanticNode node,
	    final Predicate<SemanticNode> predicate) {
	Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
	Iterable<? extends SemanticNode> r = node.filter(predicate);
	return r;
  }

public static final Uri HAS_PERMISSION = Uri.parse("http://rdfs.org/sioc/access#has_permission");

/**
 * Gets the value for the None term <strong>has permission</strong>. If there are more than one value, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Role</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Permission</strong>></p>
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value getHasPermissionValue(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(HAS_PERMISSION);
return r;
}

/**
 * Gets the value for the None term <strong>has permission</strong> matching a given locale. If there are more than one value,
 * just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Role</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Permission</strong>></p>
 * 
 * 
 * @param node
 *            a node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a Value object or null if no value is matching the term and the locale.
 */
public final static Value getHasPermissionValue(final SemanticNode node, final Locale locale) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(HAS_PERMISSION, locale);
return r;
}

/**
 * Gets all the values for the None term <strong>has permission</strong>.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Role</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Permission</strong>></p>
 * 
 * 
 * @param a
 *            node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value[] getHasPermissionValueArray(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
return node.getValueArray(HAS_PERMISSION);
}
public static final Uri HAS_STATUS = Uri.parse("http://rdfs.org/sioc/access#has_status");

/**
 * Gets the value for the None term <strong>has status</strong>. If there are more than one value, just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Item</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Status</strong>></p>
 * 
 * 
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value getHasStatusValue(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(HAS_STATUS);
return r;
}

/**
 * Gets the value for the None term <strong>has status</strong> matching a given locale. If there are more than one value,
 * just returns the first one.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Item</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Status</strong>></p>
 * 
 * 
 * @param node
 *            a node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a Value object or null if no value is matching the term and the locale.
 */
public final static Value getHasStatusValue(final SemanticNode node, final Locale locale) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue(HAS_STATUS, locale);
return r;
}

/**
 * Gets all the values for the None term <strong>has status</strong>.
 * 
 * 
 * 
 * <p>The <em>rdf type</em> is <strong>ObjectProperty</strong>></p>
 * <p>The <em>rdf domain</em> is <strong>Item</strong>></p>
 * <p>The <em>rdf range</em> is <strong>Status</strong>></p>
 * 
 * 
 * @param a
 *            node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value[] getHasStatusValueArray(final SemanticNode node) {
Preconditions.checkNotNull(node, SemanticNode.NODE_SHOULD_NOT_BE_NULL);
return node.getValueArray(HAS_STATUS);
}
}
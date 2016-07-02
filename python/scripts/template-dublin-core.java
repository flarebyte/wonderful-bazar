public static final Uri $CONSTANT$ = Uri.parse("$ABOUT$");

/**
 * Gets the value for the Dublin Core term "$LABEL$". If there are more than one value, just returns the first one.
 * $COMMENT$
 * $DESC$
 * @param node
 *            the node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value get$LABEL$Value(final MultimapSemanticNode node) {
Preconditions.checkNotNull(node, NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue($CONSTANT$);
return r;
}

/**
 * Gets the value for the Dublin Core term "$LABEL$" matching a given locale. If there are more than one value,
 * just returns the first one.
 * $COMMENT$
 * $DESC$
 * @param node
 *            a node to inspect. The node should not be null.
 * @param locale
 *            a locale used as a criteria for filtering the results.
 * @return a Value object or null if no value is matching the term and the locale.
 */
public final static Value get$LABEL$Value(final MultimapSemanticNode node, final Locale locale) {
Preconditions.checkNotNull(node, NODE_SHOULD_NOT_BE_NULL);
Value r = node.getFirstValue($CONSTANT$, locale);
return r;
}

/**
 * Gets all the values for the Dublin Core term "$LABEL$".
 * $COMMENT$
 * $DESC$
 * @param a
 *            node to inspect. The node should not be null.
 * @return a Value object or null if no value is matching the term.
 */
public final static Value[] get$LABEL$ValueArray(final MultimapSemanticNode node) {
Preconditions.checkNotNull(node, NODE_SHOULD_NOT_BE_NULL);
return node.getValueArray($CONSTANT$);
}

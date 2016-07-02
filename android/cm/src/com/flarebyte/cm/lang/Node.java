package com.flarebyte.cm.lang;

import java.util.List;

public interface Node extends Chunkable, Value, ComplexValue {
	public Node addNode(String name);

	public Node copy();

	public Node createNode(String name);

	public List<Node> getChildren();

	public int getLevel();

	public String getName();

	public Node getParent();

	public String getXpath();

	boolean isRoot();

	public Node setName(String name);

	public Node setParent(Node parent);

}

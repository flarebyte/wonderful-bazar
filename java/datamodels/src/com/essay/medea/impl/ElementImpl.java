package com.essay.medea.impl;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.essay.medea.Element;

public class ElementImpl implements Element {
	Element parent=null;
	String text;
	String name;
	boolean is_root=false;
	Map<String, String> attributes = new HashMap<String,String>();
	List<Element> children = new ArrayList<Element>();
	@Override
	public Map<String, String> getAttributes() {
		return attributes;
	}

	public ElementImpl(String name, Element parent, boolean isRoot) {
		super();
		this.name = name;
		this.parent = parent;
		is_root = isRoot;
	}

	@Override
	public List<Element> getChildren() {
		return children;
	}

	@Override
	public Element getParent() {
		return parent;
	}

	@Override
	public String getText() {
		return text;
	}

	@Override
	public boolean isRootElement() {
		return is_root;
	}

	@Override
	public Element setParent(Element parent) {
		this.parent=parent;
		return this;
	}

	@Override
	public Element setText(String text) {
		this.text=text;
		return this;
	}
	
	@Override
	public Element createElement(String name) {
		Element r = new ElementImpl(name,this,false);
		return r;
	}

	@Override
	public Element addElement(String name) {
		Element r = new ElementImpl(name,this,false);
		children.add(r);
		return r;
	}

	@Override
	public String getName() {
		return name;
	}

	@Override
	public Element setName(String name) {
		this.name=name;
		return this;
	}

	@Override
	public Element setAttribute(String key, String value) {
		this.getAttributes().put(key,value);
		return this;
	}

	@Override
	public String getAttrAbout() {
		return attributes.get(ATTRIBUTE_ABOUT);
	}

	@Override
	public String getAttrContent() {
		return attributes.get(ATTRIBUTE_CONTENT);
	}

	@Override
	public String getAttrDatatype() {
		return attributes.get(ATTRIBUTE_DATATYPE);
	}

	@Override
	public String getAttrHref() {
		return attributes.get(ATTRIBUTE_HREF);
	}

	@Override
	public String getAttrId() {
		return attributes.get(ATTRIBUTE_ID);
	}

	@Override
	public String getAttrName() {
		return attributes.get(ATTRIBUTE_NAME);
	}

	@Override
	public String getAttrProperty() {
		return attributes.get(ATTRIBUTE_PROPERTY);
	}

	@Override
	public String getAttrRel() {
		return attributes.get(ATTRIBUTE_REL);
	}

	@Override
	public String getAttrResource() {
		return attributes.get(ATTRIBUTE_RESOURCE);
	}

	@Override
	public String getAttrRev() {
		return attributes.get(ATTRIBUTE_REV);
	}

	@Override
	public String getAttrSrc() {
		return attributes.get(ATTRIBUTE_SRC);
	}

	@Override
	public String getAttrTypeof() {
		return attributes.get(ATTRIBUTE_TYPEOF);
	}

	@Override
	public String getAttrClass() {
		return attributes.get(ATTRIBUTE_CLASS);
	}

	@Override
	public int getLevel() {
		if (this.getParent()==null)return 0;
		int r = this.getParent().getLevel()+1;
		return r;
	}

	@Override
	public String getXpath() {
		if (getParent()==null)return "/"+this.getName();
		String r = getParent().getXpath()+"/"+this.getName();
		return r;
	}


}

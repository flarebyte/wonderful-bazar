package com.essay.medea;

import java.util.List;
import java.util.Map;


public interface Element {
	public final static String ATTRIBUTE_ID="id";
	public final static String ATTRIBUTE_NAME="name";
	public final static String ATTRIBUTE_CLASS="class";
	public final static String ATTRIBUTE_REL="rel";
	public final static String ATTRIBUTE_REV="rev";
	public final static String ATTRIBUTE_CONTENT="content";
	public final static String ATTRIBUTE_HREF="href";
	public final static String ATTRIBUTE_SRC="src";
	public final static String ATTRIBUTE_ABOUT="about";
	public final static String ATTRIBUTE_PROPERTY="property";
	public final static String ATTRIBUTE_RESOURCE="resource";
	public final static String ATTRIBUTE_DATATYPE="datatype";
	public final static String ATTRIBUTE_TYPEOF="typeof";
	public Map<String,String> getAttributes();
	public Element getParent();
	public Element setParent(Element parent);
	public String getText();
	public Element setText(String text);
	public String getName();
	public Element setName(String name);
	public List<Element> getChildren();
	boolean isRootElement(); 
	public Element createElement(String name);
	public Element addElement(String name);
	public String getXpath();
	public int getLevel();
	/*Attributes */
	public Element setAttribute(String key, String value);
	public String getAttrId();
	public String getAttrName();
	public String getAttrClass();
	public String getAttrRel();
	public String getAttrRev();
	public String getAttrContent();
	public String getAttrHref();
	public String getAttrSrc();
	public String getAttrAbout();
	public String getAttrProperty();
	public String getAttrResource();
	public String getAttrDatatype();
	public String getAttrTypeof();
	
	

}

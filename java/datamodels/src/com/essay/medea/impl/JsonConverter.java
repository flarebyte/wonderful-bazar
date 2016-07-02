package com.essay.medea.impl;

import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import com.essay.medea.Converter;
import com.essay.medea.Element;

public class JsonConverter implements Converter {

	@Override
	public Element fromString(String content) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String toString(Element root) {
		JSONArray r = createArray(root);
		return r.toJSONString();
	}
	
	public final static Converter create(){
		Converter r = new JsonConverter();
		return r;
	}
	
	private JSONArray createArray(Element element){
		JSONArray r = new JSONArray();
		r.add(element.getName());
		if (!element.getAttributes().isEmpty()){
			JSONObject attributes = new JSONObject();
			attributes.putAll(element.getAttributes());
			r.add(attributes);
		}
		if (element.getText()!=null){
			r.add(element.getText());
		}
		List<Element> children = element.getChildren();
		for (Element child: children){
			r.add(createArray(child));
		}
		return r;
	}

}

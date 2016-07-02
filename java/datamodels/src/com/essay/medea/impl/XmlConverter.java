package com.essay.medea.impl;

import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Text;

import com.essay.medea.Converter;
import com.essay.medea.Element;

public class XmlConverter implements Converter {
	DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
	TransformerFactory transformerFactory = TransformerFactory.newInstance();
 

	@Override
	public Element fromString(String content) {
		// TODO Auto-generated method stub
		return null;
	}
	
	public final static Converter create(){
		Converter r = new XmlConverter();
		return r;
	}
	@Override
	public String toString(Element root) {
		String r = null;
		try {
			DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
			//root elements
			Document doc = docBuilder.newDocument();
			org.w3c.dom.Element rootElement = createElement(root,doc);
			doc.appendChild(rootElement);
			Transformer transformer = transformerFactory.newTransformer();
			DOMSource source = new DOMSource(doc);
			StreamResult result =  new StreamResult(System.out);
			transformer.transform(source, result);

		} catch (ParserConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (TransformerConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (TransformerException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return r;
	}
	
	private org.w3c.dom.Element createElement(Element element,Document doc){
		org.w3c.dom.Element r = doc.createElement(element.getName());
		Map<String, String> attributes = element.getAttributes();
		Set<String> keys = attributes.keySet();
		for (String key : keys){
			 r.setAttribute(key, attributes.get(key));
		}
			
		if (element.getText()!=null){
			Text text = doc.createTextNode(element.getText());
			r.appendChild(text);
		}
		List<Element> children = element.getChildren();
		for (Element child: children){
			org.w3c.dom.Element xmlchild = createElement(child,doc);
			r.appendChild(xmlchild);
		}
		return r;
	}

}

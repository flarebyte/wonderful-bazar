#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier on 2011-07-24.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import xml.dom.minidom
import re
import string

def main():
	pass


if __name__ == '__main__':
	main()

primaryType = ["BigDecimal","BigInteger","Boolean","Byte","Calendar","Character","Double","Float","Integer","Long","Number","Short","String","Uri","URI","URL","Object"]
DC_NS="http://purl.org/dc/elements/1.1/"
RDF_NS="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS_NS="http://www.w3.org/2000/01/rdf-schema#"
OWL_NS="http://www.w3.org/2002/07/owl#"
SKOS_NS="http://www.w3.org/2004/02/skos/core#"
STATUS_NS="http://www.w3.org/2003/06/sw-vocab-status/ns#"

	
def getAttributeOrElementNS(node, namespace,term):
	r = node.getAttributeNS(namespace,term)
	if r:
		return r
	r = node.getElementsByTagNameNS(namespace,term)
	if r:
		r = r[0].firstChild.data
		return r
	else:
		return None

def getAttributeOfNS(node, ns_element, element, ns_attribute, attribute):
	elem = node.getElementsByTagNameNS(ns_element,element)
	if not elem:
		return None
	r = elem[0].getAttributeNS(ns_attribute,attribute)
	return r

def lastToken(uri):
	if not uri:
		return None
	r = string.replace(uri,"#","/")
	r = string.split(r,"/")
	if len(r)==0:
		return None
	return r[len(r)-1]

def uncurie(uri,base):
	if not uri:
		return None
	if "/" in uri:
		return uri
	return base+uri

def replacePlaceHolder(templ,keyword,value,prefix=""):
	r = templ
	if value:
		r = r.replace("__"+keyword+"__",prefix+value)
		r = r.replace("__"+keyword+"/upper()__",prefix+re.sub("[^A-Za-z0-9]","_",value.upper()))
		r = r.replace("__"+keyword+"/lower()__",prefix+re.sub("[^A-Za-z0-9]","_",value.lower()))
		r = r.replace("__"+keyword+"/capitalize()__",prefix+re.sub("[^A-Za-z0-9]","",string.capwords(value)))
		r = r.replace("__"+keyword+"/p()__","<p>"+prefix+value+"</p>")
		r = r.replace("__"+keyword+"/p()/strong()__","<p>"+prefix+"<strong>"+value+"</strong>></p>")
		r = r.replace("__"+keyword+"/strong()__",prefix+"<strong>"+value+"</strong>")
		r = r.replace("__"+keyword+"/li()__","<li>"+prefix+value+"</li>")
	else:
		r = r.replace("__"+keyword+"__","")
		r = r.replace("__"+keyword+"/upper()__","")
		r = r.replace("__"+keyword+"/lower()__","")
		r = r.replace("__"+keyword+"/capitalize()__","")
		r = r.replace("__"+keyword+"/p()__","")
		r = r.replace("__"+keyword+"/p()/strong()__","")
		r = r.replace("__"+keyword+"/strong()__","")
		r = r.replace("__"+keyword+"/li()__","")
	return r

def replaceStd(templ,desc):
	r = templ
	r = replacePlaceHolder(r,"ontology",desc.ontology)
	r = replacePlaceHolder(r,"about",desc.about)
	r = replacePlaceHolder(r,"label",desc.label)
	r = replacePlaceHolder(r,"comment",desc.comment)
	r = replacePlaceHolder(r,"desc",desc.description)
	r = replacePlaceHolder(r,"example",desc.example, "<em>Examples:</em> ")
	r = replacePlaceHolder(r,"rdftype",desc.rdftype, "The <em>rdf type</em> is ")
	r = replacePlaceHolder(r,"domain",desc.domain, "The <em>rdf domain</em> is ")
	r = replacePlaceHolder(r,"range",desc.rdfrange, "The <em>rdf range</em> is ")
	r = replacePlaceHolder(r,"inverseOf",desc.inverseOf, "This is the <em>OWL inverse</em> of ")
	r = replacePlaceHolder(r,"subPropertyOf",desc.subPropertyOf, "This is a <em>sub property</em> of ")
	return r

class Description:
	def create(self,node,ontology,base):
		self.node = node
		self.ontology = ontology
		self.base=base
		self.about=uncurie(getAttributeOrElementNS(node,RDF_NS,'about'),base)
		self.label=getAttributeOrElementNS(node,RDFS_NS,'label')
		self.comment=getAttributeOrElementNS(node,SKOS_NS,'definition')
		self.description=getAttributeOrElementNS(node,SKOS_NS,'scopeNote')
		self.example=getAttributeOrElementNS(node,SKOS_NS,'example')
		self.rdftype=lastToken(getAttributeOfNS(node,RDF_NS,'type',RDF_NS,'resource'))
		self.domain=lastToken(getAttributeOfNS(node,RDFS_NS,'domain',RDF_NS,'resource'))
		self.rdfrange=lastToken(getAttributeOfNS(node,RDFS_NS,'range',RDF_NS,'resource'))
		self.inverseOf=lastToken(getAttributeOfNS(node,OWL_NS,'inverseOf',RDF_NS,'resource'))
		self.subPropertyOf=lastToken(getAttributeOfNS(node,RDFS_NS,'subPropertyOf',RDF_NS,'resource'))
		self.term_status=getAttributeOrElementNS(node,STATUS_NS,'term_status')

class ClassGenerator:
	def __init__(self, rdfFile,genclassname):
		"""docstring for __init__:		"""
		self.genclassname=genclassname
		self.templateProperty=self.readTemplate("template_property.java")
		self.templateClass=self.readTemplate("template_class.java")
		self.docXml=xml.dom.minidom.parse(rdfFile)
		self.javafile = open ("gen_output.java","w")

	def readTemplate(self,templateFile):
		fin = open (templateFile)
		r = fin.read()
		fin.close()
		return r
	
	def readOntology(self):
		ontology = self.docXml.getElementsByTagNameNS(OWL_NS,'Ontology')
		if not ontology:
			return
		self.title="%s" % (getAttributeOrElementNS(ontology[0],DC_NS,"title"))
		self.description="%s" % (getAttributeOrElementNS(ontology[0],DC_NS,"description"))
		self.ontology_ns=getAttributeOrElementNS(ontology[0],RDF_NS,"about")
	
	def loopOn(self,tagns,tag):
		for node in self.docXml.getElementsByTagNameNS(tagns, tag):
			desc = Description()
			desc.create(node,self.title,self.ontology_ns)
			if not desc.about:
				continue
			if not desc.label:
				continue
			if desc.term_status:
				if desc.term_status != "stable":
					continue
			if desc.rdftype == "Class":
				javacode=replaceStd(self.templateClass,desc)
				self.javafile.write(javacode)
			else:
				javacode=replaceStd(self.templateProperty,desc)
				self.javafile.write(javacode)
		
		
	def generate(self):
		self.readOntology()
		self.javafile.write("/**\n"+"* "+self.title+"\n* <p>"+self.description+"</p>\n */")
		self.javafile.write("public class "+self.genclassname+" {")
		self.loopOn(RDF_NS,'Description')
		self.loopOn(RDFS_NS,'Class')
		self.loopOn(OWL_NS,'Class')
		self.loopOn(RDF_NS,'Property')
		self.javafile.write("}")
			
	
generator = ClassGenerator("sioc_access.rdf","SIOCAccess")
generator.generate()

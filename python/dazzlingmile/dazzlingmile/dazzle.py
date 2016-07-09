from pyDatalog import pyDatalog
from sympy import *
import string
import math
import csv
from collections import defaultdict

fictionFile = 'scene.csv'
MAX_WIDTH = 3872.0
MAX_HEIGHT = 2592.0
UNIT = 16.0

#pyDatalog.create_terms('math')
pyDatalog.create_terms('X', 'Y', 'Z', 'A', 'B', 'C')

class CsvToDatalog(object):
    """docstring for CsvToDatalog"""
    def __init__(self):
        self.statements = []
        self.terms= []

    def create_terms(self,row):
        pred= row[0].replace('-','_')
        self.terms.append(pred)

    def create_statement(self, row):
        subject=row.pop(0) 
        pred= row.pop(0).replace('-','_')
        objs = ["'{}'".format(v) for v in row]
        statement = "+ {pred}('{subject}', {objs})".format(pred=pred, subject=subject, objs=",".join(objs))
        self.statements.append(statement)   

    def load(self):
        print "hi"
        with open(fictionFile, 'rb') as csvfile:
            scenereader = csv.reader(csvfile)
            for row in scenereader:
                isTerm = row[1] == 'child-of-fiction-model'
                if isTerm: 
                    self.create_terms(row)
                else:
                    self.create_statement(row)
        return self.statements

    def asDatacode(self):
        datacode = "\n".join(self.statements)
        print datacode
        return datacode
    
    def asTerms(self):
        allterms = ",".join(set(self.terms))
        #print allterms
        return allterms
 
csvToDatalog = CsvToDatalog()
csvToDatalog.load()
pyDatalog.create_terms(csvToDatalog.asTerms())
pyDatalog.load(csvToDatalog.asDatacode())

pyDatalog.create_terms('SC', 'NAME', 'FRONT', 'HORIZ', 'VERT', 'VP')
#print shapes(SC,NAME,FRONT,HORIZ,VERT,VP)

pyDatalog.create_terms('nextShape','startShape')

shape_brothers = defaultdict(list)
for shape in shapes(SC,NAME,FRONT,HORIZ,VERT,VP).data:
    new_conf = (shape[2],shape[3],shape[4],shape[5])
    shape_brothers[new_conf].append(shape[1])

for shape in shape_brothers.items():
    items = shape[1]
    items.sort()
    + startShape(items[0])
    for i in range(len(items)-1):
        + nextShape(items[i],items[i+1])

pyDatalog.create_terms('START')
startingShape = startShape(START).data[0][0]

pyDatalog.create_terms('SH','SHAPE_TYPE','SHAPE_STYLE','VAR3D','CONF3D')

pyDatalog.create_terms('C3D','CX', 'CY', 'CZ')
pyDatalog.create_terms('V3D','VX', 'VY', 'VZ')

#print var3d(V3D, VX,VY,VZ)

#print conf3d(C3D, CX,CY,CZ)

#print shape3d(SH,SHAPE_TYPE, SHAPE_STYLE, VAR3D, CONF3D)

def headOrNone(value):
    if value is None:
        return None
    else:
        return value[0]

def incSize(oldValue, percentage):
    return float(oldValue) * (1+float(percentage))

def varyShape(prevVar3D, newVar3D):
    px,py,pz = prevVar3D
    nx,ny,nz = newVar3D
    return (incSize(px,nx),incSize(py,ny),incSize(pz,nz))

mainScene = headOrNone(aka(SC, 'main-scene').v())

#Calculate shapes
nShape = startingShape
hasNextShape = True
prevVaryShape = None
while hasNextShape:
    print nShape
    iType, iStyle, iVar3D, iConf3D = shape3d(nShape,SHAPE_TYPE, SHAPE_STYLE, VAR3D, CONF3D).v()
    iFront, iHoriz, iVert, iVp = shapes(mainScene,nShape,FRONT,HORIZ,VERT,VP).v()
    nFront = float(headOrNone(zone2d(iFront,X).v()))
    if prevVaryShape is None:
        prevVaryShape = (nFront*MAX_HEIGHT,nFront*MAX_HEIGHT,nFront*MAX_HEIGHT)
    nVar3D= var3d(iVar3D, VX,VY,VZ).v()
    nConf3D= conf3d(iConf3D, CX,CY,CZ).v()
    nVaryShape = varyShape(prevVaryShape,nVar3D)
    print nVaryShape, nConf3D
    #Next  Shape
    prevVaryShape = nVaryShape
    nShape= headOrNone(nextShape(nShape,SH).v())
    hasNextShape = nShape is not None
 


#!/usr/bin/env python
import os
Butter_1="#fce94f"
Butter_2="#edd400"
Butter_3="#c4a000"
Chameleon_1="#8ae234"
Chameleon_2="#73d216"
Chameleon_3="#4e9a06"
Orange_1="#fcaf3e"
Orange_2="#f57900"
Orange_3="#ce5c00"
Sky_Blue_1="#729fcf"
Sky_Blue_2="#3465a4"
Sky_Blue_3="#204a87"
Plum_1="#ad7fa8"
Plum_2="#75507b"
Plum_3="#5c3566"
Chocolate_1="#e9b96e"
Chocolate_2="#c17d11"
Chocolate_3="#8f5902"
Scarlet_Red_1="#ef2929"
Scarlet_Red_2="#cc0000"
Scarlet_Red_3="#a40000"
Aluminium_1="#eeeeec"
Aluminium_2="#d3d7cf"
Aluminium_3="#babddb6"
Aluminium_4="#888a85"
Aluminium_5="#555753"
Aluminium_6="#2e3436"
Black="#000000"
White="#ffffff"
Transparent=""

def exportToPng(svgpath,width,height,background,exportfolder, crush=False):
	fileList=os.listdir(svgpath)
	for myfile in fileList:
		if(myfile.split(".")[-1] == 'svg'):
			svgfilename=myfile[0:-4]	
			if crush:			
				os.system("inkscape ../"+svgfilename+".svg --export-background="+background+" -w"+str(width)+" -h"+str(height)
				+" --export-png=png/"+exportfolder+"/"+svgfilename+"-"+str(width)+"x"+str(height)+"tmp.png")
				os.system("pngcrush -rem alla -reduce -brute png/"+svgfilename+"-"+str(width)+"x"+str(height)+"tmp.png png/"+svgfilename+"-"+str(width)+"x"+str(height)+".png")
			else:
				if 	background==Transparent:			
					os.system("inkscape ../"+svgfilename+".svg -w"+str(width)+" -h"+str(height)+" --export-png=png/"+exportfolder+"/"+svgfilename+"-"+str(width)+"x"+str(height)+".png")
				else:						
					os.system("inkscape ../"+svgfilename+".svg --export-background="+background+" -w"+str(width)+" -h"+str(height)+" --export-png=png/"+exportfolder+"/"+svgfilename+"-"
					+str(width)+"x"+str(height)+".png")

def convertPngToIco(pngpath,exportfolder):	
	fileList=os.listdir(pngpath)
	for myfile in fileList:
		if(myfile.split(".")[-1] == 'png'):
			pngfilename=myfile[0:-4]	
			os.system("icotool -c -o ico/"+pngfilename+".ico "+ pngpath+"/"+myfile)

#Special logo export
exportToPng("../",105,105,White,"white")
exportToPng("../",16,16,Transparent,"icon")
convertPngToIco("png/icon","ico")



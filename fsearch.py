# -*- coding: utf-8 -*-
#!/usr/bin/env python3

def search_in_source(file, text):
	try:
		file = open(file)
		source = file.read()
		file.close()
		if source.find(text) is not -1: 
			return 1
		else: return -1
	except:
		pass
	
def fsearch(path, search_text, extention, dosdevices=False, PlayOnLinux=False, wine=False):
	import os
	if dosdevices is False: dosdevices = -1 
	elif dosdevices is True:
		dosdevices = 1
	if PlayOnLinux is False: PlayOnLinux = -1 
	elif PlayOnLinux is True:
		PlayOnLinux = 1
	if wine is False: wine = -1 
	elif wine is True:
		wine = 1

	liste = os.listdir(path)

	folder = [str(path+'/'+folder).replace('//','/') for folder in liste if os.path.isdir(path+'/'+folder) is True]

	for f in folder:
		try:
			select = [(f+'/'+select) for select in os.listdir(f) 
					if os.path.isdir(f+'/'+select) is True
					if str(f+'/'+select).find('/dosdevices') is -1
					if str(f+'/'+select).find('/.PlayOnLinux') is -1
					if str(f+'/'+select).find('/PlayOnLinux') is -1
					if str(f+'/'+select).find('/.wine') is -1]

			folder.extend(select)

			for select in select:

				for test in os.listdir(select):
					if str(select+'/'+test)[str(select+'/'+test).find('.'):] in extention.split() and search_in_source(select+'/'+test, search_text) is 1:
						print(select+'/'+test)
		except:
			pass

fsearch('/home', 'search word', '.py .txt', False, False, False)

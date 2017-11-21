# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

def folder_test(path):
	try:
		if len(os.listdir(path)) >= 0: return 1
	except:
		return -1

def text_search(file, text):
	try:
		file = open(file)
		source = file.read()
		file.close()
		if source.find(text) is not -1:
			return 1
	except:
		pass

def ffind(string, fstr):
	if string.find(fstr) is not -1:
		return 1 
	else: 
		return -1

def fsearch(path, search_string, type, dosdevices=False, PlayOnLinux=False, wine=False):
	print('Lütfen bekleyiniz...')
	if dosdevices is False: 
		dosdevices = -1 
	if PlayOnLinux is False: 
		PlayOnLinux = -1
	if wine is False: 
		wine = -1
	dir_list = [path]
	for path in dir_list:
		list = os.listdir(path)
		select = [
				path+'/'+select for select in list 
				if folder_test(path+'/'+select) is 1 if ffind(path, '/dosdevices/') is dosdevices 
				if ffind(path, 'PlayOnLinux') is PlayOnLinux 
				if ffind(path, '/.wine') is wine
														]
		dir_list.extend(select)
		for select in select:
			for beta in os.listdir(select):
				for fextention in type.split():
					if str(select+'/'+beta).find(fextention) is not -1 and text_search(select+'/'+beta, search_string) is 1:
						print (select+'/'+beta)


						
fsearch('/home', 'topla', '.txt .py', False, False, False)

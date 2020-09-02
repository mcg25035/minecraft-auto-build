import os
import random
programid = 0
import logging
inited = False
class core:
	global programid,inited
	def __init__():
		global programid,inited
		if not programid == 0:
			logging.error('The program already initialized.')
			return
		if os.path.isfile(os.getcwd()+'/blocktemp/lockfile'):
			logging.error('Another program using resourse.')
			return
		inited = true
		programid = random.randint(0,2147483647)
		print(os.getcwd())
		os.makedirs(os.getcwd()+'/blocktemp')
		os.chdir(os.getcwd()+'/blocktemp')
		f = open('lockfile','w')
		f.write(programid)
		f.close()
	def blockset(x,y,z,block,data):
		global inited
		if inited == False:
			logging.error('You must initialized the program\nPlease use core()')
			return
		f =

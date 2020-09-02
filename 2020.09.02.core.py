import os
import random
programid = 0
import logging
inited = False
class core:
	global programid,inited
	def __init__(self):
		global programid,inited
		if not programid == 0:
			logging.error('The program already initialized.')
			return
		if os.path.isfile(os.getcwd()+'/blocktemp/lockfile'):
			logging.error('Another program using resourse.')
			return
		inited = True
		programid = random.randint(0,2147483647)
		print(os.getcwd())
		os.makedirs(os.getcwd()+'/blocktemp')
		os.chdir(os.getcwd()+'/blocktemp')
		f = open('lockfile','w')
		f.write(str(programid))
		f.close()
	def blockset(x,y,z,block,data):
		global inited
		if inited == False:
			logging.error('You must initialized the program\nPlease enter core()')
			return
		f = open(str(x)+'_'+str(y)+'_'+str(z),'w+')
		f.write(str(block)+'\n'+str(data))
		f.close()
	def blockget(x,y,z):
		global inited
		if inited == False:
			logging.error('You must initialized the program\nPlease enter core()')
			return
		if not os.path.isfile(str(x)+'_'+str(y)+'_'+str(z)):
			logging.error('Cannot find block,Set block first,enter core.blockget(x,y,z,block,data)')
			return
		f = open(str(x)+'_'+str(y)+'_'+str(z),'r+')
		retur = f.read()
		print(retur)
		f.close()
		return(retur)

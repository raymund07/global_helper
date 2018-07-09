# -*- coding: utf-8 -*-
import pysftp as sftp
import os



port = 22
keyfile_path = None
host='192.168.11.20'
username='images'
password='xepxPU1'
cnopts = sftp.CnOpts()
#cnopts.hostkeys.load('/ru1/images')
cnopts.hostkeys = None 

with sftp.Connection(host='192.168.11.20', username='images' ,password='xepxPU1',cnopts=cnopts,port=22) as s:
    #print (s.listdir('/ru1/images'))
    a=s.listdir('/ru1/images')
    print(len(a))
    print (a)
    for i in s.listdir('/ru1/images'):
        pass
        #print(a)
        #stats=s.listdir_attr()
        #print (i,stats)   
        #os.mkdir('images/{}'.format(i))
      
        
        
    
    #print(s.getcwd())
    #print (s.listdir())
    #s.get_d('/ru1/images/2018-07-09-00-45-01_34322', 'images', preserve_mtime=True)
    #print(s.getcwd())
    


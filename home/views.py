from multiprocessing.connection import Client
import profile
from tkinter import E
from typing import final
from urllib import response
from django.shortcuts import render
from django.contrib import messages
import random
import email
from http import client
import json
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
#import dns
import pymongo
from pymongo import MongoClient
import urllib.parse
import io
from bson import Binary
import base64
#from dns import resolver
from django.contrib import messages
from datetime import datetime
from Crypto.Util.Padding import pad,unpad
from Crypto.Cipher import AES
from .help import forget_pass
#************* AES KEYS 16-BIT *************
KEYSIZE=16
BLOCKSIZE=16
key=b"1236547890123454"
vi=b"1236547890123454"
#*******************************************

#*********************** HOME PAGE *****************************
def first(request):
    return render(request,'final.html')
#***************************************************************


#********************* SIGN UP PAGE ****************************
def index (request):
   
    if (request.method=="POST"):
        username=request.POST.get('user')
        password=request.POST.get('passw')
        #print(password)
        #****************AES ENCRYPT *****
        PASS=password
        c=AES.new(key,AES.MODE_CBC,vi)
        ci=c.encrypt(pad(PASS.encode(),BLOCKSIZE))
        print(ci)
        password=ci
        #*********************************
        email=request.POST.get('email')
        users= {
            
            "username":username,
            "Password": password,
            "Email":email,
            "attemps": 0,
            't1':0

            }
        coll2.insert_many([users])
        return render(request,'final.html')
    return render(request,'signup.html')
#************************************************************************

#******************************** LOGIN PAGE ***************************
def login(request):
    def fnc():
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(dt_string, fmt)
        diff = (d1-i['t1'])
        diff_minutes = diff.seconds/60
        return int(diff_minutes)
    def allset():
        i['attemps']=0
        filter={'username':username}
        newvalue={"$set":{'attemps':i['attemps']}}
        coll2.update_one(filter,newvalue)
        i['t1']=0
        filter={'username':username}
        newvalue2={"$set":{'t1':i['t1']}}
        coll2.update_one(filter,newvalue2)
    if request.method=="POST":
        username=request.POST.get('user')
        passw=request.POST.get('passw')
        mydata=coll2.find({})
        bool1=0
        for i in mydata:
            if(i['username']==username):
                bool1=1
                #**************** AES DECRYPT ********
                ci2=AES.new(key,AES.MODE_CBC,vi)
                PASS2=unpad(ci2.decrypt(i['Password']),BLOCKSIZE)
                passw1=PASS2.decode()
                #*************************************
                if(passw1==passw):
                    if i['attemps']>=5:
                        if fnc()>=60:
                            allset()
                            return render(request,'content.html')
                    else:
                        allset()
                        return render(request,'content.html')
                else:
                    i['attemps']+=1
                    filter={'username':username}
                    newvalue={"$set":{'attemps':i['attemps']}}
                    coll2.update_one(filter,newvalue)
                    if i['attemps']==5:
                        now = datetime.now()
                        # dd/mm/YY H:M:S
                        dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

                        fmt = '%Y-%m-%d %H:%M:%S'
                        d1 = datetime.strptime(dt_string, fmt)
                        i['t1']=d1
                        filter={'username':username}
                        newvalue2={"$set":{'t1':i['t1']}}
                        coll2.update_one(filter,newvalue2)
                    if i['attemps']>=5:
                        if fnc()>=60:
                            allset()
                    messages.info(request, 'Your entered wrong password')
                    return render(request,'finalin.html')
        if(bool1==0):
             messages.info(request, 'Your entered wrong username')
    return render(request,'finalin.html')






"""def login(request):
    def fuc():
        i['f']=0
        filter={'username':username}
        newvalue={"$set":{'f':i['f']}}
        coll2.update_one(filter,newvalue)
        i['attemps']=0
        filter={'username':username}
        newvalue={"$set":{'attemps':i['attemps']}}
        coll2.update_one(filter,newvalue)
        i['t']= 0
        filter={'username':username}
        newvalue2={"$set":{'t':i['t']}}
        coll2.update_one(filter,newvalue2)
    if request.method=="POST":
        username=request.POST.get('user')
        passw=request.POST.get('passw')
        mydata=coll2.find({})
        bool1=0
        for i in mydata:
            if(i['username']==username):
                if((i['Password'])!=passw):
                    #**** UPDATE CODE IN COMPASS*****
                    i['attemps']+=1
                    filter={'username':username}
                    newvalue={"$set":{'attemps':i['attemps']}}
                    coll2.update_one(filter,newvalue)
                    #**********************************
                    if i['attemps']==5:
                        now = datetime.now()
                        i['t']= int(now.strftime("%H%M"))
                        filter={'username':username}
                        newvalue2={"$set":{'t':i['t']}}
                        coll2.update_one(filter,newvalue2)
                    if i['attemps']>=5:
                        i['f']=1
                        filter={'username':username}
                        newvalue={"$set":{'f':i['f']}}
                        coll2.update_one(filter,newvalue)
                        now = datetime.now()
                        t1=int(now.strftime("%H%M"))
                        if abs(t1-i['t'])>=1:
                            print("hai")
                            fuc()
                    messages.info(request, 'Your entered wrong password')
                    return render(request,'finalin.html',)
                else:
                    now = datetime.now()
                    t1=int(now.strftime("%H%M"))
                    print(abs(t1-i['t']))
                    if i['f']==0:
                        print("hai1")
                        fuc()
                        return render(request,'content.html')
                    elif abs(t1-i['t'])>=1:
                        print("hai2")
                        fuc()
                        return render(request,'content.html')
                    else:
                        pass
                        

        #**************************************************************************
                if(i['Password']==passw):
                    return render(request,'content.html')
                else:
                    messages.info(request, 'Your entered wrong password')
                    return render(request,'finalin.html',)
        #***************************************************************************
        if(bool1==0):
             messages.info(request, 'Your entered wrong username')
    return render(request,'finalin.html',)"""


#********************************* MONGODB ATLAS CONECTION  **************************
"""
username = urllib.parse.quote_plus('praveenvenkat2')
password = urllib.parse.quote_plus('praveen3412')
client=pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.c3u1v.mongodb.net/mydatabase?retryWrites=true&w=majority"%(username,password))
"""
#**************************************************************************************
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=client['mydatabase']
coll=db['Fruits']
coll3=db['emojis']
coll2=db['user1']
#**************************** RETRIVE THE DATA FROM MONGO COMPASS **********************
"""arr=[]
#arr1=[]
imageid=[]
imgno=[]
#imageid1=[]
#imgno1=[]
mydata=coll.find({})
#mydata1=coll3.find({})
for i in mydata:
    arr.append(i["str"])
    imageid.append(i["imgid"])
    imgno.append(i['imgno'])"""

"""for i in mydata1:
    arr1.append(i["str"])
    imageid1.append(i["imgid"])
    imgno1.append(i['imgno'])"""


#print(imageid)
# Create your views here.
#*****************************************************************************************


#*********************************** PASS THE IMAGE DATA WITHOUT RELODING USING AJAX**********************
from django.http import HttpResponse
import json

def python_funct(request):
      #do something with the data passed
      if request.method == 'GET':
        param1 = request.GET.get('param_first')
        print(param1)
        arr=[]
        imgno=[]
        coll=db[param1]
        mydata=coll.find({})
        for x in mydata:
            arr.append(x["str"])
            imgno.append(x['imgid'])
        c=list(zip(arr,imgno))
        random.shuffle(c)
        arr,imgno=zip(*c)
      #fullname= 33
      response = {
        'fullname': arr,
        'imgno':imgno,
         }
        
      return JsonResponse(response)
#***************************************************************************************

#print(imgno)
# AES 256 encryption/decryption using pycrypto library
 

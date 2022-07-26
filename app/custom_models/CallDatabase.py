#!/usr/bin/env python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('blood-48be6-firebase-adminsdk-qu8br-a96b64eb95.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()


def insert_record(user_id,record_list):
	data = {
	'姓名': record_list[0],
	'捐血方式': record_list[1],
	'時間': record_list[2],
    }
	collection_ref = db.collection(str(user_id))
	collection_ref.add(data)

	message = f"資料成功匯入囉!"
	
	return message

def leaderboard(user_id,record_list):
    data ={
        '姓名': record_list[0],
        record_list[1]:firestore.Increment(1)
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    blood_ref.update(data)

def read_record(user_id):
    docs = db.collection(str(user_id)).stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        datalist.append(doc.to_dict())
        #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def insert_userlist(user_id,nm,blood,year,gender,place,other):
    data ={
	'暱稱':nm,
	'血型':blood,
	'出生年':year,
	'性別':gender,
    '地區':place,
	'備註':other
	}
    print(user_id)
    collection_ref = db.collection('個人資料').document(str(user_id))
    collection_ref.set(data)

def read_userlist(user_id):
    collection_ref = db.collection('個人資料').document(str(user_id))
    datalist=[]
    docs = collection_ref.get()
    datalist.append(docs.to_dict())
    print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def read_leaderboard():
    docs = db.collection('捐血次數').stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        #docc = doc.to_dict()
        datalist.append(doc.to_dict())
        #datalist.append([docc['姓名'], docc['250cc全血']])
        #print(docc['姓名'])
        #print(docc['250cc全血'])
        print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

def record(user_id,year,way):
    data ={  
	'時間':year,
	'捐血方式':way
	}
    print(user_id)
    collection_ref = db.collection(str(user_id))
    collection_ref.add(data)
    
def r_leaderboard_n(user_id,nm):
    data ={
        '姓名': nm,
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    blood_ref.set(data)

def r_leaderboard(user_id,way):
    data ={
        way:firestore.Increment(1)
    }
    
    blood_ref = db.collection('捐血次數').document(str(user_id))
    blood_ref.update(data)


def r_record(user_id):
    docs = db.collection(str(user_id)).stream()
    datalist=[]
    #docs = collection_ref.get()
    for doc in docs:
        datalist.append(doc.to_dict())
        #print(datalist)
        #datalist = f'{doc.to_dict()}'
    return datalist

import json

mydict_1 = { "brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]} 


mydict_2 = "{ 'brand': 'Ford'," + "'electric': False," +  "'year': 1964," + "'colors': ['red', 'white', 'blue']}"

def SerializaJson(dData,file_path)---> True/False 

    sData = json.dumps(dData)
    try:
        with open(file_path, "w") as myfile:
             myfile.write(sData)
        return True
    except:
        return False
    
def SerializaJson2(dData, file_path):
    try:
        with open(file_path) as myfile:
            myfile.write(sData)
        return True
    except:
        return False
            

def DeserializeJson1(sFilePath):
    try:
        with open(file_path, "w") as myfile:
            json.dump(dData,myfile)
        return True
    except:
        return False
"""   
    sData = ""
    sAppo = ""
    try:
        with open (sFilePath, "r") as myfile:
            sAppo = myfile.read(500)
            while len(sAppo)==500:
                sData += sAppo
                sAppo = mylife.read(500)
            if len (sAppo)> 0:
                sData+= sAppo
        return sData
"""


"""
def DeserializeJson1(sFilePath):
    sData = ""
    sAppo = ""
    dData = {}
    try:
        with open(sFilePath,"r") as myfile:
            sAppo = myfile.read(500)
            while len(sAppo)==500:
                sData += sAppo
                sAppo = myfile.read(500)
            if len(sAppo)> 0:
                sData += sAppo
        if len(sData)>0:
            dData = json.loads(sData)
            return dData
        else:
            return None
    except:
        return None
"""


""""
json.dump(dData,myfile)
"""


mydict_1 = { "brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]} 

bREt = SerializaJson(mydict_1, "./prodotto.json")
print(bREt)
sys.exit()



"""
def DeserializeJson(file_path)--> dict
    json.dump() str1 = json.dumps(mydict_1) 
    json.load dict_1 = json.loads(mydict_2)
"""
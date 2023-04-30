#  IMPORTS .
import requests,json
import hashlib
import subprocess

#  Get you acess , from firebase
class secury_key:
    def __init__(self, data_base:str):
        self.data_base = data_base

    def check_key(self, key:str) -> dict:
        # Load your database
        database = requests.get(f'{self.data_base}auth-keys/.json',verify=True)

        database_data = database.json() # <- Convert your data to json

        user_auth = key
        
        user_registered = 'Key Not Exist'

        user_id = None

        for user in database_data: # Verify if key exist in data-base

            key_registered = database_data[str(user)]['key']
            user_name = database_data[str(user)]['name']
            
            if user_auth == key_registered:
                #print(f'{user_name}:{key_registered}')
                user_registered = database_data[str(user)]['registered']
                if user_registered == '' or user_registered == None:
                    user_registered = 'not_registered'
                    user_id = str(user)
                else:
                    user_registered = 'registered'
                    user_id = str(user)
                break
        
        r = {'registered':user_registered,
             'userid':user_id
             
             }         
        return r
    
    def auth_key(self,name:str) -> bool:
        database = requests.get(f'{self.data_base}/auth-keys/{name}/registered/.json',verify=True)
        database_data = database.json()
        user_hwid = database_data

        serial_number = None
        try:
            result = subprocess.check_output('wmic baseboard get serialnumber', shell=True)
            serial_number = result.decode().split('\n')[1].strip()
        except:
            pass

        #GET CPU ID
        cpu_id = None
        try:
            result = subprocess.check_output('wmic cpu get processorid', shell=True)
            cpu_id = result.decode().split('\n')[1].strip()
        except:
            pass

        
        hwid = ''
        if serial_number:
            hwid += serial_number
        if cpu_id:
            hwid += cpu_id

        #Apply hash MD5
        hashed_hwid = hashlib.md5(hwid.encode()).hexdigest()

        if hashed_hwid == user_hwid:
            return True
        else:
            return False
 
    def register_key(self, name:str) -> bool:
        print(name)
        serial_number = None
        try:
            result = subprocess.check_output('wmic baseboard get serialnumber', shell=True)
            serial_number = result.decode().split('\n')[1].strip()
        except:
            pass

        #GET CPU ID
        cpu_id = None
        try:
            result = subprocess.check_output('wmic cpu get processorid', shell=True)
            cpu_id = result.decode().split('\n')[1].strip()
        except:
            pass

        
        hwid = ''
        if serial_number:
            hwid += serial_number
        if cpu_id:
            hwid += cpu_id

        #Apply hash MD5
        hashed_hwid = hashlib.md5(hwid.encode()).hexdigest()
 
        data = {"registered": hashed_hwid}
        URL = f'{self.data_base}/auth-keys/{name}.json'
        
        print(URL)
        r = requests.patch(url=URL,verify=True,json=data)
        print(r)
        print(r.text)
        

        


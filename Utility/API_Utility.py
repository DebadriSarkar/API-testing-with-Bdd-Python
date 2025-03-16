import json

import requests


class API_Utility:
    data = json.load(open("Resources/config.json"))
    api_url = data["API URL"]
    global response


    def Method_Call(self,table, method, endpoint):
        if method == 'POST':
            uri = self.api_url + endpoint
            payload = {
                "membername": table[0][0],
                "memberemail": table[0][1],
                "membermobile": table[0][2],
                "password": table[0][3],
                "confirmpassword": table[0][4],
                "gender": table[0][5]
            }
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.post(uri,json=payload,headers=headers)
            return response

    def Method_Call_Update(self,table, method, endpoint):
        if method == 'PUT':
            uri = self.api_url + endpoint
            payload = {
                "membername": table[0][0],
                "memberemail": table[0][1],
                "membermobile": table[0][2],
                "password": table[0][3],
                "gender": table[0][4]
            }
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.put(uri, json=payload, headers=headers)
            return response

    def Method_Call_FIND_ALL(self, table, method, endpoint):
        if method == 'GET':
            uri = self.api_url + endpoint
            response = requests.get(uri)
            return response

    def Method_Call_DELETE_BY_ID(self, table, method, endpoint):
        if method == 'DELETE':
            uri = self.api_url + endpoint
            response = requests.delete(uri)
            return response

    def Verify_POST(self, table):
        for row in table:
            status = row['Status']
            message = row['Message']
            return status, message


    def Verify_PUT(self, table):
        for row in table:
            status = row['Status']
            message = row['Message']
            return status, message

    def Verify_GET(self,table):
        for row in table:
            status = row['Status']
            message = row['Message']
            return status, message

    def Verify_DELETE(self,table):
        for row in table:
            status = row['Status']
            message = row['Message']
            return status, message
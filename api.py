from datetime import datetime
import os
import json
import requests
import csv

class Api:
    api_url = "https://qa-interview-test.splytech.dev/api"
    path, dirs, files = next(os.walk("./template")) 
    logFile = './log/LOG_{datetime}.txt'.format(datetime=datetime.now().strftime("%Y%m%d_%H%M%S"))
    
    def __init__(self):
        # INITIAL SETTING
        now = datetime.now()
        self.current_time = now.strftime("%H-%M-%S")
               
    
    def createRecord(self, endpoint, body):
        headers = {'Content-Type': 'application/json'}
        url = "{api_url}/{endpoint}".format(api_url=self.api_url, endpoint=endpoint)
        payload = json.dumps(body)
        response = requests.request("POST", url, headers=headers, data=payload)
        status = response.status_code

        return status, self.decode_and_parse_response(response)
    
    
    def getRecord(self, endpoint, itemId):
        headers = {}
        payload = {}
        url = "{api_url}/{endpoint}/{itemId}".format(api_url=self.api_url, endpoint=endpoint, itemId=itemId)
        response = requests.request("GET", url, headers=headers, data=payload)
        status = response.status_code

        return status, self.decode_and_parse_response(response)
      
    
    def extractTemplate(self):
        reader = csv.reader(open('{path}/{file}'.format(path=self.path, file=str(self.files[0])), 'r'))
        result = {}

        for index, item in enumerate(reader, start=0):
            if index == 0:
                header = item
                continue
            for indCol, col in enumerate(header):
                result.setdefault(col, []).append(item[indCol])
        
        return result
    
    
    @staticmethod
    def decode_and_parse_response(response):
        json_data = response.text.encode('utf8')
        parsed_json = (json.loads(json_data))
        
        return parsed_json
    
    
# def main():
#     client = Api()


# if __name__ == "__main__":
#     main()

import json
import logging
import os
import sys
from pathlib import Path
from datetime import date, datetime
from bodyJson import BodyJson
from api import Api


def apiTest():
    fromCsv = api.extractTemplate()
    csvHeader = list(fromCsv.keys())
    for i in range(0,len(fromCsv['testId'])):
        row = []
        for item in csvHeader:
            row.append(fromCsv[item][i])
        body = jsonBody.createRecord(csvHeader, row)
        status, response = api.createRecord('journeys', body)
        

        if status >=251 :
            logging.info("{status} No Data Recorded, {Test}, {Desc}, ===>, {message}, {error}"\
                .format(status=status, Test=fromCsv['testName'][i], Desc=fromCsv['testDescription'][i], message=response["message"], error=response["info"]))
        else:
            recordId = response["_id"]
            statusLoaded, loadedRecord = api.getRecord('journeys', str(recordId))
            logging.info("{status} Data Succesfully Recorded, {Test}, {Desc}".format(status=statusLoaded, Test=fromCsv['testName'][i], Desc=fromCsv['testDescription'][i]))
            logging.info("Get Record:\n {data}".format(data=json.dumps(loadedRecord, indent= 4)))
    
    print("TEST COMPLETED!!!")
  
if __name__ == '__main__':
    print("TEST STARTS.....")
    api = Api()
    jsonBody = BodyJson()
    if not os.path.exists(os.path.dirname(api.logFile)):
        os.makedirs(os.path.dirname(api.logFile))
    logging.basicConfig(filename=api.logFile, format='%(asctime)s %(levelname)-s %(message)s', datefmt='%a %d-%b-%Y %H:%M:%S', level=logging.INFO, force=False)
    apiTest()
import time
import sys
import datetime
import json
import numpy
import io
import os

# Get sensors' data from Pi and send it to the app

def run(day, start, end):
    now = datetime.datetime.now()
    file = '/sensor_data/' + now.year + now.month + now.day + '/' + now.year + '-' + now.month + '-' + now.day

    if not file.isfile():
    #return no data
    else:
        #check if there is reading error
        errorfile = file+'/error_log'
        if os.path.isfile(errorfile):
            error = json.load(errorfile, 'r')
            time = error['tempSensor']['time']
            if datetime.datetime.utcnow().isoformat() - time < 5:
                return -1
            else:
                # delete error file

        data = json.load(file, 'r')
        count = data['count']

        for i in range(200):
            #format json string to return

    return


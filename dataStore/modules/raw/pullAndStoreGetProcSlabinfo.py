__author__ = "<programmerli@foxmail.com>"
__copyright__ = "Licensed under GPLv2 or later."

from dataStore.lepdClient.LepdClient import LepdClient
from dataStore.influxDbUtil.dbUtil import MyInfluxDbClient

import time

'''
fetch data related to  GetProcSlabinfo from lepd by lepdClient and 
store the returned data into the influxDB by influxDBClient.
'''
def pullAndStoreGetProcSlabinfo(lepdClient, influxDbClient):
    res = lepdClient.sendRequest('GetProcSlabinfo')
    # print(res)
    # str1 = res["result"].split("\n")
    # for x in str1:
    #     print(x)
    json_body = [
        {
            "measurement": "GetProcSlabinfo",
            "tags": {
                # the address of lepd
                "server": lepdClient.server
            },
            # "time": "2017-03-12T22:00:00Z",
            "fields": {
                "slabinfo": res["result"]

            }
        }
    ]

    influxDbClient.write_points(json_body)



if (__name__ == '__main__'):
    lepdClient = LepdClient('localhost')
    influxDbClient = MyInfluxDbClient('localhost')
    for i in range(1):
        pullAndStoreGetProcSlabinfo(lepdClient, influxDbClient)
        time.sleep(1)

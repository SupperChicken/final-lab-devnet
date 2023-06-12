import requests
import json

requests.packages.urllib3.disable_warnings()
baseUrl = "https://api.meraki.com/api/v1"
API_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "681155"

def get_org_inv():
    url = baseUrl + "/organizations/{}/inventory/devices".format(org_id)
    
    header = {
    "Content-Type" : "application/json",
    "Accept" : "application/json",
    "X-Cisco-Meraki-API-Key" : API_key 
    }

    respone = requests.get(url,headers=header)

    data_inv =respone.json()

    parse_data_inv =json.dumps(data_inv, indent=4)

    print("cau_b:")
    print(parse_data_inv)
    print("-----------")


    print("cau_c:")
    deviceid_null = []
    for i in data_inv:
        if i["networkId"] == None:
            deviceid_null.append(i)
    print(json.dumps(deviceid_null, indent=4))
    print ("-------")


if __name__ == "__main__":
        get_org_inv()
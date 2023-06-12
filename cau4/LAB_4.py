import requests
import json
requests.packages.urllib3.disable_warnings()
baseUrl = "https://api.meraki.com/api/v1"
API_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "681155"
def get_org():
    url = baseUrl + f"/organizations/{org_id}/inventory/devices"
    header = {
        "X-Cisco-Meraki-API-Key" : API_key
    }
    response= requests.get(url,headers=header,verify=False)
    data=response.json()
    parse_data=json.dumps(data,indent=4)
    print(parse_data)
    # for i in data:
    #     id_org=i["id"]
    #     print(id_org)
if __name__ == "__main__":
    get_org()
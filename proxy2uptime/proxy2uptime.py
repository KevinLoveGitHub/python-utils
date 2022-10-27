#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import yaml
import json
import requests


def start(value):
    # send http request

    # url = "https://api.huacloud.xyz/sub?target=clash&insert=true&emoji=true&udp=true&clash.doh=true&new_name=true&filename=Flower_SS&url=https%3A%2F%2Fapi.flowercloud.xyz%2Fosubscribe.php%3Fsid%3D17074%26token%3DBSke57QTJy4i%26sip002%3D1"
    # payload = {}
    # headers = {}
    # response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    # data = yaml.safe_load(response.text)

    file = value['file']

    with open(file, 'r') as f:
        data = yaml.safe_load(f)

    # 判断proxies是否存在
    if 'proxies' in data:
        proxies = data['proxies']
    else:
        print("proxies not found")
        return

    # 文件存在
    read_file = "original.json"
    if os.path.exists("temp.json"):
        read_file = "temp.json"
    # 读取backup.json, 然后追加到文件backup.json
    with open(read_file, 'r') as f:
        data = json.loads(f.read())

    # last_item_id = data['monitorList'][-1]['id']
    monitors = []
    pre_name = ""
    interval = 3600
    for proxy in proxies:
        name = proxy['name']
        server = proxy['server']
        port = proxy['port']
        # name 不包含Traffic和Expire
        exclude_names = ["TRAFFIC", "EXPIRE", "官网", "IPV6接入", "ASYNCHRONOUS"]
        if any(exclude_name in name.upper() for exclude_name in exclude_names):
            continue

        split = name.split(" ")
        tmp_name = None
        if len(split) > 2:
            tmp_name = split[0] + " " + split[1]

        if tmp_name is None or pre_name == tmp_name:
            continue

        pre_name = tmp_name
        print(name + ":" + pre_name)

        # last_item_id = last_item_id + 1
        monitors.append({
            # "id": last_item_id,
            "name": name,
            "url": "https://",
            "method": "GET",
            "hostname": server,
            "port": port,
            "maxretries": 0,
            "weight": 2000,
            "active": 1,
            "type": "port",
            "interval": interval,
            "retryInterval": interval,
            "resendInterval": 0,
            "keyword": None,
            "expiryNotification": False,
            "ignoreTls": False,
            "upsideDown": False,
            "maxredirects": 10,
            "accepted_statuscodes": [
                "200-299"
            ],
            "dns_resolve_type": "A",
            "dns_resolve_server": "1.1.1.1",
            "dns_last_result": None,
            "pushToken": None,
            "docker_container": "",
            "docker_host": None,
            "proxyId": None,
            "notificationIDList": {
                "1": True
            },
            "tags": [],
            "mqttUsername": "",
            "mqttPassword": "",
            "mqttTopic": "",
            "mqttSuccessMessage": "",
            "databaseConnectionString": None,
            "databaseQuery": None,
            "authMethod": None,
            "authWorkstation": None,
            "authDomain": None,
            "radiusUsername": None,
            "radiusPassword": None,
            "radiusCalledStationId": None,
            "radiusCallingStationId": None,
            "radiusSecret": None,
            "headers": None,
            "body": None,
            "basic_auth_user": None,
            "basic_auth_pass": None
        })

    print(len(monitors))
    # 写入文件
    data['monitorList'].extend(monitors)
    with open('temp.json', 'w') as f:
        f.write(json.dumps(data))


if __name__ == '__main__':
    # 创建数组
    # proxys = [{
    #     "name": "ssrcloud",
    #     "file": "薯条.yaml",
    #     "tag": "ssrcloud"
    # }, {
    #     "name": "flower",
    #     "file": "花云.yaml",
    #     "tag": "flower"
    # }]

    proxys = [{
        "name": "proxy",
        "file": "proxy.yaml",
    }]

    for value in proxys:
        start(value)

    os.rename('temp.json', 'result.json')

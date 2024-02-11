def call_message(msg):
    import json
    import datetime
    #print(f"---\nexample(1) receive: {msg}")
    msgJson = json.loads(msg)
    if msgJson.get('productKey') is not None:
        productKey = msgJson.get('productKey')
        if msgJson.get("devId") is not None:
            devId = msgJson.get("devId")
        if (productKey == "qgwcxxws"):  # switch
            if ( msgJson.get("status")):
                statusJson = msgJson.get("status")
                print(datetime.datetime.now(), "//", devId, statusJson[0])


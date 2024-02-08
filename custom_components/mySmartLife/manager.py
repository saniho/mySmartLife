def call_message(msg):
    import json
    import datetime
    #print(f"---\nexample(1) receive: {msg}")
    msgJson = json.loads(msg)
    if msgJson.get('productKey') is not None:
        productKey = msgJson.get('productKey')
        if (productKey == "qgwcxxws"):  # switch
            print("oupi")
            if ( msgJson.get("status")):
                statusJson = msgJson.get("status")
                print(datetime.datetime.now())
                print(statusJson[0])


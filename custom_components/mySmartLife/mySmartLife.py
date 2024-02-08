import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessID, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint

    def call_message(msg):
        import json
        print(f"---\nexample(1) receive: {msg}")
        msgJson = json.loads(msg)
        if msgJson.get('productKey') is not None:
            productKey = msgJson.get('productKey')
            if ( productKey == "qgwcxxws"): # switch
                print("oupi")

    def subscribe(self):
        open_pulsar = TuyaOpenPulsar(
            self._access_id, self._acces_key, self._mqEndPoint, TuyaCloudPulsarTopic.PROD
        )
        # Add Message Queue listener
        open_pulsar.add_message_listener(call_message)

        # Start Message Queue
        open_pulsar.start()

    def unsubcribe(self):
        open_pulsar.stop()
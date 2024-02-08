import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessID, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint


    def subscribe(self, functionName):

        self.open_pulsar = TuyaOpenPulsar(
            self._access_id, self._acces_key, self._mqEndPoint, TuyaCloudPulsarTopic.PROD
        )
        # Add Message Queue listener
        self.open_pulsar.add_message_listener(functionName)

        # Start Message Queue
        self.open_pulsar.start()
        print("start listen")

    def unsubcribe(self):
        self.open_pulsar.stop()
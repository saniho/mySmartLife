import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessId, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint

    def subscribe(self):
        open_pulsar = TuyaOpenPulsar(
            ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
        )
        # Add Message Queue listener
        open_pulsar.add_message_listener(call_message)

        # Start Message Queue
        open_pulsar.start()

    def unsubcribe(self):
        open_pulsar.stop()
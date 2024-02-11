import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic

_LOGGER = logging.getLogger(__name__)
# Définir la classe de traitement des messages
class MessageHandler:
    def __init__(self, obj):
        self.obj = obj

    def on_message(self, message):
        # Accéder à l'objet passé à la fonction lambda
        _LOGGER.debug(f"Objet : {self.obj}")

        # Traiter le message
        _LOGGER.debug(f"Message reçu : {message.data}")

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessID, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint


    def subscribe(self, obj):

        self.open_pulsar = TuyaOpenPulsar(
            self._access_id, self._acces_key, self._mqEndPoint, TuyaCloudPulsarTopic.PROD
        )
        # Add Message Queue listener
        #self.open_pulsar.add_message_listener(functionName)
        self.open_pulsar.add_message_listener(lambda message: MessageHandler(obj).on_message(message))

        # Start Message Queue
        self.open_pulsar.start()
        _LOGGER.debug("start listen")

    def unsubcribe(self):
        self.open_pulsar.stop()
import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic
from custom_components.mySmartLife import myEntitySmartLife
import homeassistant.helpers.service as service_helper

_LOGGER = logging.getLogger(__name__)
# Définir la classe de traitement des messages
class MessageHandler:
    def __init__(self, obj):
        self.obj = obj

    def on_message(self, msg):
        import json, datetime
        # Accéder à l'objet passé à la fonction lambda
        _LOGGER.debug(f"Objet : {self.obj}")

        # Traiter le message
        _LOGGER.debug(f"Message reçu : {msg}")
        msgJson = json.loads(msg)
        if msgJson.get('productKey') is not None:
            productKey = msgJson.get('productKey')
            if msgJson.get("devId") is not None:
                devId = msgJson.get("devId")
                if (productKey == "qgwcxxws"):  # switch
                    if ( msgJson.get("status")):
                        statusJson = msgJson.get("status")
                        _LOGGER.debug( "status : %s / %s / %s" %(datetime.datetime.now(), devId, statusJson[0]))
                        code = statusJson[0]["code"]
                        sensorName = "%s.%s"%(devId, code)
                        value = statusJson[0]["value"]
                        if sensorName not in self.obj['listSensors'].keys():
                            myEntity = myEntitySmartLife.myEntitySmartLife( sensorName, value)
                            self.obj['addEntities']([myEntity])
                            self.obj['listSensors'][sensorName] = myEntity
                        else:
                            self.obj['listSensors'][ sensorName ]._changeData(value)
                            self.obj['listSensors'][ sensorName ]._update()
                        # reset pour bouton Click / Double_clik
                        if ( code in ['switch_mode1'] ):
                            self.obj['listSensors'][sensorName]._resetDataCall()

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessID, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint


    def subscribe(self, listSensors, hass, objAddEntities):

        self.open_pulsar = TuyaOpenPulsar(
            self._access_id, self._acces_key, self._mqEndPoint, TuyaCloudPulsarTopic.PROD
        )
        # Add Message Queue listener
        obj = {}
        obj['listSensors']= {}
        obj['hass']=hass
        obj['addEntities']=objAddEntities
        self.open_pulsar.add_message_listener(lambda message: MessageHandler(obj).on_message(message))

        # Start Message Queue
        self.open_pulsar.start()
        _LOGGER.debug("start listen")

    def unsubcribe(self):
        self.open_pulsar.stop()
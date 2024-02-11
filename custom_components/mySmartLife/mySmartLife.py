import logging
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic
from custom_components.mySmartLife import myEntitySmartLife
import homeassistant.helpers.service as service_helper

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(10)
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
                        sensorName = "%s.%s"%(devId, statusJson[0]["code"])
                        value = statusJson[0]["value"]
                        _LOGGER.debug( "entite deja connue ?")
                        if sensorName not in self.obj['listSensors']:
                            #self.obj['addEntities']() with data message
                            _LOGGER.debug( "added" )
                            myEntity = myEntitySmartLife.myEntitySmartLife( sensorName, value)
                            _LOGGER.debug( "myEntity created, ajout à  %s" %self.obj['addEntities'] )


                            # mettre dans l'obj l'instance de l'entite pour appeler l'update en directe ensuite !!
                            self.obj['addEntities']([myEntity])
                            _LOGGER.debug( "myEntity add_entities ok" )
                            self.obj['listSensors'].append( sensorName )
                        else:
                            #send notification update with message !!
                            _LOGGER.debug( "send notification" )
                            hass = self.obj['hass']
                            _LOGGER.debug( "send notification 1" )
                            data = {"param": value}
                            theSensorName = "mySmartLife.%s"
                            _LOGGER.debug( "theSensorName send notification 2 %s"%theSensorName )
                            theSensorName = "mySmartLife.bfc185d3e2bd3cbc39bscy.switch_mode1"
                            entity_manager = hass.data.get(theSensorName)
                            _LOGGER.debug( "entity_manager send notification 2 %s"%entity_manager )
                            _LOGGER.debug( "send notification 3" )
                            _LOGGER.debug( "hass send notification 2 %s"%hass )
                            _LOGGER.debug( "send notification 3" )
                            _LOGGER.debug( "service_helper send notification 4 %s"%service_helper )
                            _LOGGER.debug( "send notification 5" )
                            service_helper.call_service(hass, "homeassistant", "update_entity",
                                                        {"entity_id": theSensorName})
                            _LOGGER.debug( "send notification ok " )
                            pass
                        #_LOGGER.debug( "sensorName: %s" %(sensorName))

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
        obj['listSensors']=[]
        obj['hass']=hass
        obj['addEntities']=objAddEntities
        self.open_pulsar.add_message_listener(lambda message: MessageHandler(obj).on_message(message))

        # Start Message Queue
        self.open_pulsar.start()
        _LOGGER.debug("start listen")

    def unsubcribe(self):
        self.open_pulsar.stop()
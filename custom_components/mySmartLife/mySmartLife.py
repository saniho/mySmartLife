import logging
from homeassistant.helpers import entity_registry as er
from tuya_connector import TUYA_LOGGER, TuyaOpenPulsar, TuyaCloudPulsarTopic
from .myEntitySmartLife import myEntitySmartLife

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
        #print(f"Message reçu : {msg}")
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
                            _LOGGER.debug( "creation myEntitySmartLife")
                            myEntity = myEntitySmartLife( sensorName, value)
                            _LOGGER.debug( "add myEntitySmartLife")
                            try:
                                self.obj['hass'].add_entity(myEntity)
                            except Exception as e:
                                # Gérer l'erreur
                                _LOGGER.debug("add myEntitySmartLife ... erreur")
                                _LOGGER.debug(f"Type d'erreur : {type(e)}")
                                _LOGGER.debug(f"Message d'erreur : {e}")
                            #self.obj['hass'].services.call("sensor", "add_entity", {"entity_id": myEntity.unique_id})
                            #self.obj['addEntities']([myEntity]) # fait planter !!!!
                            _LOGGER.debug( "fin myEntitySmartLife")
                            #self.obj['listSensors'][sensorName] = myEntity
                        else:
                            self.obj['listSensors'][ sensorName ]._changeData(value)
                            self.obj['listSensors'][ sensorName ]._update()
                        # reset pour bouton Click / Double_clik
                        if ( code in ['switch_mode1'] ):
                            self.obj['listSensors'][sensorName]._resetDataCall()
                elif (productKey == "vlzqwckk"):  # thermometre
                    ## TD : gestion objet generique + gestion unité des mesure
                    if ( msgJson.get("status")):
                        statusJson = msgJson.get("status")
                        _LOGGER.debug( "status : %s / %s / %s" %(datetime.datetime.now(), devId, statusJson[0]))
                        code = statusJson[0]["code"]
                        sensorName = "%s.%s"%(devId, code)
                        value = statusJson[0]["value"]
                        if sensorName not in self.obj['listSensors'].keys():
                            myEntity = myEntitySmartLife( sensorName, value)
                            self.obj['addEntities']([myEntity])
                            self.obj['listSensors'][sensorName] = myEntity
                        else:
                            self.obj['listSensors'][ sensorName ]._changeData(value)
                            self.obj['listSensors'][ sensorName ]._update()
                elif (productKey == "g2y6z3p3ja2qhyav"):  # thermometre
                    ## TD : gestion objet generique + gestion unité des mesure
                    if ( msgJson.get("status")):
                        statusJson = msgJson.get("status")
                        _LOGGER.debug( "status : %s / %s / %s" %(datetime.datetime.now(), devId, statusJson[0]))
                        code = statusJson[0]["code"]
                        sensorName = "%s.%s"%(devId, code)
                        value = statusJson[0]["value"]
                        if sensorName not in self.obj['listSensors'].keys():
                            myEntity = myEntitySmartLife( sensorName, value)
                            self.obj['addEntities']([myEntity])
                            self.obj['listSensors'][sensorName] = myEntity
                        else:
                            self.obj['listSensors'][ sensorName ]._changeData(value)
                            self.obj['listSensors'][ sensorName ]._update()

class mySmartLife:
    def __init__(self):
        pass

    def setConfig(self, accessID, accessKey, mqEndPoint):
        self._access_id = accessID
        self._acces_key = accessKey
        self._mqEndPoint = mqEndPoint


    def subscribe(self, listSensors, hass, objAddEntities, prod = True):

        _LOGGER.debug("create TuyaOpenPulsar")
        if prod:
            topic = TuyaCloudPulsarTopic.PROD
        else:
            topic = TuyaCloudPulsarTopic.TEST
        self.open_pulsar = TuyaOpenPulsar(
            self._access_id, self._acces_key, self._mqEndPoint, topic
        )
        _LOGGER.debug("Add Message Queue listener")
        # Add Message Queue listener
        self.obj = {}
        self.obj['listSensors']= {}
        self.obj['hass']=hass
        self.obj['addEntities']=objAddEntities
        #_LOGGER.debug("add_message_listener")
        #self.open_pulsar.add_message_listener(lambda message: MessageHandler(self.obj).on_message(message))

        # Start Message Queue
        self.open_pulsar.start()
        _LOGGER.debug("start listen")

    def addlistener(self):
        _LOGGER.debug("add_message_listener")
        self.open_pulsar.add_message_listener(lambda message: MessageHandler(self.obj).on_message(message))

    def getTuya(self):
        return self.open_pulsar

    def unsubcribe(self):
        self.open_pulsar.stop()
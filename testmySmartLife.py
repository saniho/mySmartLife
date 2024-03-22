def testMySmartLife():
  from custom_components.mySmartLife import mySmartLife

  _mySmartLife = mySmartLife.mySmartLife()

  import configparser
  mon_conteneur = configparser.ConfigParser()
  mon_conteneur.read("../myCredential/security.txt")
  accessId = mon_conteneur["SMARTLIFE"]['ACCESS_ID']
  accessKey = mon_conteneur["SMARTLIFE"]['ACCESS_KEY']
  mqEndPoint = mon_conteneur["SMARTLIFE"]['MQ_ENDPOINT']
  _mySmartLife.setConfig( accessId, accessKey, mqEndPoint )
  listSensors = []
  hass = "Mon hass"
  obj = "Mon objet"
  _mySmartLife.subscribe(listSensors, hass, objAddEntities = obj, prod=True)

testMySmartLife()
def testMySmartLife():
  from custom_components.mySmartLife import mySmartLife, sensorMySmartLife
  from custom_components.mySmartLife.manager import call_message

  _mySmartLife = mySmartLife.mySmartLife()

  import configparser
  mon_conteneur = configparser.ConfigParser()
  mon_conteneur.read("../myCredential/security.txt")
  accessId = mon_conteneur["SMARTLIFE"]['ACCESS_ID']
  accessKey = mon_conteneur["SMARTLIFE"]['ACCESS_KEY']
  mqEndPoint = mon_conteneur["SMARTLIFE"]['MQ_ENDPOINT']
  _mySmartLife.setConfig( accessId, accessKey, mqEndPoint )
  _mySmartLife.subscribe(call_message)


testMySmartLife()
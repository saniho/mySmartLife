def testMySmartLife():
  from custom_components.mySmartLife import mySmartLife, sensorMySmartLife

  _mySmartLife = mySmartLife.mySmartLife()

  import configparser
  mon_conteneur = configparser.ConfigParser()
  mon_conteneur.read("../myCredential/security.txt")
  print( mon_conteneur.keys)
  accessId = mon_conteneur["SMARTLIFE"]['ACCESS_ID']
  accessKey = mon_conteneur["SMARTLIFE"]['ACCESS_KEY']
  mqEndPoint = mon_conteneur["SMARTLIFE"]['MQ_ENDPOINT']
  _mySmartLife.setConfig( accessId, accessKey, mqEndPoint )
  _mySmartLife.subscribe()

  print(1/0)


  print(_mySmartLife.getMoney())
  sAM = sensorMySmartLife.manageSensorState()
  sAM.init(_mySmartLife )
  state, attributes = sAM.getstatusMoney()
  sensorMySmartLife.logSensorState( attributes )
  state, attributes = sAM.getstatusTotalMoney()
  sensorMySmartLife.logSensorState( attributes )
  state, attributes = sAM.getstatusData()
  sensorMySmartLife.logSensorState( attributes )


testMySmartLife()
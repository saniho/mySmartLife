# mySmartLife

J'en avait marre de ne pas arriver à gerer facilement mes deux boutons Zigbee, 

le click, le double_click n'arrivait pas au bon moment, et impossible de déclencher des automations.

Donc voici une petite contribution pour gerer cela.

Pour le moment, la gestion uniquement possible via le fichier yaml, mais plus tard, 

il sera possible de le faire via les ecrans de configs

config yaml
```
- platform: mySmartLife
  ACCESS_ID: xxx
  ACCESS_KEY: xxx
  MQ_ENDPOINT: wss://mqe.tuyaeu.com:8285/
```
MQ_ENDPOINT : si votre tuya utilise le datacenter europeen

![](img/token.png)
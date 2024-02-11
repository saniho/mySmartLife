"""Sensor for my first"""
import logging
from collections import defaultdict
from datetime import timedelta, datetime

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_TOKEN,
    CONF_NAME,
    ATTR_ATTRIBUTION,
    CONF_SCAN_INTERVAL,
)

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.util import slugify
from homeassistant.util.dt import now, parse_date


from .const import (
    DOMAIN,
    __VERSION__,
    __name__,
)

_LOGGER = logging.getLogger(__name__)
DOMAIN = "saniho"
ICON = "mdi:package-variant-closed"
SCAN_INTERVAL = timedelta(seconds=1800)
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_TOKEN): cv.string,
    }
)

from . import mySmartLife

_LOGGER.setLevel(10)
_mySmartLife = mySmartLife.mySmartLife()
listSensors = []

def call_message(msg):
    import json
    import datetime
    #print(f"---\nexample(1) receive: {msg}")
    msgJson = json.loads(msg)
    if msgJson.get('productKey') is not None:
        productKey = msgJson.get('productKey')
        if msgJson.get("devId") is not None:
            devId = msgJson.get("devId")
        if (productKey == "qgwcxxws"):  # switch
            if ( msgJson.get("status")):
                statusJson = msgJson.get("status")
                _LOGGER.debug( "%s %s"%(devId, statusJson[0]))
                sensorName = "%s %s"%(devId, statusJson[0]["switch_mode1"])
                #if ( sensorName ) not in listSensors:
                #    add_entities([infoSensor_qgwcxxws(session, sensorName)], True)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the platform."""
    name = config.get(CONF_NAME)

    accessId = "tkpy8gyab2mgidrn9wky"
    accessKey = "9d1862bb04ea49f4a9eccb81742c3d8d"
    mqEndPoint = "wss://mqe.tuyaeu.com:8285/"
    _mySmartLife.setConfig(accessId, accessKey, mqEndPoint)

    obj = "Mon objet"
    _mySmartLife.subscribe(obj)


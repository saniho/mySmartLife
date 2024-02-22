"""Sensor for my first"""
import logging
from collections import defaultdict
from datetime import timedelta, datetime

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
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
    PLATFORMS,
    __VERSION__,
    __name__,
    CONF_ID,
    CONF_KEY,
    CONF_ENDPOINTKEY,
)

_LOGGER = logging.getLogger(__name__)
ICON = "mdi:package-variant-closed"
SCAN_INTERVAL = timedelta(seconds=1800)
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_ID): cv.string,
        vol.Required(CONF_KEY): cv.string,
        vol.Required(CONF_ENDPOINTKEY): cv.string,
    }
)

from .mySmartLife import mySmartLife

_mySmartLife = mySmartLife()
listSensors = []

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the platform."""
    _LOGGER.info(f"setup_platform")
    name = config.get(CONF_NAME)

    accessId = config.get(CONF_ID)
    accessKey = config.get(CONF_KEY)
    mqEndPoint = config.get(CONF_ENDPOINTKEY)
    _mySmartLife.setConfig(accessId, accessKey, mqEndPoint)

    _mySmartLife.subscribe(listSensors, hass, add_entities)
    _LOGGER.info(f"setup_platform end")


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up the mySmartLife sensor platform."""

    _LOGGER.info(f"async_setup_entry")
    entities = []
    async_add_entities(
        entities,
        False,
    )
    _LOGGER.info(f"async_setup_entry end ")
    _LOGGER.info(f"setup_platform 2 {entry}")
    _LOGGER.info(f"setup_platform 2 data {entry.data}")

    accessId = entry.data.get(CONF_ID)
    accessKey = entry.data.get(CONF_KEY)
    mqEndPoint = entry.data.get(CONF_ENDPOINTKEY)
    _mySmartLife.setConfig(accessId, accessKey, mqEndPoint)

    _mySmartLife.subscribe(listSensors, hass, async_add_entities)
    _LOGGER.info(f"setup_platform end2")
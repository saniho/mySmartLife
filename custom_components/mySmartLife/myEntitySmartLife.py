
import logging
from collections import defaultdict

from homeassistant.helpers.entity import Entity

from homeassistant.const import (
    ATTR_ATTRIBUTION,
)
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(10)
class myEntitySmartLife(Entity):
    """."""

    def __init__(self, name, value):
        """Initialize the sensor."""
        self._name = name
        self._attributes = None
        self._state = value
        _LOGGER.debug("tout est ok")

    @property
    def unique_id(self):
        "Return a unique_id for this entity."
        return "mySmartLife.%s" %self._name
    @property
    def name(self):
        """Return the name of the sensor."""
        return "mySmartLife.%s" %self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return ""
    def _update(self):
        """Update device state."""
        _LOGGER.debug("_update")
        status_counts = defaultdict(int)
        self._attributes = {ATTR_ATTRIBUTION: ""}
        self._attributes.update(status_counts)
        self._state = "%s" %("pressure")
        _LOGGER.debug("_update 2")
    async def async_update(self):
        _LOGGER.debug("async_update")
        self._state = "%s" %("pressure 2")
        await self.async_update_ha_state()
        _LOGGER.debug("async_update 2")
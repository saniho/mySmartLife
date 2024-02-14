
import logging
from collections import defaultdict

from homeassistant.helpers.entity import Entity

from homeassistant.const import (
    ATTR_ATTRIBUTION,
)
from .const import (
    DOMAIN,
    __VERSION__,
    __name__,
)
import datetime
_LOGGER = logging.getLogger(__name__)
class myEntitySmartLife(Entity):
    """."""

    def __init__(self, name, value):
        """Initialize the sensor."""
        self._name = name
        self._timeout = 2 # secondes
        status_counts = {}
        status_counts["version"] = __VERSION__
        status_counts["last_update"] = "%s"%(datetime.datetime.now())
        self._attributes = {}
        self._attributes.update(status_counts)
        self._state = value
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
    def _changeData(self, newValue ):
        self._state = newValue
        self._lastSynchro = datetime.datetime.now()
    def _resetData(self):
        self._state = "unknown"
        self._update()
    def _resetDataCall(self):
        from threading import Timer
        timer = Timer(self._timeout, self._resetData)
        # Démarrage du Timer
        timer.start()
    def _update(self):
        """Update device state."""
        status_counts = {}
        status_counts["version"] = __VERSION__
        status_counts["last_update"] = "%s" %(datetime.datetime.now())
        self._attributes = {}
        self._attributes.update(status_counts)
        self.async_write_ha_state()
    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes
    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attributes
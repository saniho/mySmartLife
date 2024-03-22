"""mySmartLife component."""
from __future__ import annotations

import ast
import asyncio
import logging
import traceback
from datetime import timedelta

try:
    from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
    from homeassistant.const import CONF_SCAN_INTERVAL, EVENT_HOMEASSISTANT_STARTED
    from homeassistant.core import CoreState, HomeAssistant, callback
    from homeassistant.exceptions import ConfigEntryNotReady
    from homeassistant.helpers.typing import ConfigType
    from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
except ImportError:
    # si py test
    class DataUpdateCoordinator:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class ConfigEntryNotReady:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class HomeAssistant:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class ConfigType:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class SOURCE_IMPORT:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class ConfigEntry:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass

    class callback:  # type: ignore[no-redef]
        def __init__(self):
            # nothing to do
            pass



from . import mySmartLife

from .const import (  # isort:skip
    DOMAIN,
    PLATFORMS,
    __VERSION__,
    __name__,
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(10)
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up smartlife_conf from legacy config file."""
    conf = config.get(DOMAIN)
    if not conf:
        return True

    for smartlife_conf in conf:
        ch = dir(smartlife_conf)
        _LOGGER.info(f"smartlife_conf data {ch}")
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": SOURCE_IMPORT}, data=smartlife_conf
            )
        )

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up an smartlife_conf account from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    for platform in PLATFORMS:
        _LOGGER.info(f"smartlife_conf data {platform}")
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unload_ok:
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)

    return unload_ok


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    _LOGGER.info("_async_update_listener ")
    await hass.config_entries.async_reload(entry.entry_id)

async def options_updated_listener(hass, entry):
    """Handle options update. suite modification options"""
    _LOGGER.info("options_updated_listener ")
    _LOGGER.info("options_updated_listener - done -- ")


async def async_set_options(self):
    """Set options for entry."""
    _LOGGER.info(f"async_set_options - proc -- {self.entry.options}")
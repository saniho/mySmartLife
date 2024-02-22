""" Config flow """
import logging
import uuid

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import (  # isort:skip
    DOMAIN,
    CONF_ID,
    CONF_KEY,
    CONF_ENDPOINTKEY,
)

_LOGGER = logging.getLogger(__name__)

class mySmartLifeFlowHandler(  # type: ignore[call-arg]
    config_entries.ConfigFlow, domain=DOMAIN
):

    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        self._errors = {}
        self._data = {}
        self._data["unique_id"] = str(uuid.uuid4())

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return mySmartLifeOptionsFlowHandler(config_entry)

    @callback
    def _show_setup_form(self, user_input=None, errors=None):
        """Show the setup form to the user."""

        _LOGGER.info(f"user_input _show_setup_form {user_input}")
        if user_input is None:
            user_input = {}
        conf_id = ""
        conf_key = ""
        conf_endpointkey = ""

        data_schema = vol.Schema(
            {
                vol.Required(CONF_ID, default=user_input.get(CONF_ID, conf_id)): str,
                vol.Required(CONF_KEY, default=user_input.get(CONF_KEY, conf_key)): str,
                vol.Required(CONF_ENDPOINTKEY, default=user_input.get(CONF_ENDPOINTKEY, conf_endpointkey)): str,
            }
        )
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors or {},
        )

    async def async_step_user(self, user_input=None):  # pylint: disable=unused-argument
        self._errors = {}
        _LOGGER.info(f"user_input async_step_user {user_input}")
        if user_input is None:
            return self._show_setup_form(user_input, self._errors)

        conf_id = user_input[CONF_ID]
        conf_key = user_input.get(CONF_KEY)
        conf_endpointkey = user_input.get(CONF_ENDPOINTKEY)

        # Check if already configured
        await self.async_set_unique_id(f"{conf_id}")
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=conf_id,
            data={
                CONF_ID: conf_id,
                CONF_KEY: conf_key,
                CONF_ENDPOINTKEY: conf_endpointkey,
            },
        )

    async def async_step_import(self, user_input):
        """Import a config entry."""
        return await self.async_step_user(user_input)


class mySmartLifeOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle a option flow."""

    def __init__(self, config_entry):
        self.config_entry = config_entry
        self._data = {}
        self._data["unique_id"] = config_entry.options.get("unique_id")

    async def async_step_init(self, user_input=None):
        """Handle options flow."""
        _LOGGER.info(f"user_input async_step_init {user_input}")
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        conf_id = "ACCESS_ID"
        conf_key = "ACCESS_KEY"
        conf_endpointkey = "wss://mqe.tuyaeu.com:8285/"
        data_schema = vol.Schema(
            {
                vol.Required(
                    CONF_ID,
                    default=self.config_entry.options.get(CONF_ID, conf_id),
                ): str,
                vol.Required(
                    CONF_KEY,
                    default=self.config_entry.options.get(CONF_KEY, conf_key),
                ): str,
                vol.Optional(
                    CONF_ENDPOINTKEY,
                    default=self.config_entry.options.get(CONF_ENDPOINTKEY, conf_endpointkey),
                ): cv.string,
            }
        )
        return self.async_show_form(step_id="init", data_schema=data_schema)
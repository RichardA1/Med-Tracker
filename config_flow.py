"""
med_tracker config_flow.py

Handles the configuration flow and options flow for the integration.
"""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, STATUS_TAKEN, STATUS_LATER, STATUS_FORGOTTEN

class MedTrackerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Med Tracker."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["medication_name"],
                data={
                    "medication_name": user_input["medication_name"],
                    "initial_pills": user_input["initial_pills"],
                    "photo_url": user_input.get("photo_url"),
                    "status": user_input["status"],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("medication_name"): str,
                vol.Required("initial_pills", default=30): int,
                vol.Optional("photo_url"): str,
                vol.Required("status", default=STATUS_LATER): vol.In(
                    [STATUS_TAKEN, STATUS_LATER, STATUS_FORGOTTEN]
                ),
            }),
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return MedTrackerOptionsFlow(config_entry)


class MedTrackerOptionsFlow(config_entries.OptionsFlow):
    """Handle options for an existing entry."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_data = self.config_entry.data
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("initial_pills", default=current_data.get("initial_pills", 30)): int,
                vol.Optional("status", default=current_data.get("status", STATUS_LATER)): vol.In(
                    [STATUS_TAKEN, STATUS_LATER, STATUS_FORGOTTEN]
                ),
            }),
        )

import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class MedTrackerOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_data = self.config_entry.options

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("image_url", default=current_data.get("image_url", "")): str,
                vol.Optional("status", default=current_data.get("status", "Later")): vol.In(["Taken", "Later", "Forgotten"]),
            })
        )

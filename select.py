"""
med_tracker select.py

Creates a select entity for medication status.
"""
from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, STATUS_TAKEN, STATUS_LATER, STATUS_FORGOTTEN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up select entity for med_tracker."""
    data = entry.data
    async_add_entities([MedTrackerStatusSelect(data)])

class MedTrackerStatusSelect(SelectEntity):
    """Select entity for medication status."""

    def __init__(self, data):
        self._attr_name = f"{data['medication_name']} Status"
        self._attr_options = [STATUS_TAKEN, STATUS_LATER, STATUS_FORGOTTEN]
        self._attr_current_option = data.get("status", STATUS_LATER)

    def select_option(self, option: str) -> None:
        """Set the selected option."""
        self._attr_current_option = option

"""
med_tracker sensor.py

Creates a sensor entity showing the remaining pills.
"""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up med_tracker sensor."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([MedTrackerSensor(data)])

class MedTrackerSensor(SensorEntity):
    """Sensor showing remaining pills."""

    def __init__(self, data):
        self._attr_name = f"{data['medication_name']} Remaining Pills"
        self._attr_native_unit_of_measurement = "pills"
        self._attr_state = data["initial_pills"]

    @property
    def native_value(self):
        return self._attr_state

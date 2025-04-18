"""
med_tracker __init__.py

Handles setup of the custom integration, including forwarding entries to platforms.
"""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up med_tracker from a config entry."""
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Forward entry to supported platforms
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor", "select"])
    return True

# Med Tracker – Home Assistant Custom Integration

Med Tracker is a Home Assistant custom integration that lets you add medications as individual entities. Each medication can be tracked with:
- A dropdown (`select`) to set its status: **Taken**, **Later**, or **Forgotten**
- A sensor showing how many pills are left

This is useful for keeping track of daily medications or supplements and can be expanded for reminders, logs, and caregiver dashboards.

---

## Features

✅ Add medications using the **Home Assistant UI (Add Integration)**  
✅ Track inventory of each medication (pill count)  
✅ Set current status from a dropdown: `Taken`, `Later`, or `Forgotten`  
✅ Works with multiple medications  
✅ Fully local, privacy-friendly

---

## Installation

1. Extract the contents of `med_tracker.zip` into your Home Assistant `custom_components` folder:

2. Restart Home Assistant.

3. Go to **Settings > Devices & Services > Integrations**  
   Click **"Add Integration"** and search for `Med Tracker`.

---

## Configuration

You will be prompted to enter the following when adding a new medication:

- **Medication Name** (e.g. "Ibuprofen")
- **Initial Pill Count** (e.g. `30`)
- **Initial Status** (`Taken`, `Later`, or `Forgotten`)

Each medication becomes:
- A **sensor** showing how many pills are left
- A **select** dropdown to update the current status

---

## Updating Status or Count

- The dropdown in the UI allows you to mark whether the medication was taken.
- Inventory tracking is manual for now, but services for auto-decrement can be added easily.

---

## Known Issues

- Status and count are not persisted across reboots unless you enable [state restoration](https://www.home-assistant.io/integrations/restore_state/).
- Services for incrementing or decrementing pill count are not yet implemented.
- No automation reminders yet (can be done via standard HA automations).

---

## Future Improvements

- Add reminder and notification system
- Add support for recurring schedules
- Allow pill count decrement when "Taken" is selected
- Option flow for editing entries after setup

---

## File Structure
custom_components/med_tracker/

├── __init__.py

├── manifest.json

├── config_flow.py

├── sensor.py

├── select.py

└── const.py

---

## Credits

Created by Richard Albritton with ❤️ for the Home Assistant community.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# This HACS integration is obsolete. Please use the official Home Assistant core integration.

# IOmeter HACS
The IOmeter integration to use your IOmeter in Home Assistant to keep track of your power usage, power production and device status.


## Installation

### HACS - Recommended
- Install the [Home Assistant Community Store, short HACS](https://hacs.xyz), if not already done.
- Inside HACS add this repository as a [Custom repository](https://hacs.xyz/docs/faq/custom_repositories/)
- Restart Home-Assistant.

### Manual
- Copy directory `custom_components/iometer` to your `<config dir>/custom_components` directory.
- Restart Home-Assistant.

## Available Sensors
```text
- Power (W): Active power
- Total energy usage (kWh): How much energy the meter used
- Total energy returned (kWh): How much energy the meter returned to the grid
- Meter number: Electricity meter number
- Pin status: Electricity meter pin status
- Core battery level: Battery level of the IOmeter Core in percent
- Core power status: Battery or USB-C power for the IOmeter Core
- Core/Bridge status: Status of the Sub-GHz connection between Core and Bridge
- Signal strength WiFi: WiFi connection strength of the Bridge
- Signal strength Core/Bridge: Sub-GHz connection stren
```

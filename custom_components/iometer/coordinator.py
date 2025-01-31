"""DataUpdateCoordinator for IOmeter."""

from dataclasses import dataclass
import logging

from iometer import IOmeterClient, IOmeterConnectionError, Reading, Status

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

type IOmeterConfigEntry = ConfigEntry[IOMeterCoordinator]


@dataclass
class IOmeterData:
    """Class for data update."""

    reading: Reading
    status: Status


class IOMeterCoordinator(DataUpdateCoordinator[IOmeterData]):
    """Class to manage fetching IOmeter data."""

    config_entry: IOmeterConfigEntry
    client: IOmeterClient

    def __init__(self, hass: HomeAssistant, client: IOmeterClient) -> None:
        """Initialize coordinator."""

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=DEFAULT_SCAN_INTERVAL,
        )
        self.client = client
        self.identifier = self.config_entry.entry_id

    async def _async_update_data(self) -> IOmeterData:
        """Update data async."""
        try:
            reading = await self.client.get_current_reading()
            status = await self.client.get_current_status()
        except IOmeterConnectionError as error:
            raise UpdateFailed(error) from error

        return IOmeterData(reading=reading, status=status)

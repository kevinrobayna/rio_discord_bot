import logging

import requests
from ratelimit import limits, sleep_and_retry
from requests.adapters import HTTPAdapter

logger = logging.getLogger(__name__)


class RaiderIOClient:
    def __init__(self, raider_io_url: str, retries_config: dict):
        self.raider_io_url = raider_io_url
        self.retries_config = retries_config

    @sleep_and_retry  # without this it will fail if we reached the max r/s
    @limits(calls=10, period=1)  # 10r/s
    def retrieve_rio_stats(self, name: str, server: str, region: str = "eu") -> dict:
        try:
            url = f"{self.raider_io_url}?region={region}&realm={server}&name={name}&fields=mythic_plus_scores"
            s = requests.Session()
            s.mount("https://", HTTPAdapter(max_retries=self.retries_config))
            response = s.get(
                url=url,
                headers={"accept": "application/json"},
            )
            return response.json()["mythic_plus_scores"]
        except Exception as e:
            logger.exception(f"RaiderIOClient - Something went wrong while looking for RIO for player {name}-{server}")
            raise e

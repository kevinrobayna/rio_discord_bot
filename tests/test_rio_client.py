from pytest import fixture

from rio_discord_bot.rio_client import RaiderIOClient


@fixture
def mock_get_request(mocker):
    return mocker.patch("requests.Session.get")


RAIDER_IO_EXAMPLE_RESPONSE = {
    "name": "Sylphyl",
    "race": "Troll",
    "class": "Druid",
    "active_spec_name": "Restoration",
    "active_spec_role": "HEALING",
    "gender": "female",
    "faction": "horde",
    "achievement_points": 12275,
    "honorable_kills": 0,
    "region": "eu",
    "realm": "Sanguino",
    "last_crawled_at": "2021-03-08T20:35:40.000Z",
    "profile_url": "https://raider.io/characters/eu/sanguino/Sylphyl",
    "profile_banner": "covenantbanner_nightfae",
    "mythic_plus_scores": {
        "all": 880,
        "dps": 458.2,
        "healer": 880,
        "tank": 0,
        "spec_0": 458.2,
        "spec_1": 0,
        "spec_2": 0,
        "spec_3": 880,
    },
}


def test_get_raider_io_data(mock_get_request):
    mock_get_request.return_value.status_code = 200
    mock_get_request.return_value.json.return_value = RAIDER_IO_EXAMPLE_RESPONSE

    client = RaiderIOClient(
        raider_io_url="https://raider.io/api/v1/characters/profile",
        retries_config={
            "total": 3,
            "backoff_factor": 1,
            "status_forcelist": [429, 500, 502, 503, 504],
        },
    )

    data = client.retrieve_rio_stats(server="sanguino", name="Sylphyl", region="eu")

    assert data["all"] == 880
    assert data["dps"] == 458.2
    assert data["healer"] == 880
    assert data["tank"] == 0

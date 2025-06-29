import pytest
from weather_wardrobe.recommender import get_outfit_recommendation

class DummyResponse:
    def __init__(self, temp, weather_main):
        self.temp = temp
        self.weather_main = weather_main

    def json(self):
        return {
            "main": {"temp": self.temp},
            "weather": [{"main": self.weather_main}]
        }

def fake_requests_get(*args, **kwargs):
    class Response:
        def __init__(self):
            self.status_code = 200
        def json(self):
            return {
                "main": {"temp": 8},
                "weather": [{"main": "Rain"}]
            }
    return Response()

def test_get_outfit_recommendation(monkeypatch):
    import weather_wardrobe.recommender as r

    monkeypatch.setattr(r.requests, "get", fake_requests_get)
    result = r.get_outfit_recommendation("London", "fake-api-key")
    assert "warm jacket" in result.lower()
    assert "umbrella" in result.lower()



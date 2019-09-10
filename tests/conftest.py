import pytest


@pytest.fixture
def event_loop():
    import asyncio
    return asyncio.get_event_loop()

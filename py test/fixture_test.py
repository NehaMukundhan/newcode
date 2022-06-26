import pytest
@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i will execute last")
def test_fixturedemo(setup):
    print("i will execute steps in fixture demo")
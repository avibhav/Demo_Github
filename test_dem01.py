import pytest

@pytest.mark.skip
def test_demoFirst():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings  do  not match"


@pytest.mark.smoke
def test_demoSecond():
    msg = "Hello"
    assert msg == "Hello"
    print(msg)

# -k is used to run particular program with defined keyword
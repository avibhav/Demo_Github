# fixtures are used as setup and tear down methods for test cases- confest file to generalize fixture and make it
# available for the all test cases

import pytest


@pytest.fixture(scope="class")
def setup():
    print("It will be executed first")
    yield
    print("will executes at last")



@pytest.fixture()
def dataLoad():
    print("user Profile")
    return ["Avibhav", "Kumar", "Artificsmasher.com"]


# when we have to use parameterised fixture we need to pass 'request' keyword within method

@pytest.fixture(params=["chrome", "Firefozx","IE"])
def crossBrowser(request):
    return request.param
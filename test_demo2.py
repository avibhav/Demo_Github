#  Xfail is used to run the test but it wll not show either pass or fail
# # -m is used to run those program which are marked
import pytest

# @pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_Greet():
    print("Good Morning")



def test_crossBrowser(crossBrowser):
    print(crossBrowser)


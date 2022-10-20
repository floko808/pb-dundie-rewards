import pytest
from subprocess import check_output, CalledProcessError

@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """test command load"""
    
    out = check_output(["dundie", "load", "tests/assets/people.csv"]).decode("utf-8").split("\n")
    assert len(out) == 3
    
@pytest.mark.integration
@pytest.mark.high
@pytest.mark.parametrize("wrong_command", ["lload", "loady", "carrega"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    with pytest.raises(CalledProcessError) as error:
        out = check_output(["dundie", wrong_command, "tests/assets/people.csv"]).decode("utf-8").split("\n")

    assert "status 2" in str(error.getrepr())
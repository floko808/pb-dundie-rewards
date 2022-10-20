import pytest
from click.testing import CliRunner

from dundie.cli import load, main
from tests.constants import PEOPLE_FILE as PF

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """test command load"""

    out = cmd.invoke(load, PF)

    assert "Dunder Mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    out = cmd.invoke(main, wrong_command, PF)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output

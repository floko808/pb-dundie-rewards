import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE as PF


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_3_people():
    """Test load function"""
    assert len(load(PF)) == 3


@pytest.mark.unit
@pytest.mark.medium
def test_load_positive_first_name_starts_with_j():
    """Test load function"""
    assert load(PF)[0]["name"] == "Jim Halpert"

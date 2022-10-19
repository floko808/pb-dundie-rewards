import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE as PF

@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test load function"""
    assert len(load(PF)) == 2
    assert load(PF)[0][0] == 'J'
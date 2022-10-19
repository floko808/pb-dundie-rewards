import pytest
import os
import uuid
from dundie.core import load
from tests.constants import PEOPLE_FILE as PF


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("Garbage data/file.")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(request):  # injecao de dependencias
    """Test load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    with open(filepath, "w") as file_:
        file_.write("Dados uteis para os testes com pytest")

    assert len(load(PF)) == 2
    assert load(PF)[0][0] == 'J'
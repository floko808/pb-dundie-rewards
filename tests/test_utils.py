import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize("address", ["joe@doe.com", "foo@bar.com"])
def test_positive_check_valid_email(address):
    """Ensure e-mails is valid"""
    print(address)
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize("address", ["joe@.com", "@bar.com", "foo@bar"])
def test_negativa_check_valid_email(address):
    """Ensure e-mails is valid"""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_genereate_simple_password():
    """test generation of random simple password
    TODO: Generate hashed complex passwords and encrypt it
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))
    assert len(set(passwords)) == 100

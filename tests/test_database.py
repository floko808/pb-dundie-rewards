import pytest

from dundie.database import EMPTY_DB, add_movement, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_db():
    db = connect()
    data = {
        "name": "Jhon Doe",
        "role": "Relezeiro",
        "dept": "Eng App",
    }
    db["people"]["joe@doe.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["joe@doe.com"] == data


@pytest.mark.unit
def test_add_person_for_the_first_time():
    pk = "joe@doe.com"
    data = {
        "name": "Jhon Doe",
        "role": "Relezeiro",
        "dept": "Eng App",
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    db = connect()
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    assert len(db["movement"][pk]) > 0
    assert db["movement"][pk][0]["value"] == 500


@pytest.mark.unit
def test_negative_add_person_valid_email():
    with pytest.raises(ValueError):
        add_person({}, ".@blah", {})


@pytest.mark.unit
def test_add_or_remove_points_for_person():
    pk = "joe@doe.com"
    data = {
        "name": "Jhon Doe",
        "role": "Relezeiro",
        "dept": "Eng App",
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)
    db = connect()

    before = db["balance"][pk]

    add_movement(db, pk, -100, "manager")
    commit(db)

    db = connect()
    after = db["balance"][pk]

    assert after == before - 100
    assert after == 400
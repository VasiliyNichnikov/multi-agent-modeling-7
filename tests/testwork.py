from app.models.user import UserModel


def test_user(session):
    user = UserModel(user_id=349134)
    session.add(user)
    session.commit()

    assert session.query(UserModel).filter(UserModel.user_id == 349134) is not None
    # obj = MyFactory(user_id=1294)
    # assert obj


def test_user_2(session):
    user = UserModel(user_id=349134)
    session.add(user)
    session.commit()
    assert len(session.query(UserModel).filter(UserModel.user_id == 349134).all()) == 1

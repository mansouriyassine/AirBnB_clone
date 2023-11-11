#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User


def test_save_reload_user():
    """Test for saving and reloading User objects."""

    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"

    my_user.save()

    storage.reload()

    all_objs = storage.all()

    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Created User object --")
    print(my_user)


if __name__ == "__main__":
    test_save_reload_user()

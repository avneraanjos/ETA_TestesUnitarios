from src.models.store import Store
from src.models.user import User
from typing import Optional, Union


class ServiceUser:
    def __init__(self):
        self._store = Store()

    def add_user(self, name: str, job: str) -> str:
        if ((name is not None and job is not None) and
                (isinstance(name, str) and isinstance(job, str))):
            if self.get_user_by_name(name) is None:
                user = User(name, job)
                self._store.bd.append(user)
                return "User added"
            else:
                return "User already existent"
        else:
            return "Parameter not valid"

    def get_user_by_name(self, name: str) -> Optional[Union[User, str]]:
        if name is not None and isinstance(name, str):
            for user in self._store.bd:
                if user.name == name:
                    return user
            return None
        else:
            return "Parameter not valid"

    def remove_user(self, name: str) -> str:
        if name is not None and isinstance(name, str):
            user = self.get_user_by_name(name)
            if user is not None:
                self._store.bd.remove(user)
                return "User removed"
            else:
                return "User not existent"
        else:
            return "Parameter not valid"

    def update_user(self, name: str, newname: str) -> str:
        if name is not None and newname is not None and isinstance(name, str) and isinstance(newname, str):
            user = self.get_user_by_name(name)
            if user is not None:
                user.name = newname
                return "User updated"
            else:
                return "User not existent"
        return "Parameter not valid"

from src.services.service_user import ServiceUser
from src.models.user import User


class TestServiceUser:
    def test_add_user_success(self):
        service = ServiceUser()
        expected_result = "User added"
        result = service.add_user("Maria", "QA")
        print("AVNER")
        print(service._store.bd)
        assert result == expected_result

    def test_add_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.add_user(None, "QA")
        assert result == expected_result

    def test_add_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.add_user(2, "QA")
        assert result == expected_result

    def test_add_user_already_existent(self):
        service = ServiceUser()
        expected_result = "User already existent"
        service.add_user("Maria", "QA")
        result = service.add_user("Maria", "QA")
        assert result == expected_result

    def test_remove_user_success(self):
        service = ServiceUser()
        expected_result = "User removed"
        service.add_user("Maria", "QA")
        result = service.remove_user("Maria")
        assert result == expected_result

    def test_remove_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.remove_user(None)
        assert result == expected_result

    def test_remove_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.remove_user(2)
        assert result == expected_result

    def test_remove_user_not_existent(self):
        service = ServiceUser()
        expected_result = "User not existent"
        result = service.remove_user("Maria")
        assert result == expected_result

    def test_update_user_success(self):
        service = ServiceUser()
        expected_result = "User updated"
        service.add_user("Maria", "QA")
        result = service.update_user("Maria", "Mariana")
        assert result == expected_result

    def test_update_user_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.update_user(None, "Mariana")
        assert result == expected_result

    def test_update_user_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.update_user(2, "Mariana")
        assert result == expected_result

    def test_update_user_not_existent(self):
        service = ServiceUser()
        expected_result = "User not existent"
        result = service.update_user("Maria", "Mariana")
        assert result == expected_result

    def test_get_user_by_name_success(self):
        service = ServiceUser()
        expected_user = User("Maria", "QA")
        service.add_user("Maria", "QA")
        user = service.get_user_by_name("Maria")
        assert user == expected_user

    def test_get_user_by_name_not_str(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.get_user_by_name(2)
        assert result == expected_result

    def test_get_user_by_name_none(self):
        service = ServiceUser()
        expected_result = "Parameter not valid"
        result = service.get_user_by_name(None)
        assert result == expected_result

    def test_get_user_by_name_not_existent(self):
        service = ServiceUser()
        expected_result = None
        result = service.get_user_by_name("Maria")
        assert result == expected_result


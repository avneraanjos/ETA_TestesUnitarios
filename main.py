from src.services.service_user import ServiceUser

service = ServiceUser()
expected_result = "User added"
result = service.add_user(name="Maria", job="QA")
assert result == expected_result
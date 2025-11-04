import pytest

from authz.evaluator import evaluate


@pytest.mark.parametrize(
    "user,action,resource,expected",
    [
        ({"role": "admin"}, "delete", "document", "permit"),
        ({"role": "reader"}, "read", "document", "permit"),
        ({"role": "reader"}, "write", "document", "deny"),
        ({"role": "guest"}, "write", "document", "deny"),
        ({"role": "unknown"}, "read", "document", "deny"),
    ],
)
def test_evaluate_basic(user, action, resource, expected):
    res = evaluate(user, action, resource)
    assert res["decision"] == expected

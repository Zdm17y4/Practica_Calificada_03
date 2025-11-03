# main.py
"""
main.py
-------
Script de prueba manual del motor de autorización (Sprint 01).
Ejecuta distintos escenarios y muestra las decisiones.
"""

from authz.evaluator import evaluate

def test_cases():
    users = [
        {"role": "admin"},
        {"role": "reader"},
        {"role": "guest"}
    ]

    actions = ["read", "write"]
    resource = "document"

    for user in users:
        for action in actions:
            decision = evaluate(user, action, resource)
            print(f"User={user['role']:<6} | Action={action:<5} | Decision={decision['decision']} | Policy={decision['policy_id']}")

if __name__ == "__main__":
    test_cases()

# authz/evaluator.py
"""
evaluator.py
-------------
Evalúa si un usuario tiene permiso para realizar
una acción sobre un recurso según las políticas cargadas.
"""

from .policy_parser import load_policies

def evaluate(user, action, resource):
    """
    Evalúa si el usuario tiene permiso.

    Parámetros:
        user (dict): Ej. {"role": "reader"}
        action (str): Ej. "read"
        resource (str): Ej. "document"

    Retorna:
        dict: {
            "decision": "permit" o "deny",
            "policy_id": "policy-001",
            "reason": "Matched policy policy-001"
        }
    """
    policies = load_policies()

    for p in policies:
        # Coincidencias de rol, acción y recurso
        role_match = (p["subject"]["role"] == user["role"] or p["subject"]["role"] == "*")
        action_match = (p["action"] == action or p["action"] == "*")
        resource_match = (p["resource"] == resource or p["resource"] == "*")

        if role_match and action_match and resource_match:
            return {
                "decision": p["effect"],
                "policy_id": p["id"],
                "reason": f"Matched policy {p['id']}"
            }

    # Si no hay coincidencia, negar por defecto
    return {
        "decision": "deny",
        "policy_id": None,
        "reason": "No matching policy found"
    }

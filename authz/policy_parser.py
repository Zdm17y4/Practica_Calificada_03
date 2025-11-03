# authz/policy_parser.py
"""
policy_parser.py
----------------
Se encarga de cargar todas las políticas de autorización
desde archivos JSON ubicados en la carpeta 'authz/policies'.

Cada política define reglas como:
- id: identificador único
- subject: quién (rol/usuario)
- resource: sobre qué recurso
- action: acción permitida o denegada
- effect: "permit" o "deny"
"""

import json
import os

def load_policies(path="./authz/policies"):
    """
    Carga todas las políticas JSON desde la carpeta indicada.
    Retorna una lista de diccionarios.

    Ejemplo:
    [
        {
            "id": "policy-001",
            "subject": {"role": "reader"},
            "resource": "document",
            "action": "read",
            "effect": "permit"
        }
    ]
    """
    policies = []

    for filename in os.listdir(path):
        if filename.endswith(".json"):
            file_path = os.path.join(path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                policy = json.load(f)

                # Validar campos básicos
                required = ["id", "subject", "resource", "action", "effect"]
                if all(k in policy for k in required):
                    policies.append(policy)
                else:
                    print(f"[WARN] Política inválida: {filename}")

    print(f"[INFO] {len(policies)} políticas cargadas desde {path}")
    return policies

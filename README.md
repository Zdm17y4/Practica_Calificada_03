# Sprint 01 - Core Policy Engine

## Objetivo del Sprint 01

Implementar el **motor base de autorización (AuthZ)** para el sistema **RBAC (Role-Based Access Control)**.  
El propósito es decidir, mediante **políticas declaradas en formato JSON**, si un usuario tiene o no permiso para ejecutar una acción sobre un recurso determinado.

## Estructura general del proyecto (Sprint 01)


## Descripción del Módulo AuthZ (Core Policy Engine)

El módulo **AuthZ** constituye el núcleo del sistema de control de acceso.  
Su función es **evaluar políticas de autorización** bajo el modelo **RBAC**, siguiendo el principio de **denegación por defecto**.

### Componentes principales

| Archivo | Descripción |
|----------|--------------|
| `authz/policy_parser.py` | Carga y valida las políticas desde `/authz/policies/`. |
| `authz/evaluator.py` | Evalúa las solicitudes de acceso según las políticas cargadas. |
| `authz/policies/*.json` | Conjunto de políticas base (`admin`, `reader`, `guest`). |

## Estructura de una Política

Cada política se declara en formato JSON con los siguientes campos:

```json
{
  "id": "policy-001",
  "description": "Permite lectura de documentos a usuarios con rol lector",
  "subject": {"role": "reader"},
  "resource": "document",
  "action": "read",
  "effect": "permit"
}
```

## Flujo de Ejecución del Motor de Políticas

### Paso 1 – Cargar las políticas
```python
from authz.policy_parser import load_policies
policies = load_policies()
```

### Paso 2 – Evaluar el acceso
```python
from authz.evaluator import evaluate
result = evaluate({"role": "reader"}, "read", "document")
```

### Paso 3 – Resultado esperado
```json
{"decision": "permit", "policy_id": "policy-001"}
```

### Uso completo
Podemos realizar todo el ejemplo completo mediante el archivo `main.py`.
Salida esperada:
```pgsql
User=admin  | Action=read  | Decision=permit
User=admin  | Action=write | Decision=permit
User=reader | Action=read  | Decision=permit
User=reader | Action=write | Decision=deny
User=guest  | Action=read  | Decision=deny
User=guest  | Action=write | Decision=deny
```

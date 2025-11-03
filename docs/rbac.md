# Role-Based Access Control (RBAC)

El modelo **RBAC (Role-Based Access Control)** define el control de acceso basado en roles.  
Cada usuario hereda permisos a través de su rol, en lugar de asignaciones directas.

En este proyecto, el sistema AuthZ utiliza RBAC para decidir si un usuario puede o no ejecutar una acción sobre un recurso.

## Componentes del motor AuthZ

1. **Policy Parser (`policy_parser.py`)**  
   Carga todas las políticas desde archivos JSON y las valida.

2. **Evaluator (`evaluator.py`)**  
   Determina si una solicitud es `permit` o `deny` según las políticas cargadas.

3. **Policies (`/authz/policies/`)**  
   Carpeta con las reglas declaradas en formato JSON.

## Flujo lógico de evaluación

1. El usuario solicita una acción sobre un recurso.  
2. El evaluador busca una política cuyo `subject.role`, `action` y `resource` coincidan.  
3. Si encuentra coincidencia → devuelve el `effect` (`permit` o `deny`).  
4. Si no hay coincidencia → deniega el acceso por defecto.

## Reglas de decisión

- Si una política coincide → se aplica su `effect`.
- Si varias coinciden → se toma la más específica.
- Si ninguna coincide → se aplica **denegación por defecto** (`deny`).

## Casos esperados

| Rol | Acción | Recurso | Resultado |
|------|---------|----------|------------|
| admin | read | document | permit |
| admin | write | document | permit |
| reader | read | document | permit |
| reader | write | document | deny |
| guest | write | document | deny |

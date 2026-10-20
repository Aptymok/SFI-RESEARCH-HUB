# SFI-DF-001 · CORRIGENDUM 001 — inadmisibilidad de la comparación auxiliar como evaluación MIHM/MIHM-T

**Fecha de la rectificación:** 2026-10-20
**Clase:** POST_HOC_METHODOLOGICAL_CORRECTION
**Estado:** CORRECCIÓN DOCUMENTAL EN RAMA DE INVESTIGACIÓN, SIN PROMOCIÓN CANÓNICA
**Ámbito:** SFI-DF-001 A/B, especialmente el benchmark B de 15 minutos y las comparaciones M0/M1 descriptivas.
**Regla:** conservar versiones y resultados originales, sin borrado, sin modificación retroactiva de observaciones y sin reinterpretación favorable o desfavorable de MIHM.

## 1. Error identificado

Los documentos de SFI-DF-001 utilizan los nombres `M0` y `M1` para dos actividades que no constituyen una evaluación experimental válida de la metodología MIHM ni una ejecución nativa de MIHM-T:

1. Las lecturas A y B elaboraron dos **narrativas documentales en una misma conversación**, sin la ejecución del selector metodológico, el contrato MIHM y la extensión temporal canónica, sin análisis ciego ni evaluador científico independiente.
2. El benchmark de rendimiento B comparó **dos regresiones Ridge con distintas variables temporales** sobre el número de aplicaciones a Neon cada quince minutos. Su llamado `M1_temporal_proxy` **no implementa MIHM, MIHM-T, su selección de método, estado multinodo, restricciones ni modelo dimensional de transferencia**. No observó relojes originales de autorización, decisión o ejecución.

La etiqueta de veredicto `NO_DEMONSTRATED_INCREMENT` usada en documentos anteriores puede interpretarse erróneamente como un resultado de MIHM contra métodos existentes. **Se retira como veredicto científico sobre MIHM para A y B.** El estado correcto de la hipótesis metodológica MIHM es `NOT_EVALUATED_BY_THIS_EXPERIMENT`, no `REFUTED`, `CONFIRMED`, ni un resultado negativo empírico de MIHM.

## 2. Qué permanece verdadero y reutilizable

- Los agregados y lecturas de estado Supabase / Neon / SFI_ROOT fueron observaciones reales en instantes distintos y no atómicos; conservan su procedencia y limitaciones.
- El código y la programación declarada de continuidad tenían discrepancias de metadatos; el defecto se documentó en `Aptymok/system-friction#791`. No se infiere de ello qué cron se ejecutó.
- El benchmark auxiliar se **ejecutó** sobre una extracción autorizada agregada de 2,470 eventos `applied_at` en 223 intervalos. Su holdout evaluó 79 intervalos: MAE M0=17.523, MAE proxy temporal=18.777 y MAE de cero=17.114. Estas cifras **solo comparan esos pronosticadores auxiliares en esa muestra**. No evalúan ni refutan MIHM-T.
- Los resultados preliminares de documentación y la búsqueda de errores operativos permanecen como **QA, diagnóstico y preparación de instrumentos**, no validación científica ni fracaso científico de la metodología.

## 3. Reclasificación de los artefactos existentes

| Artefacto original | Clase legítima | Inadmisible como |
|---|---|---|
| `results/A_M0_CONVENTIONAL.md` | Lectura documental exploratoria | Control confirmatorio independiente |
| `results/A_M1_MIHM.md` | Representación manual inspirada en MIHM | Ejecución computacional de MIHM |
| `results/A_COMPARISON.md` | Nota de comparación narrativa de un mismo analista | Resultado científico M0 vs MIHM |
| `results/B_SELF_SYSTEM_EXPLORATORY.md` | Observaciones operativas y reconstrucción de alcance limitado | Demostración o refutación de MIHM-T |
| `results/B_RETROSPECTIVE_THROUGHPUT_COMPARISON.md` | Benchmark de ingeniería de regresiones auxiliares | Evaluación nativa MIHM-T, predicción de fricción o causalidad |
| Evento Method Lab `94057a3b-7bce-4889-94bb-d38f862773da` | Registro derivado de observaciones y análisis exploratorios | Validación/falsación de MIHM, experimento nativo, RETURN científico |

Cualquier texto anterior `NO_DEMONSTRATED_INCREMENT` debe leerse estrictamente como **no se ha mostrado beneficio adicional en la representación manual o el modelo auxiliar ensayado**, NO como inferencia sobre la eficacia de MIHM.

## 4. Restricción institucional y estadística

**No contabilizar** estos artefactos como:
- intentos confirmatorios de validación/falsación de MIHM, MIHM-T o SFT;
- evidencia favorable o desfavorable en el registro de hipótesis científicas de MIHM;
- tasa institucional de éxitos/fracasos científicos; o
- evidencia de certificación, auditoría acreditada, predicción prospectiva o RETURN externo.

Conservar todos los datos legítimos y los resultados auxiliares con sus nombres originales y procedencia. Si se citan, citar **esta rectificación junto al documento original**. No reescribir el registro histórico como si el ensayo hubiera sido distinto.

## 5. Condiciones para una comparación auténtica

Una nueva prueba requiere ANTES de ejecutarse: delimitar el objeto real para el cual el canon selecciona `SFI_INSTITUTIONAL` / `SCOREFRICTION` / `PPOI` según propósito; construir un `SfiMihmFoundationFrame` válido; ejecutar `assessSfiMihmFoundation()`; admitir o bloquear MIHM-T por las referencias reales de dimensiones; capturar fuentes, permisos y relojes sin fuga temporal; invocar el instrumento propio realmente implementado si está disponible; definir una alternativa convencional competente con igual paquete y presupuesto; preregistrar resultados y fallos; y organizar evaluación independiente.

Si el código existente solo permite validar estructura y fuentes, reportar `NATIVE_MIHMT_EMPIRICAL_EXECUTION_NOT_IMPLEMENTED_OR_NOT_YET_VERIFIED`, **sin sustituirlo de nuevo por una regresión y llamarla MIHM**.

## 6. Autoridad y trazabilidad

Este documento es una **rectificación editorial y epistemológica posterior a los resultados**. No solicita borrar evidencia, alterar el estado histórico ni autoconceder a SFI reconocimiento científico. El evento original en Method Lab se conserva íntegro; se vinculará un nuevo evento derivado que lo rectifica, sin borrarlo ni promoverlo.

El defecto `system-friction#791` continúa como incidencia técnica real e independiente de este problema de método.

**Conclusión corregida:** `MIHM_METHOD_NOT_EVALUATED_BY_SFI_DF_001_A_OR_B`. Sólo se evaluaron lecturas documentales y pronosticadores auxiliares de ingeniería.

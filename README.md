# Trabajo Práctico: Sistemas de Procesamiento de Datos
## Tecnicatura Universitaria en Programación - UTN
### Documentación del Proyecto: Célula de Desarrollo (Fase PROY-3)

---

## 1. Introducción y Selección de Escenario
Este repositorio contiene el desarrollo e implementación del Trabajo Práctico obligatorio para la materia de Organización Empresarial. De acuerdo con los lineamientos provistos por la cátedra, se ha seleccionado el **Escenario B: Análisis de Ventas de una Pequeña Empresa**.

El objetivo central del sistema es automatizar la ingesta, validación y procesamiento estadístico de registros de transacciones anuales utilizando únicamente recursos nativos de Python, garantizando un rendimiento óptimo y una arquitectura modular limpia.

---

## 2. Roles y Distribución de Responsabilidades
El flujo de trabajo se estructuró bajo una modalidad de simulación de roles ágiles, distribuidos de la siguiente manera para el cumplimiento de las tres fases del proyecto:
(Cabe aclarar que al trabajo lo realice de manera individual siempre respetando la division de roles)

* **P1 - Líder y Organizador (Rol: Hugo):** Responsable del diseño y aprovisionamiento inicial del repositorio remoto en GitHub, la definición de la estructura base de directorios y el control del archivo global de documentación.
* **P2 - Desarrollador Técnico (Rol: Paco):** Encargado de la implementación de la lógica algorítmica pura, el control de flujos con estructuras condicionales, la manipulación de cadenas de texto y el manejo de flujos de archivos I/O de entrada.
* **P3 - Revisor y QA (Rol: Luis):** Responsable de la auditoría del código, optimización de la documentación técnica interna, control de calidad, aseguramiento de la consistencia de la rama principal (`main`) y la gestión final de la integración mediante Pull Requests.

---

## 3. Arquitectura del Repositorio y Estructura de Directorios
Para asegurar la mantenibilidad y cumplir con los estándares técnicos solicitados, el proyecto se organiza de forma jerárquica bajo el siguiente esquema:

```text
TP_analisis_ventas/
│
├── datos/
│   └── sales_sample_2024.csv        # Dataset fuente con el histórico de transacciones
│
├── scripts/
│   └── analisis-ventas.py          # Script principal con la lógica de procesamiento
│
├── resultados/
│   └── resultados.txt              # Reporte final consolidado generado por el sistema
│
└── README.md                       # Documentación técnica e institucional del proyecto

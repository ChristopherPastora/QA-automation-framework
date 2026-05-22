<div align="center">

# 🧪 QA Automation Framework

### Framework profesional de automatización · Web + API · Selenium · Pytest · CI/CD

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![Pytest](https://img.shields.io/badge/Pytest-7.x-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

</div>

---

## 📋 Descripción

Framework de automatización de pruebas end-to-end diseñado con buenas prácticas de ingeniería de calidad. Cubre pruebas **Web** con Selenium y pruebas de **API REST** con Requests, integrado con un pipeline de CI/CD en GitHub Actions.

---

## 🏗️ Estructura del proyecto

```
qa-automation-framework/
├── .github/
│   └── workflows/
│       └── qa-pipeline.yml       # Pipeline CI/CD
├── tests/
│   ├── web/
│   │   ├── pages/                # Page Object Model
│   │   │   ├── base_page.py
│   │   │   └── login_page.py
│   │   └── test_login.py
│   ├── api/
│   │   ├── clients/              # API Clients
│   │   │   └── base_client.py
│   │   └── test_users_api.py
│   └── conftest.py               # Fixtures globales
├── utils/
│   ├── config.py                 # Configuración global
│   └── logger.py                 # Logger centralizado
├── reports/                      # Reportes HTML generados
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/ChristopherPastora/qa-automation-framework.git
cd qa-automation-framework
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 3. Ejecutar pruebas

```bash
# Todas las pruebas
pytest

# Solo pruebas web
pytest tests/web/ -v

# Solo pruebas API
pytest tests/api/ -v

# Con reporte HTML
pytest --html=reports/report.html --self-contained-html
```

---

## 🧩 Patrones y buenas prácticas

| Patrón | Descripción |
|--------|-------------|
| **Page Object Model** | Separación de lógica de UI y lógica de test |
| **Fixtures con Pytest** | Setup/teardown reutilizable y modular |
| **API Client Layer** | Capa de abstracción para llamadas HTTP |
| **Logging centralizado** | Trazabilidad completa de ejecución |
| **CI/CD con GitHub Actions** | Ejecución automática en cada PR |

---

## 🤖 CI/CD Pipeline

Cada push o Pull Request ejecuta automáticamente:

```
Push/PR → Install deps → Run Web Tests → Run API Tests → Generate Report → Upload Artifact
```

---

## 📊 Cobertura de pruebas

- ✅ Login / autenticación web
- ✅ Flujos de usuario end-to-end
- ✅ CRUD de API REST (GET, POST, PUT, DELETE)
- ✅ Validación de esquemas de respuesta
- ✅ Manejo de errores y casos de borde

---

<div align="center">

*Desarrollado por [Christopher Pastora](https://github.com/ChristopherPastora) · QA Engineer Senior*

</div>

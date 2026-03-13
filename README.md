# Model Property Registry (Static API)

This repository functions as a **Free Static API Server**, leveraging GitHub's infrastructure to serve model telemetry with zero-latency overhead.

## 🚀 Architectural Overview

This system orchestrates continuous data synchronization and delivery through several key components:

- **Automated Synchronization**: A robust CI/CD pipeline (GitHub Actions) performs a daily reconciliation with the OpenRouter API to ensure the registry remains current with the latest model releases.
- **Static API Paradigm**: By serving structured JSON files directly from the repository, clients can retrieve model properties without the need for a dynamic backend, maximizing reliability and speed.
- **Extensible Registry**: Beyond automated fetching, the system supports high-fidelity manual registration of customized or proprietary models.

## 📡 API Documentation

### 1. Model Index
Retrieve a comprehensive, alphabetically sorted list of all registered models and their corresponding file paths.

**Endpoint:**
`https://raw.githubusercontent.com/activebook/models/main/list.json`

### 2. Model Telemetry
Access detailed properties for a specific model using the path provided in the index.

**Pattern:**
`https://raw.githubusercontent.com/activebook/models/main/models/[model_file].json`

**Example:**
`https://raw.githubusercontent.com/activebook/models/main/models/openai_gpt-4o.json`

---

## 🛠 Management & Operations

### Synchronizing Remote Data
To manually trigger a synchronization of remote OpenRouter data:
```bash
python3 sync_models.py
```
*Note: This is automatically performed every 24 hours via GitHub Actions.*

### Adding Customized Models
For models not present on OpenRouter, use the following utility to register them in the registry:
```bash
python3 add_custom_model.py <provider> <model_name> <context_length> <max_completion_tokens>
```

**Example:**
```bash
python3 add_custom_model.py activebook quantum-llama 128000 8192
```

---

## 📁 Repository Structure
- `models/`: Catalog of individual model JSON assets.
- `list.json`: The primary index for programmatic discovery.
- `sync_models.py`: The synchronization and indexing engine.
- `add_custom_model.py`: Utility for manual registry entries.
- `.github/workflows/`: Automation orchestration logic.
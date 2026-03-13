# Contributing to Model Property Registry

Thank you for your interest in contributing to the Model Property Registry. This document outlines the procedures for contributing to this project, with a particular emphasis on the integration of custom models.

## How to Contribute

To maintain a high standard of quality and consistency, we follow these general steps for contributions:

1. **Fork the Repository**: Create a personal copy of the repository on GitHub.
2. **Clone the Fork**: Download the repository to your local machine.
3. **Create a Feature Branch**: Use a descriptive name for your branch (e.g., `feat/add-quantum-llama`).
4. **Implement Changes**: Add your models or apply fixes.
5. **Commit and Push**: Ensure your commit messages are clear and professional.
6. **Open a Pull Request**: Submit your changes for review against the `main` branch.

## Adding Custom Models

We particularly welcome contributions that expand our registry with high-fidelity model telemetry. For models not currently indexed by OpenRouter, please use the provided automation utility.

### Prerequisites

- **Python 3.x**: Ensure you have a modern Python environment installed.
- **Dependencies**: Install the required libraries via pip:
  ```bash
  pip install requests
  ```

### Using the Registration Utility

The `add_custom_model.py` script standardizes the creation of model assets and ensures the registry index is automatically refreshed.

#### Command Syntax

```bash
python3 add_custom_model.py <provider> <model_name> <context_length> <max_completion_tokens>
```

#### Argument Definitions

- `provider`: The entity providing the model (e.g., `openai`, `anthropic`, `custom`).
- `model_name`: The specific identifier for the model (e.g., `gpt-4o`, `claude-3-opus`).
- `context_length`: The maximum number of tokens supported in the context window (integer).
- `max_completion_tokens`: The maximum number of tokens allowed in a single completion (integer).

#### Implementation Example

To register a proprietary model named `quantum-llama` from a provider named `activebook`:

```bash
python3 add_custom_model.py activebook quantum-llama 128000 8192
```

### Verification of Changes

Upon successful execution, the script will:
1. Generate a standardized JSON asset in the `models/` directory.
2. Update the `list.json` index to include the new entry.

Please verify these files locally before submitting your Pull Request to ensure the telemetry is accurate.

## Reporting Issues

If you encounter technical anomalies or have suggestions for architectural improvements, please open an issue on the GitHub repository. Provide as much context as possible to facilitate a swift resolution.

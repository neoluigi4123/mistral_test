# Mistral Test

This repository contains a simple Python project designed to demonstrate configuration and usage of a local environment with a custom LLM interface. It currently includes:

- `config.py` – Holds configuration settings for the application.
- `llm.py` – Provides an interface to interact with a large language model.
- `main.py` – Entry point for running the application.
- `requirements.txt` – Lists Python dependencies.

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url> mistral_test
   cd mistral_test
   ```

2. **Create a virtual environment (Windows example)**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**
   Edit `config.py` to suit your environment (API keys, model names, etc.)

## ▶️ Usage

Run the main script to start the application:

```bash
python main.py
```

The program will load configuration, initialize the LLM client, and perform its designated task.

## 📝 Project Structure

```
config.py         # Configuration settings
llm.py            # LLM client interface
main.py           # Application entry point
requirements.txt  # Required packages
README.md         # This file
local_data/       # Example data storage
```

## 🚀 Contributing

Contributions are welcome! Please open issues or pull requests on the repository. Make sure to follow PEP 8 style and include tests when adding features.

## 📄 License

**MIT License** - See the [LICENSE](LICENSE) file for details.

---

Enjoy exploring the Mistral test project!
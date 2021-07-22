# demostack

# Local debug config for VSCode on Windows

## Poetry

install the poetry: https://python-poetry.org/docs/#installation

```powershell
> poetry config --list
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}\\virtualenvs"
> poetry config virtualenvs.in-project true --local
> poetry config virtualenvs.path ".venv" --local
> poetry config --list
virtualenvs.in-project = true
virtualenvs.path = ".venv"
```

install required packages from `pyproject.toml`

```powershell
> poetry install
```

## VSCode

check your current config.

```bash
> poetry config --list
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}\\virtualenvs"
> exit
```

config examples:

`.vscode/launch.json`

```json
{
    "version": "0.2.0",
    "configurations": [{
        "name": "Python FastAPI",
        "type": "python",
        "request": "launch",
        "module": "uvicorn",
        "console": "integratedTerminal",
        "justMyCode": false,    // allow debugging thirdparty code
        "args": [
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
            "--reload",
        ],
        "envFile": "${workspaceFolder}/.env",
    }]
}
```

`.vscode/settings.json`
```json
{
    // [workspace settings.json]
    // interpreter
    "python.pythonPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",

    // console
    "terminal.integrated.defaultProfile.windows": "PowerShell",

    // formatter
    "editor.formatOnSave": true,
    "editor.formatOnPaste": false,
    "python.formatting.provider": "black",

    // linter
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--config=.flake8"
    ],
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.lintOnSave": true,

    // tester
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": false,
    "python.testing.pytestArgs": ["tests"],

    // misc
    "python.languageServer": "Pylance",
    "files.watcherExclude": {
        "**/.git/objects/**": true,
        "**/.git/subtree-cache/**": true,
        "**/node_modules/*/**": true,
        "**/.hg/store/**": true,
        "**/.venv/**": true
    }
}
```
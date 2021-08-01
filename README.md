# demostack

A snippet for creating my backend app, based on the following projects.
https://github.com/tiangolo/full-stack-fastapi-postgresql

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
    "configurations": [
        {
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
    },
    {
        "name": "Alembic make rev",
        "type": "python",
        "request": "launch",
        "module": "alembic",
        "console": "integratedTerminal",
        "args": [
            "revision",
            "--autogenerate",
            "-m",
            "'empty comment.'",
        ],
        "envFile": "${workspaceFolder}/.env",
    },
    {
        "name": "Alembic migrate to latest",
        "type": "python",
        "request": "launch",
        "module": "alembic",
        "console": "integratedTerminal",
        "args": [
            "upgrade",
            "head",
        ],
        "envFile": "${workspaceFolder}/.env",
    }

  ]
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


# Alembic

https://alembic.sqlalchemy.org/en/latest/tutorial.html

make the version.

```bash
$ alembic revision --autogenerate -m "some comment.."
```

```bash
$ show version history

alembic history --verbose
Rev: 0672759c3200 (head)
Parent: <base>
Path: ${workspaceFolder}/alembic/versions/0672759c3200_empty_comment.py

    'empty comment.'

    Revision ID: 0672759c3200
    Revises:
    Create Date: 2021-08-02 00:10:23.529062
```


upgrade to the head, runs alembic/env.py run_migrations_online.

`$ alembic upgrade head`

downgrade to latest version.

```bash
$ alembic downgrade base
### or
$ alembic downgrade -1
```

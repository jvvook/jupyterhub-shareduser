# Simple authenticator/spawner for user-wide Jupyterhub

This extension simply turns Jupyterhub into Jupyterlab with multiple configurations identified by arbitrarily chosen names. Other things such as base directory and password are still shared.

## Motivation

Our lab used to share a single instance of Jupyterlab on a single Unix account. The problem was that the Jupyterlab session and configuration were also shared between the members. This extension enables the separation of them by arbitrarily chosen names.

## Installation

Install user-wide Jupyterhub along with Jupyterlab (or Notebook).

```bash
conda install -c conda-forge jupyterlab jupyterhub
```

Clone this repository and run `pip install -e .`

## Configuration

```py
c.JupyterHub.authenticator_class = "shareduser.SUAuthenticator"
c.SUAuthenticator.password_hash = "$argon2id$v=19$m=102400,t=2,p=..."
c.JupyterHub.spawner_class = "shareduser.SUSpawner"
c.Spawner.default_url = "/lab"
```

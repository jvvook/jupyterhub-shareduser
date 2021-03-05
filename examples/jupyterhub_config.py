c.JupyterHub.authenticator_class = "milabhub.MILABAuthenticator"
c.MILABAuthenticator.password_hash = "$argon2id$v=19$m=102400,t=2,p=8$ea/JivMMOpOUN5ym19409w$+04mRsmdQyDKib2erZyU2A"
c.JupyterHub.spawner_class = "milabhub.MILABSpawner"
c.Spawner.default_url = "/lab"

from pathlib import Path
hub_dir = Path.home() / ".jupyterhub"
c.JupyterHub.cookie_secret_file = str(hub_dir / "jupyterhub_cookie_secret")
c.JupyterHub.db_url = str(hub_dir / "jupyterhub.sqlite")
c.JupyterHub.pid_file = str(hub_dir / "jupyterhub.pid")
c.ConfigurableHTTPProxy.pid_file = str(hub_dir / "jupyterhub-proxy.pid")

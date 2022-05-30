c.JupyterHub.authenticator_class = "shareduser.SUAuthenticator"
c.SUAuthenticator.password_hash = "$argon2id$v=19$m=102400,t=2,p=..."
c.JupyterHub.spawner_class = "shareduser.SUSpawner"
c.Spawner.default_url = "/lab"

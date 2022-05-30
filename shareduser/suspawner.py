from pathlib import Path

from jupyterhub.spawner import LocalProcessSpawner
from traitlets import default, Unicode

class SUSpawner(LocalProcessSpawner):
    jupyter_dir_template = Unicode(
        "{home}/.jupyterhub/user/{username}",
        config=True,
        help="""
            Template to expand to set the user jupyter home.
            {username} is expanded to the jupyterhub username.
            {home} is expanded to the home directory.
        """,
    )

    jupyter_dir = Unicode(help="The jupyter home directory for the user.")

    @default("jupyter_dir")
    def _default_jupyter_dir(self):
        username = self.user.name
        home = str(Path.home())
        return self.jupyter_dir_template.format(username=username, home=home)

    def make_preexec_fn(self, name):
        def preexec():
            pass
        return preexec

    def user_env(self, env):
        env["JUPYTER_CONFIG_DIR"] = f"{self.jupyter_dir}"
        # env["JUPYTER_CONFIG_DIR"] = f"{self.jupyter_dir}/config"
        # env["JUPYTER_DATA_DIR"] = f"{self.jupyter_dir}/data"
        # env["JUPYTER_RUNTIME_DIR"] = f"{self.jupyter_dir}/runtime"
        return env

    async def move_certs(self, paths):
        return paths

from jupyterhub.auth import Authenticator
from traitlets import Unicode
from argon2 import PasswordHasher

class MILABAuthenticator(Authenticator):
    password_hash = Unicode(
        config=True,
        help="""
            Set a global password hash (argon2) for all users wanting to log in.
            This allows users with any username to log in with the same static password.
        """,
    )

    def is_admin(self, handler, authentication):
        return True

    async def authenticate(self, handler, data):
        if not self.password_hash:
            return None

        try:
            ph = PasswordHasher()
            ph.verify(self.password_hash, data["password"])
            return data["username"]
        except:
            pass

        return None

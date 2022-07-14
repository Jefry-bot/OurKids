from controllers.AuthController import AuthController
from controllers.UserController import UserController

auth = AuthController()
user = UserController()

CONTROLLERS = { "auth": auth, "user": user}

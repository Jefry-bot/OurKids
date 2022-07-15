from controllers.AuthController import AuthController
from controllers.ErrorController import ErrorController

auth = AuthController()
error = ErrorController()

CONTROLLERS = { "auth": auth, "error": error}

from controllers.AuthController import AuthController
from controllers.ErrorController import ErrorController
from controllers.ScreensController import ScreensController

auth = AuthController()
error = ErrorController()
screens = ScreensController()

CONTROLLERS = { "auth": auth, "error": error, "screens": screens}

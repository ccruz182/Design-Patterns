from factories.mac_factory import MacOSFactory
from factories.win_factory import WindowsFactory
from application import Application

def configure_application(os):
    if os == "win":
        factory = WindowsFactory()
    elif os == "mac":
        factory = MacOSFactory()

    return factory


win_app = Application(configure_application("win"))
win_app.paint()

macos_app = Application(configure_application("mac"))
macos_app.paint()
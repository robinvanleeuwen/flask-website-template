import inspect


class ColorTypes(object):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


log_level_definitions = {
    "DEBUG": 6,
    "INFO": 5,
    "VERBOSE": 4,
    "WARNING": 3,
    "ERROR": 2,
    "SILENT": 1,
}


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RsLogger(object, metaclass=Singleton):
    def __init__(self, log_level=None, log_to_screen=True):
        self.log_to_screen = log_to_screen

    def debug(self, message, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 6:
            formatted_message = (
                    ColorTypes.BOLD
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)
            self.write_to_logfile(message=formatted_message)

    def header(self, message, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 5:
            formatted_message = (
                    ColorTypes.BOLD
                    + ColorTypes.HEADER
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)
            self.write_to_logfile(message=formatted_message)

    def info(self, message, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 5:
            formatted_message = (
                    ColorTypes.OKBLUE
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)
            self.write_to_logfile(message=formatted_message)

    def ok(self, message, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 4:
            formatted_message = (
                    ColorTypes.OKGREEN
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)
            self.write_to_logfile(message=formatted_message)

    def warning(self, message, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 3:
            formatted_message = (
                    ColorTypes.WARNING
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)
            self.write_to_logfile(message=formatted_message)

    def fail(self, message, stop=False, **kwargs):
        from app import app

        log_level = app.config.get("LOGLEVEL")

        if log_level_definitions[log_level] >= 2:
            formatted_message = (
                    ColorTypes.FAIL
                    + inspect.stack()[1][3]
                    + "() : "
                    + str(message)
                    + ColorTypes.ENDC
            )
            if self.log_to_screen:
                print(formatted_message, **kwargs)

            if stop:
                return

            self.write_to_logfile(message=formatted_message)

    def write_to_logfile(self, message=None):
        from app import app

        if message:
            try:
                f = open(
                    app.config.get("LOGFILE", "/var/log/rawfare.log"), "a"
                )
                f.write(message + "\n")
            except Exception as e:
                self.fail(f"Could not write to logfile: {str(e)}", stop=True)

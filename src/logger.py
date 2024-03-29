from functools import wraps

from fastlogging import LogInit
from flask import request

from src.config import Config


class Logger:
    def __init__(self, filename="devika_agent.log"):
        config = Config()
        logs_dir = config.get_logs_dir()
<<<<<<< HEAD
        self.logger = LogInit(pathName=logs_dir + "/" + filename, console=True, colors=True)
=======
        self.logger = LogInit(pathName=logs_dir + "/devika_agent.log", console=True, colors=True)
        self.mode = "on"
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

    def read_log_file(self) -> str:
        with open(self.logger.pathName, "r") as file:
            return file.read()

    def info(self, message: str):
        self.logger.info(message)
        self.logger.flush()

    def error(self, message: str):
        self.logger.error(message)
        self.logger.flush()

    def warning(self, message: str):
        self.logger.warning(message)
        self.logger.flush()

    def debug(self, message: str):
        self.logger.debug(message)
        self.logger.flush()

    def exception(self, message: str):
        self.logger.exception(message)
        self.logger.flush()


def route_logger(logger: Logger):
    """
    Decorator factory that creates a decorator to log route entry and exit points.
    The decorator uses the provided logger to log the information.

    :param logger: The logger instance to use for logging.
    """

    log_enabled = Config().get_logging_rest_api()

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if logger.mode == "off":
                return func(*args, **kwargs)
            # Log entry point
            if log_enabled:
                logger.info(f"{request.path} {request.method}")

            # Call the actual route function
            response = func(*args, **kwargs)

            from werkzeug.wrappers import Response

            # Log exit point, including response summary if possible
            try:
<<<<<<< HEAD
                if log_enabled:
=======
                if isinstance(response, Response) and response.direct_passthrough:
                    logger.debug(f"{request.path} {request.method} - Response: File response")
                else:
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
                    response_summary = response.get_data(as_text=True)
                    logger.debug(f"{request.path} {request.method} - Response: {response_summary}")
            except Exception as e:
                logger.exception(f"{request.path} {request.method} - {e})")

            return response
        return wrapper
    return decorator

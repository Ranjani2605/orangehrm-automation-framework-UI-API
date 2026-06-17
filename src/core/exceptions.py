
class FramworkException(Exception):
    """Base exception for framework-level errors."""


class ConfigNotFoundException(FramworkException):
    """Raised when environment config file is missing."""

class InvalidBrowserException(FramworkException):
    """Raised when unsupported browser is selected."""

class UnsafeDBQueryException(FramworkException):
    """Raised when unsafe DB query is detected."""
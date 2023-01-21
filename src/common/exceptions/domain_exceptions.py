class DomainError(Exception):
    def __init__(self, message: str | None = None):
        super().__init__(message)


class EntityNotFound(DomainError):
    pass

class DomainError(Exception):
    def __init__(self, message: str | None = None):
        self.message = message
        super().__init__(message)


class EntityNotFound(DomainError):
    pass


class AccessError(DomainError):
    pass

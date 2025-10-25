class BaseError(Exception):
    def __init__(self, status_code:int, type:str, detail:str, is_operational:bool | None = True):
        self.status_code = status_code
        self.type = type
        self.detail = detail
        self.is_operational = is_operational

        super.__init__(self.detail)

class NotFoundError(BaseError):
    def __init__(self,  detail):
        super().__init__(
            status_code=404,
            type= 'RESOURCE_NOT_FOUND_ERR',
            detail=detail
        )
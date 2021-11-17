# multi level inheritance


class Response:
    def __init__(self, code):
        self.code = code


class SuccessResponse(Response):
    pass


class OKResponse(SuccessResponse):
    pass


class CreatedResponse(SuccessResponse):
    pass

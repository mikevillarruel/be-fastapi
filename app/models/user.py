import pydantic


class User(pydantic.BaseModel):
    id: int
    username: str
    password: str

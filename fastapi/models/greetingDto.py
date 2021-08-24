from pydantic import BaseModel

class GreetingDto(BaseModel):
    greetings: str = None
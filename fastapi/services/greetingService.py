from models.greetingDto import GreetingDto

class GreetingService():
    def greetings(self) -> str:
        dto = GreetingDto()
        dto.greetings = "Hi folks!"
        return dto
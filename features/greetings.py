from datetime import datetime


class Greetings:
    def __init__(self):
        self.now = datetime.now()

    def wish(self):
        hour_right_now = self.now.hour

        base_expression = "what can i do for you?"

        if hour_right_now <= 12 and hour_right_now >= 6:
            return "Good morning Sir, " + base_expression
        elif hour_right_now >= 12 and hour_right_now <= 18:
            return "Good afernoon Sir, " + base_expression
        else:
            return "Good evening Sir, " + base_expression

    def aboutMe(self):

        expression = """My name is SH. I m a simple virtual assistant.
         Simple as in I don't have Natural Language Processing capabilities
          but I can do simple tasks and automations such as reporting date
           and time or reporting weather forecast."""
        return expression
    

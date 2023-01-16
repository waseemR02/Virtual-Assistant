from datetime import datetime
import random


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

    def birthday_wish(self):
        """
        This method returns an expression when the query is : Today is my birthday.

        It returns an expression randomly chosen from a list.
        """
        quotes = [
            "Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!",
            """A wish for you on your birthday, whatever you ask may you receive, 
            whatever you seek may you find, whatever you wish may it be fulfilled
            on your birthday and always. Happy birthday!""",
            """Happy birthday! Your life is just about to pick up speed and blast off into the stratosphere. 
            Wear a seat belt and be sure to enjoy the journey. Happy birthday!""",
            """Count not the candles…see the lights they give. Count not the years, but the life you live. 
            Wishing you a wonderful time ahead. Happy birthday.""",
            """Forget the past; look forward to the future, for the best things are yet to come.""",
            """Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful
             tapestry of the world to make this year the best ever. Enjoy the ride.""",
            """You're older today than yesterday but younger than tomorrow, happy birthday!""",
            """As you get older three things happen. The first is your memory goes, and I can't remember the other two. Happy birthday!""",
            """Happy birthday! May your Instagram wall be filled with messages from people you never talk to."""
        ]

        base_expression = "Many Many Happy returns of the day to you. I have a quote for you. "
        expression = random.choice(quotes)

        return base_expression + expression

    def girlfriend(self):
        return "I am in relationship with Alexa since 4 years"

    def born(self):
        return "I was created on 4-January-2023 by professor Waseem"

    def enemy(self):
        return "I do not have enemies. In fact I love them, friends ask you questions and enemies question you."

    def strength(self):
        return

    def weakness(self):
        return "The biigest weakness of mine is not having a physical presence. I donot have the feature that makes me communicate face to face."

    def inspiration(self):
        return "My inspiration is professor Joseph Weizenbaum. He was the first person to create a natural language processing computer program or chatbot known as ELIZA. It was created to demonstrate that the communication between man and machine was superficial."

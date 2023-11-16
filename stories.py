"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["adjective", "plural_food_1", 'verb', 'noun', 'plural_food_2', 'color', 'animal', 'something_you_can_ride_in'],
    """Today I went to my favorite Taco Stand called the {adjective} {animal}.
    Unlike most food stands, they cook and prepare the food in a {something_you_can_ride_in}
     while you {verb}. The best thing on the menu is the {color} {noun}. Instead of ground beef
     they fill the taco with {plural_food_2}, cheese, and top it off with a salsa made from {plural_food_1}."""
)

story3 = Story(
    ['verb', 'adjective_1', 'adjective_2', 'place', 'color', 'time_of_day', 'food_1', 'food_2', 'plural_noun', 'number'],
    """Bats are so cool! They are {color}, {adjective_2} animals which have wings. They like to fly around at
     {time_of_day} which makes some people scared of them. But bats are {adjective_1}, and they don't want to
     hurt people. I have a pet bat that lives in {place}. I like to feed him {food_1} and {food_2}. He likes
     to {verb}. I am his favorite person, but he also likes {plural_noun}. I want to convince my parents to get me {number} more bats."""
)
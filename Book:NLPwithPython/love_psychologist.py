!pip install -U nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [r'(.*) happy because (.*)',
    ["%2. That's a good reason to feel happy! Tell me more.."]],

    [r'(.*) unhappy because (.*)',
    ["%3. Don't be sad. Find the positive side."]],

    [r'(.*) (unhappy|happy)',
    ["Ok. %1 %2. But why ?"]],

    [r'(.*) in love with (.*)',
    ["%1 in love with %2. %2 is handsome."]],

    [r'(.*) (like|love) (.*)',
    ["That's amazing! Tell me more!"]],

    [r'I hate (.*)',
    ["Relax..Let's discuss about it."]],

    [r'(.*) hates (.*)',
    ["All right! That seems important but %1 lose."]],

    [r'(.*)',
    ["%1. How do you feel about that?"]],

]
def love_psychologist():
  print("Hi, I'm your psychologist. What's wrong? ") 

  chat = Chat(pairs, reflections)
  chat.converse()
if __name__ == "__main__":
  love_psychologist()

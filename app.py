from flask import Flask
app = Flask(__name__)
person = input ('Name a person:')
adjective = input ('Name an adjective:')
adjective2 = input ('Name an adjective:')
noun = input ('Name a noun:')
adjective3 = input ('Name an adjective:')
noun2 = input ('Name an noun:')
adjective4 = input ('Name an adjective:')
adjective5 = input ('Name an adjective:')
verb = input ('Name a verb:')
verb2 = input ('Name a verb:')
person2 = input ('Name a person:')
verb3 = input ('Name an adjective:')
adjective6 = input ('Name an adjective:')
verb4 = input ('Name an verb:')

madlib = f"Yesterday, {person} and I went to the park. On our way to the {adjective} park we saw a {adjective2} {noun} on a bike. We also saw big {adjective3}. Once we got to the {adjective3} park, the sky turned {adjective4}. It started to {verb} and {verb2}. {person2} and I {verb3} all the way home. Tomorrow we will try to go to the {adjective5} park again and hope it doesn't {verb4}."

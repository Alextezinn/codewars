"""

The open/closed principle states that code should be closed for modification, yet open for extension.
That means you should be able to add new functionality to an object or method without altering it.

One way to achieve this is by using a lambda, which by nature is lazily bound to the lexical context.
Until you call a lambda, it is just a piece of data you can pass around.
"""
spoken = lambda greeting: "".join([greeting.capitalize(), "."])
shouted = lambda greeting: "".join([greeting.upper(), "!"])
whispered = lambda greeting: "".join([greeting.lower(), "."])

greet = lambda style, msg: style(msg)

from src.greeting import greeting

def test_default_greeting():
    assert greeting() == "Hello, Azure DevOps learner!"

def test_personalised_greeting():
    assert greeting("Mick") == "Hello, Mick!"

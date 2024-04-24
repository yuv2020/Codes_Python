from better_profanity import profanity

text = input("Enter some text:")
censored_text = profanity.censor(text)
print(f"Censored text: {censored_text}")

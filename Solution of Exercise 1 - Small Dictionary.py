# PROBLEM: WRITE A PROGRAM WHICH WILL HELP THE USER TO UNDERSTAND THE MEANING OF A FEW DIFFICULT ENGLISH WORDS.

print("Let's Improve our Vocabulary!!")
print("This is kind of a dictionary which will help you with the meaning of a few difficult English words.", "\n")

print("Please enter the word whose meaning you are willing to know (from the printed words below).")
print("[i] Bilk")
print("[ii] Candor")
print("[iii] Covet")
print("[iv] Dearth")
print("[v] Fatuous", "\n")

n = input().capitalize()


Dictionary = {"Bilk": "Cheat somebody out of what is due, especially money",
             "Candor": "The quality of being honest or straight forward",
             "Covet": "Wish, long, or crave for.",
             "Dearth": "An insufficient quantity or number",
             "Fatuous": "Devoid of Intelligence"}

print(n, end=": ")
print(Dictionary.get(n))

print("\n Thanks for using.")

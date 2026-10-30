# string concatenation (aka how we put strings together)
# i want a string to say "come play ______"
# game = "" # variable

# game = input ("what game do you want to play?")
# print f"come play{game}"

game = input ("what game do you want play")
adj = input ("give an adjective for how you would describe the game")
famousperson = input ("give me a famous person")

madlib = f"do you want to play {game}? I really think {game} is really good because its so {adj} please come play it would be really awkward if it was just me and {famousperson}"

print (madlib)
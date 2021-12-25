import random

print("""Hello, this is a flip a coin game.
0 - to play
1 - to exit""")
startGame = int(input())
coin = ["head", "tail"]
if startGame == 0:
    num = random.randint(0,1)
    print("The face of the coin is:",coin[num])
if startGame == 1:
    print("bye, let's play next time")
if startGame < 0 or startGame > 1:
    print("dont do it")

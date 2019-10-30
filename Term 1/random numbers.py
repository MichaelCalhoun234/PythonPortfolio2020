import random
def coin_toss():
    for i in range (50):
       
        coinToss = random.randint(1,2)

        if coinToss == 1:
            print ("heads")

        elif coinToss == 2:
            print("tails")

coin_toss()
                    




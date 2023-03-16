pizzas = int(input())


happiness = {1:0, 2:1}

def getHappy(pizza):
    if pizza in happiness:
        return happiness[pizza]

    if pizza % 2 == 0:
        happiness[pizza] = (pizza // 2) ** 2 + getHappy(pizza // 2) * 2
        return happiness[pizza]
    elif pizza % 2 == 1:
        happiness[pizza] = (pizza // 2 * (pizza // 2 + 1)) + getHappy(pizza // 2) + getHappy(pizza // 2 + 1)
        return happiness[pizza]


print(getHappy(pizzas))

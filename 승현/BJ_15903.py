n, m = map(int, input().split())
card = list(map(int, input().split()))

for _ in range(m):
    card.sort()
    card_sum = card[0] + card[1]
    card[0] = card_sum
    card[1] = card_sum


print(sum(card))
"""
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2

and assumed that each pair of rabbits reaches maturity in one month and
produces a single pair of offspring (one male, one female) each subsequent
month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed
number of months. See Figure 4 for a depiction of a rabbit tree in which
rabbits live for three months (meaning that they reproduce only twice before
dying).

Given: Positive integers n≤100 and m≤20
Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
"""

pairs_born_per_pair = 1
months = 92
rabbit_lifespan = 18

pairs_total = 0
pairs_adult = 0
pairs_maturing = 0
pairs_to_be_born = 1
pairs_dying_in_n_months = {}

for month in range(0, rabbit_lifespan+1):
    pairs_dying_in_n_months[month] = 0

pairs_dying_in_n_months[rabbit_lifespan] = pairs_to_be_born

for i in range(0, months):
    if pairs_maturing > 0:
        pairs_adult += pairs_maturing
        pairs_maturing = 0

    if pairs_to_be_born > 0:
        pairs_total += pairs_to_be_born
        pairs_maturing = pairs_to_be_born

        max_lifespan = len(pairs_dying_in_n_months)
        print("lifespans: " + str(max_lifespan))
        pairs_dying_in_n_months[max_lifespan-1] += pairs_maturing

    keys = list(pairs_dying_in_n_months.keys())
    for key in range(0, len(keys)):
        if key is 0 and pairs_dying_in_n_months[key] > 0:
            print("some rabbits died :( (" + str(pairs_dying_in_n_months[key]) + ")")
            pairs_adult -= pairs_dying_in_n_months[key]
            pairs_dying_in_n_months[key] = 0

        if key+1 < len(keys):
            pairs_dying_in_n_months[key] = pairs_dying_in_n_months.get(key+1)
            pairs_dying_in_n_months[key+1] = 0
        else:
            pairs_dying_in_n_months[key] = 0

        print(pairs_dying_in_n_months.values())

    pairs_to_be_born = pairs_adult * pairs_born_per_pair

print("")
print(pairs_total)

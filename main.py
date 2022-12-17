from itertools import permutations
import math


# find the best option
def find_best_option(options: list[float]):
    best_option = -1
    max_values = -math.inf
    for i in range(0, len(options)):
        if max_values < options[i]:
            max_values = options[i]
            best_option = i
    return best_option, max_values


# this function find allocation by VCG algorithm
def do_VCG(values: list[list[float]]):
    """"
         >>> [do_VCG([[5, 12], [7, 10]])]
         [['player 0 get object 1 in price 3', 'player 1 get object 0 in price 0']]
         >>> [do_VCG([[9, 3, 8], [12, 10, 2], [5, 7, 6]])]
         [['player 0 get object 2 in price 0', 'player 1 get object 0 in price 1', 'player 2 get object 1 in price 0']]
         >>> [do_VCG([[4, 3, 11, 7], [5, 8, 2, 8], [0, 17, 3, 8], [8, 12, 3, 6]])]
         [['player 0 get object 2 in price 0', 'player 1 get object 3 in price 0', 'player 2 get object 1 in price 4', 'player 3 get object 0 in price 0']]
        """
    options = []
    num_of_players = []
    # create permutation of all the players
    for i in range(0, len(values)):
        num_of_players.append(i)
    perm = list(permutations(num_of_players))
    for i in range(0, len(perm)):  # pass over all the options
        sum = 0
        for j in range(0, len(values)):  # pass over all the values in this option
            sum += values[perm[i][j]][j]
        options.append(sum)
    best_option, max_values = find_best_option(options)
    sum_without = []
    for k in range(0, len(values)):  # pass over all the players
        sum_without_k = []
        for i in range(0, len(perm)):  # pass over all the options
            sum = 0
            for j in range(0, len(values)):  # pass over all the values in this option
                if k != perm[i][j]:
                    sum += values[perm[i][j]][j]
            sum_without_k.append(sum)
        sum_without.append(sum_without_k)
    best_option_without = []
    # find the best option without player k
    for k in range(0, len(sum_without)):
        curr_best, curr_max = find_best_option(sum_without[k])
        best_option_without.append((curr_best, curr_max))
    ans = []
    # enter the answer to list
    for k in range(0, len(best_option_without)):
        price = best_option_without[k][1] - sum_without[k][best_option]
        ans.append("player " + str(k) + " get object " + str(perm[best_option].index(k)) + " in price " + str(price))
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()

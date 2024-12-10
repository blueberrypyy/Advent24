lst_1 = []
lst_2 = []
final = []


def part1():

    # sort both lists
    with open('day1.txt', 'r') as day1:
            for line in day1:
                line = line.split()
                lst_1.append(line[0])
                lst_2.append(line[1])

    lst_1 = sorted(lst_1)
    lst_2 = sorted(lst_2)

    x = 0
    for num1 in lst_1:
        ans = int(num1) - int(lst_2[x])
        final.append(ans)
        x += 1

    print(sum(final))


def part2():
    lst_1 = []
    lst_2 = []
    similarity = {}
    final = []


    # sort both lists
    with open('day1.txt', 'r') as day1:
        for line in day1:
            line = line.split()
            lst_1.append(line[0])
            lst_2.append(line[1])
        lst_1 = sorted(lst_1)
        lst_2 = sorted(lst_2)

        for num1 in lst_1:
            x = 0
            for num2 in lst_2:
                if num1 == num2:
                    x += 1
                    similarity[int(num1)] = int(x)
                    #print(num1, " == ", num2)
                else: continue

        #print(similarity)

        total = [] 
        for item in similarity:
            print(item, similarity[item])
            product = item * similarity[item]
            total.append(product)
        print(sum(total))






    #for item in lst_1:
    #    if item in lst_2:
            #print('Found', item)

part2()



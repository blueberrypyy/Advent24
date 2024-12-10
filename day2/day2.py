
def is_safe(num_list, safe_reports=0):
    increasing = False
    decreasing = False
    safe = bool
    for i, num in enumerate(num_list):
        #print(f'{num_list2[i-1]} + {num}')
        #print(i, item)
        if i > 0:
            if num_list[i-1] < num: increasing = True           # Check if increasing
            if num_list[i-1] > num: decreasing = True           # Check if decreasing
            if abs(num_list[i-1] - num) > 3: safe = False       # Check if distance > 3
            elif num_list[i-1] == num: safe = False             # Check if equal

        if increasing == True and decreasing == True: safe = False
    if safe != False: safe_reports += 1
    #print(num_list, 'Safe:', safe, 'total:', safe_reports)
    return safe_reports


total_safe = 0
with open('input.txt', 'r') as fil:
    for line in fil:
        nums_list = [int(x) for x in line.split()]      # Convert to int
        total_safe += is_safe(nums_list)

print('Safe reports:', total_safe)




#Prints a maximum set of activities that can be done by a 
#single person, one at a time
#n --> Total number of activities 
#s[]--> An array that contains start time of all activities 
#f[] --> An array that contains finish time of all activities 


def find_activities(arr):
    n = len(arr)
    arr.sort(key = lambda x: x[1])

    i = 0

    selected = [arr[i]]
    for j in range(1, n):
        start_time_next_activity = arr[j][0]
        end_time_prev_activity = arr[i][1]

        if start_time_next_activity >= end_time_prev_activity:
            selected.append(arr[j])
            i = j

    return selected


arr = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
print(find_activities(arr))


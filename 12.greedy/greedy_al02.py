
# Problem 1: Maximum Meetings
def maximum_meetings(start, end):
    if len(start) != len(end):
        raise ValueError("Start and end lists must have equal lengths.")

    meetings = sorted(
        zip(start, end),
        key=lambda meeting: meeting[1]
    )

    count = 0
    last_end = float("-inf")

    for meeting_start, meeting_end in meetings:
        if meeting_start > last_end:
            count += 1
            last_end = meeting_end

    return count


# Problem 2: Assign Cookies
def assign_cookies(children, cookies):
    children.sort()
    cookies.sort()

    child_index = 0
    cookie_index = 0

    while child_index < len(children) and cookie_index < len(cookies):
        if cookies[cookie_index] >= children[child_index]:
            child_index += 1

        cookie_index += 1

    return child_index


# Problem 3: Lemonade Change
def lemonade_change(bills):
    five = 0
    ten = 0

    for bill in bills:
        if bill == 5:
            five += 1

        elif bill == 10:
            if five == 0:
                return False

            five -= 1
            ten += 1

        elif bill == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

        else:
            return False

    return True


if __name__ == "__main__":
    print("Maximum Meetings:")
    print(maximum_meetings(
        [1, 3, 0, 5, 8, 5],
        [2, 4, 6, 7, 9, 9]
    ))

    print("\nAssign Cookies:")
    print(assign_cookies([1, 2, 3], [1, 1]))
    print(assign_cookies([1, 2], [1, 2, 3]))

    print("\nLemonade Change:")
    print(lemonade_change([5, 5, 5, 10, 20]))
    print(lemonade_change([5, 5, 10, 10, 20]))

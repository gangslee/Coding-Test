
def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)

    for i in range(len(seller)):
        if amount[i] == 0:
            continue

        current = amount[i]*100
        person = seller[i]

        while True:
            temp = int(current*0.1)
            answer[enroll.index(person)] += (current - temp)

            current = temp

            person = referral[enroll.index(person)]

            if person == "-":
                break

    return answer


er = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
ref = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
sel = ["young", "john", "tod", "emily", "mary"]
amt = [12, 4, 2, 5, 10]

print(solution(er, ref, sel, amt))

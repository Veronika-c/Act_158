
def pathway1_result(lit, al, bio, grade):
    proficient = 1500
    result = ["Analysis of Pathway 1:"]
    if lit >= 1500 and bio >= 1500 and al >= 1500:
        result.append("you passed all your keystones you qualify for pathway 1")
    elif grade == 12:
        result.append("since you are not taking keystones in senoir year it's closed for you")
    else:
        if lit < 1500:
            result.append("You need " + str(1500 - lit) + " more points on the literature.")
        if bio < 1500:
            result.append("You need " + str(1500 - bio) + " more points on the biology.")
        if al < 1500:
            result.append("You need " + str(1500 - al) + " more points on the algebra.")
    return result

#print(pathway1_result(1564, 900, 1545, 11))

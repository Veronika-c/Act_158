def get_scores():
    with open("appdata.txt","r") as file:
        data = []
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
    return data


def pathway1_result(lit, al, bio, grade, pass_l, pass_a, pass_b):
    proficient = 1500
    result = ["Analysis of Pathway 1:"]
    if lit >= pass_l and bio >= pass_b and al >= pass_a:
        result.append("you passed all your keystones you qualify for pathway 1")
    elif grade == 12:
        result.append("since you are not taking keystones in senoir year it's closed for you")
    else:
        if lit < pass_l:
            result.append("You need " + str(1500 - lit) + " more points on the literature.")
        if bio < pass_b:
            result.append("You need " + str(1500 - bio) + " more points on the biology.")
        if al < pass_a:
            result.append("You need " + str(1500 - al) + " more points on the algebra.")
    return result

#print(pathway1_result(1564, 900, 1545, 11))
print(get_scores())

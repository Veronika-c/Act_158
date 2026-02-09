def get_scores():
    with open("appdata.txt","r") as file:
        data = []
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
        data.append(int(file.readline()))
    return data


def pathway1_result(lit, al, bio, grade, pass_l, pass_a, pass_b):
    
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


def pathway2_result(lit, al, bio, grade, pass_l, pass_a, pass_b, combo,  basic_l, basic_a, basic_b ):
    pro1 = False
    no_bb = False
    combo_score = False
    result = []

    if lit >= pass_l or al >= pass_a or bio >= pass_b:
        pro1 = True

    if lit >= basic_l and al >= basic_a and bio >= basic_b:
        no_bb = True

    if lit + bio + al >= combo:
        combo_score = True

    if pro1 and no_bb and combo_score:
        result.append("You meet all the requirments for Pathway 2")

    if not pro1:
        list = [bio , lit, al]
        list.sort()
        if list[-1] == bio:
            result.append("You need at least one proficient keystone ")
            result.append("You are closest to proficient in biology you need " + str(pass_b - bio) + " more points")

            
    
    

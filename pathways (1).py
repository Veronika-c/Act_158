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
        return result

    if grade == 12:
         result.append(" Since you're in 12 grade, you can no longer improve your keystone scores. Please check another pathway.")
         return result

    if not pro1:
        list = [bio , lit, al]
        list.sort()
        if list[-1] == bio:
            result.append("You need at least one proficient keystone ")
            result.append("You are closest to proficient in biology you need " + str(pass_b - bio) + " more points")

        if list[-1] == lit:
            result.append("You need at least one proficient keystone ")
            result.append("You are closest to proficient in literature you need " + str(pass_l - lit) + " more points")

        if list[-1] == al:
            result.append("You need at least one proficient keystone ")
            result.append("You are closest to proficient in algebra you need " + str(pass_a - al) + " more points.")

    if lit < basic_l:
        result.append(" Your literature score is below basic, You need " + str(basic_l - lit) + " more points. ")

    if bio < basic_b:
        result.append(" Your biology score is below basic, You need " + str(basic_b - bio) + " more points. ")

    if al < basic_a:
        result.append(" Your algebra score is below basic, You need " + str(basic_a - al) + " more points. ")


    if not combo_score:
        result.append(" Your combined score needs to be " + str(combo) + ". You need " + str(combo - (lit + bio + al)) + " more points.")

    return result

#print (pathway2_result(1409, 1390, 1480, 11, 1500, 1500, 1500, 4452, 1444 , 1439, 1460 ))


def pathway3_result(cte, cert, grade):
    result = []
    if (grade == 11 or grade == 12) and not cte:
        result.append(" You can no longer enroll in a CTE program, this pathway is closed. ")
        return result
    if cte and cert:
        result.append(" Since you are in a CTE Program and earned an industry certification you qualify for this pathway.")

    if cte and not cert:
        result.append(" You have not recieved an industry certification yet, you will need one in order to complete this pathway.")

    if not cte and cert:
        result.append(" You are not in a CTE program but have earned a industry certification, therefore you should check pathway 5.")


    if (grade == 9 or grade == 10) and not cte :
        result.append(" If you are in 9th or 10th grade and will like to join a CTE program talk to your counselor about opportunities in your district.")
    return result

print(pathway3_result( True, False , 10))

    

    

    
        
        
        
    
    



            
    
    

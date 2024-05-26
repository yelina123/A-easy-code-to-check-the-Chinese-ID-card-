def LenNum(a,lenid): 
    b = len(str(a))
    #如果 b!=lenid 就要求重新输入a
    while b != lenid:
        print("您输入的位数不对，应为",lenid,"位。请重新输入。(tips:如果你没有完整的身份证号，请将你不知道的位数用'0'填充。)")
        while True:
            print()
            a=InputNum.InputNumber(Prompt='请输入身份证号(tips:如果你没有完整的身份证号,请将你不知道的位数用0填充。)')
            b = LenNum(a,lenid)
            if b==lenid:
                break
        break
    return a
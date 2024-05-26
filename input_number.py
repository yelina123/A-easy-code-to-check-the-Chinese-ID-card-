def InputNumber(Prompt):
    while True:
        try:
            
            a = int(input(Prompt))
            break
        except ValueError:
            print("输入不是整数，请重新输入。")
    return a
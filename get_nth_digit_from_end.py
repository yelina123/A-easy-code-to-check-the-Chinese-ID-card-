def get_nth_digit_from_end(a, n):#求倒数第n位的a的数字
    # 将整数转换为字符串
    a_str = str(a)
    # 检查n是否超过整数的长度
    if n > len(a_str):
        return None  # 返回None表示无效
    # 取得倒数第n位的字符，并转换为整数
    else:
        return int(a_str[-n])

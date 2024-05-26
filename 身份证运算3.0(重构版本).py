
import citylist
import get_nth_digit_from_end as g
import input_number as InputNum
import LenNum
cityok=0
province=0
Prompt=0
   

#正式开始运行
print("感谢使用身份证工具箱")
print('请选择模式','1==解析')

mode=(input())
if mode=='1':
#    print('working')
    print('正在解析...')
    Prompt='请输入身份证号，应该有十八位。(tips:如果你没有完整的身份证号,请将你不知道的位数用0填充。)'
    print()
    a=InputNum.InputNumber(Prompt='请输入身份证号，应该有十八位。(tips:如果你没有完整的身份证号,请将你不知道的位数用0填充。)')
    lenid=18
    LenNum.LenNum(a,lenid)
    a1 = g.get_nth_digit_from_end(a, 1)#这里反过来的，这是最后一位
    a2 = g.get_nth_digit_from_end(a, 2)
    a3 = g.get_nth_digit_from_end(a, 3)
    a4 = g.get_nth_digit_from_end(a, 4)
    a5 = g.get_nth_digit_from_end(a, 5)
    a6 = g.get_nth_digit_from_end(a, 6)
    a7 = g.get_nth_digit_from_end(a, 7)
    a8 = g.get_nth_digit_from_end(a, 8)
    a9 = g.get_nth_digit_from_end(a, 9)
    a10 =g.get_nth_digit_from_end(a, 10)
    a11 =g.get_nth_digit_from_end(a, 11)
    a12 =g.get_nth_digit_from_end(a, 12)
    a13 =g.get_nth_digit_from_end(a, 13)
    a14 =g.get_nth_digit_from_end(a, 14)
    a15 =g.get_nth_digit_from_end(a, 15)
    a16 =g.get_nth_digit_from_end(a, 16)
    a17 =g.get_nth_digit_from_end(a, 17)
    a18 =g.get_nth_digit_from_end(a, 18)
    nummall=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9)+str(a10)+str(a11)+str(a12)+str(a13)+str(a14)+str(a15)+str(a16)+str(a17)+str(a18)
    yyyy=str(a12)+str(a11)+str(a10)+str(a9)
    mm=str(a8)+str(a7)
    dd=str(a6)+str(a5)
    #print(nummall)
    #print(yyyy)
    #print(mm)
    #print(dd)
    # 获取身份证号码前四位
    id_num =str(a18)+str(a17)
    id_city=str(a18)+str(a17)+str(a16)+str(a15)+str(a14)+str(a13)
    #print(id_num)
#    print('你的出生日期是','year',yyyy,'month',mm,'day',dd)


    # 解析身份证号码前四位对应的地区
    if id_num in citylist.id_prefix:
       province=1
       #print(f'该身份证号码的省级行政单位是{id_prefix[id_num]}')

    else:
        print('无法解析该身份证号码前四位对应的省份',id_num)
        province=0

    
    id_city=str(id_city)
    if id_city in citylist.id_citylist:
       cityok=1
       #print(f'该身份证号码的省级行政单位是{id_city[id_citylist]}')

    else:
        print('无法解析该身份证号码前6位对应的city',id_city)
        cityok=0

    #解析最后一位（核心算法）
    b_01, b_02, b_03, b_04, b_05, b_06, b_07, b_08, b_09, b_10, b_11, b_12, b_13, b_14, b_15, b_16, b_17, b_18 = \
    a18, a17, a16, a15, a14, a13, a12, a11, a10, a9, a8, a7, a6, a5, a4, a3, a2, a1
    c_01, c_02, c_03, c_04, c_05, c_06, c_07, c_08, c_09, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17 = \
    b_01 * 7, b_02 * 9, b_03 * 10, b_04 * 5, b_05 * 8, b_06 * 4, b_07 * 2, b_08 * 1, b_09 * 6, b_10 * 3, b_11 * 7, b_12 * 9, b_13 * 10, b_14 * 5, b_15 * 8, b_16 * 4, b_17 * 2
    he=c_01+c_02+c_03+c_04+c_05+c_06+c_07+c_08+c_09+c_10+c_11+c_12+c_13+c_14+c_15+c_16+c_17

    he=he%11
    if he==0:
        he=1
    elif he==1:
        he=0
    elif he==2:
        he='X'
    elif he==3:
        he=9
    elif he==4:
        he=8
    elif he==5:
        he=7
    elif he==6:
        he=6
    elif he==7:
        he=5
    elif he==8:
        he=4
    elif he==9:
        he=3
    elif he==10:
        he=2
#    b_all=str(b_01)+str(b_02)+str(b_03)+str(b_04)+str(b_05)+str(b_06)+str(b_07)+str(b_08)+str(b_09)+str(b_10)+str(b_11)+str(b_12)+str(b_13)+str(b_14)+str(b_15)+str(b_16)+str(b_17)
    if str(he)==str(a1):
        #print('最后一位为',he)
        jym='true'#jym:校验码
    else:
        #print('身份证最后一位有问题啊,应改为',he)
        jym='false,应为',str(he)
    #判断性别
    if b_17 % 2 == 0:
        #print('女性')
        xingbie='女'
    else:
        #print('男性')
        xingbie='男'
    print('--------------------')
    print('result:')
    if cityok==0 and province==1:

        print('出生日期:',yyyy,mm,dd,";性别:",xingbie,';所在省级行政单位:',citylist.id_prefix[id_num],'；实验性功能：城市：','not in list',';校验码校验',jym)
    elif province==0 and cityok==0:
        print('出生日期:',yyyy,mm,dd,";性别:",xingbie,';所在省级行政单位:not in list','；实验性功能：城市:Not in list',';校验码校验',jym)
    elif province==1 and cityok==1:
        print('出生日期:',yyyy,mm,dd,";性别:",xingbie,';所在省级行政单位:',citylist.id_prefix[id_num],'；实验性功能：城市(精确到区):',citylist.id_citylist[id_city],';校验码校验',jym)
    else:
        print('未知错误发生')
    print("*请注意:如果你不确定的位置使用了0来填充,则不能确保程序结果全部正确。")
    print('联系作者:https://space.bilibili.com/626752761')
    print('--------------------')
elif mode!=1:
    print('正在开发中')
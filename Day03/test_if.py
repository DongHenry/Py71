chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# year = int(input("请用户输入出生年份"))
# if(chinese_zodiac[year % 12]) == "狗":
#     print("狗年大吉")

# for循环的遍历演示
for year in range(1995, 2020):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

"""
识别十二生肖，根据年份判断十二生肖
"""

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[5])
# print(chinese_zodiac[3:9])

year = 2019
print(chinese_zodiac[year % 12])

# 序列的 in / not in 操作
print('猪' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# 序列的 " + " 操作
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + ' dhenry')

# 序列的 “ * ” 操作
print(" Dhenry " * 3)

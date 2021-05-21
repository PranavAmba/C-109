import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics as stx

dice_result = []
count = []

for i in range(0,1000):

    dice1 = random.randint(1,6)
   #
   #  print ( dice1 )

    dice2= random.randint(1,6)
   # print (dice2)

    dice_result.append(dice1+dice2)
    count.append(i)

#print(dice_result)

#fig=px.bar(x=dice_result,y=count)
#fig.show()

mean=sum(dice_result)/len(dice_result)
print (mean)

median=stx.median(dice_result)
print (median)

mode=stx.mode(dice_result)
print(mode)

std_deviation=stx.stdev(dice_result)
print(std_deviation)

fig=ff.create_distplot([dice_result],['Result'])
fig.show()
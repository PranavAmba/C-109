import pandas as pd
import statistics as stx
import csv

df=pd.read_csv('data.csv')

height_list=df['Height(Inches)'].to_list()
weight_list=df['Weight(Pounds)'].to_list()

#mean

height_mean=stx.mean(height_list)
weight_mean=stx.mean(weight_list)

height_median=stx.median(height_list)
weight_median=stx.median(weight_list)

height_mode=stx.mode(height_list)
weight_mode=stx.mode(height_list)

height_stdev=stx.stdev(height_list)
weight_stdev=stx.stdev(weight_list)

print('mean,median,mode of height is {} , {} and {} respectively'.format(height_mean,height_median,height_mode))
print('mean,median,mode of weight is {} , {} and {} respectively'.format(weight_mean,weight_median,weight_mode))

#1,2,3 standard deviation for height

height_first_stdev_start,height_first_stdev_end= height_mean-height_stdev,height_mean+height_stdev
height_second_stdev_start,height_second_stdev_end= height_mean-(2*height_stdev),height_mean+(2*height_stdev)
height_third_stdev_start,height_third_stdev_end= height_mean-(3*height_stdev),height_mean+(3*height_stdev)

#1,2,3 standard deviation for weight

weight_first_stdev_start,weight_first_stdev_end= weight_mean-weight_stdev,weight_mean+weight_stdev
weight_second_stdev_start,weight_second_stdev_end= weight_mean-(2*weight_stdev),weight_mean+(2*weight_stdev)
weight_third_stdev_start,weight_third_stdev_end= weight_mean-(3*weight_stdev),weight_mean+(3*weight_stdev)

# % of data within 1,2,3 standard deviation for height

height_list_of_data_within_1_stdev=[result for result in height_list if result>height_first_stdev_start and result <height_first_stdev_end]
height_list_of_data_within_2_stdev=[result for result in height_list if result>height_second_stdev_start and result <height_second_stdev_end]
height_list_of_data_within_3_stdev=[result for result in height_list if result>height_third_stdev_start and result <height_third_stdev_end]

# % of data within 1,2,3 standard deviation for weight

weight_list_of_data_within_1_stdev=[result for result in weight_list if result>weight_first_stdev_start and result <weight_first_stdev_end]
weight_list_of_data_within_2_stdev=[result for result in weight_list if result>weight_second_stdev_start and result <weight_second_stdev_end]
weight_list_of_data_within_3_stdev=[result for result in weight_list if result>weight_third_stdev_start and result <weight_third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_stdev)*100.0/len(height_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_stdev)*100.0/len(weight_list)))
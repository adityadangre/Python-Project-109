import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

df = pd.read_csv('projectdata.csv')

math_list = df['math score'].tolist()
read_list = df['reading score'].tolist()
write_list = df['writing score'].tolist()

math_mean = statistics.mean(math_list)
read_mean = statistics.mean(read_list)
write_mean = statistics.mean(write_list)

math_sd = statistics.stdev(math_list)
read_sd = statistics.stdev(read_list)
write_sd = statistics.stdev(write_list)

math_median = statistics.median(math_list)
read_median = statistics.median(read_list)
write_median = statistics.median(write_list)

math_1st_sd_s, math_1st_sd_e = math_mean - math_sd, math_mean + math_sd
math_2nd_sd_s, math_2nd_sd_e= math_mean - 2 * math_sd, math_mean + 2 * math_sd
math_3rd_sd_s, math_3rd_sd_e = math_mean - 3 * math_sd, math_mean + 3* math_sd

math_list_1st_sd = [result for result in  math_list if result > math_1st_sd_s and result < math_1st_sd_e]
math_list_2nd_sd = [result for result in  math_list if result > math_2nd_sd_s and result < math_2nd_sd_e]
math_list_3rd_sd = [result for result in  math_list if result > math_3rd_sd_s and result < math_3rd_sd_e]


write_1st_sd_s, write_1st_sd_e = write_mean - write_sd, write_mean + write_sd
write_2nd_sd_s, write_2nd_sd_e= write_mean - 2 * write_sd, write_mean + 2 * write_sd
write_3rd_sd_s, write_3rd_sd_e = write_mean - 3 * write_sd, write_mean + 3* write_sd

write_list_1st_sd = [result for result in  write_list if result > write_1st_sd_s and result < write_1st_sd_e]
write_list_2nd_sd = [result for result in  write_list if result > write_2nd_sd_s and result < write_2nd_sd_e]
write_list_3rd_sd = [result for result in  write_list if result > write_3rd_sd_s and result < write_3rd_sd_e]


read_1st_sd_s, read_1st_sd_e = read_mean - read_sd, read_mean + read_sd
read_2nd_sd_s, read_2nd_sd_e= read_mean - 2 * read_sd, read_mean + 2 * read_sd
read_3rd_sd_s, read_3rd_sd_e = read_mean - 3 * read_sd, read_mean + 3* read_sd

read_list_1st_sd = [result for result in  read_list if result > read_1st_sd_s and result < read_1st_sd_e]
read_list_2nd_sd = [result for result in  read_list if result > read_2nd_sd_s and result < read_2nd_sd_e]
read_list_3rd_sd = [result for result in  read_list if result > read_3rd_sd_s and result < read_3rd_sd_e]

print("---------Mean of Math, Reading & Writing Score-------")
print('Mean of Math Score is', math_mean)
print('Mean of Reading Score is', read_mean)
print('Mean of Writing Score is', write_mean, '\n')

print("---------Standard Deviation of Math, Reading & Writing Score-------")
print('Standard Deviation of Math Score is', math_sd)
print('Standard Deviation of Reading Score is', read_sd)
print('Standard Deviation of Writing Score is', write_sd, '\n')

print("---------Median of Math, Reading & Writing Score-------")
print('Median of Math Score is', math_median)
print('Median of Reading Score is', read_median)
print('Median of Writing Score is', write_median, '\n')

print("---------1st, 2nd, 3rd  SD of Maths Score-------")
print('Percentage of data of Maths Score which lies in first standard deviation is', len(math_list_1st_sd * 100) / len(math_list))
print('Percentage of data of Maths Score which lies in second standard deviation is', len(math_list_2nd_sd * 100) / len(math_list))
print('Percentage of data of Maths Score which lies in third standard deviation is', len(math_list_3rd_sd * 100) / len(math_list), '\n')

print("---------1st, 2nd, 3rd  SD of Reading Score-------")
print('Percentage of data of Reading Score which lies in first standard deviation is', len(read_list_1st_sd * 100) / len(read_list))
print('Percentage of data of Reading Score which lies in second standard deviation is', len(read_list_2nd_sd * 100) / len(read_list))
print('Percentage of data of Reading Score which lies in third standard deviation is', len(read_list_3rd_sd * 100) / len(read_list), '\n')

print("---------1st, 2nd, 3rd  SD of Writing Score-------")
print('Percentage of data of Writing Score which lies in first standard deviation is', len(write_list_1st_sd * 100) / len(write_list))
print('Percentage of data of Writing Score which lies in second standard deviation is', len(write_list_2nd_sd * 100) / len(write_list))
print('Percentage of data of Writing Score which lies in third standard deviation is', len(write_list_3rd_sd * 100) / len(write_list), '\n')



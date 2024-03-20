def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2, 4, 6, 9, 100, 9009] #You make

mapped_times2 = map(times2, my_list)
mapped_times3 = map(div2, my_list)
mapped_times4 = map(exp2, my_list)

mapped_times2_list = list(mapped_times2)
mapped_times3_list = list(mapped_times3)
mapped_times4_list = list(mapped_times4)
print(mapped_times2_list)
print(mapped_times3_list)
print(mapped_times4_list)
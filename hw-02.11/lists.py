#hw
#1
empty_list=[]
print(empty_list)
#2
list=[1,2,3,4,5]
print(list)
#3
list=[1,2,3,4,5,6,7,8,9,10]
print(len(list))
#4
item1,*rest,last_item=list
print(item1)
print(last_item)
print(rest)
#5
print("Name \tage \theight \tfamily status \taddress")
print("Akniet \t16 \t168 \tsingle        \tMaulenova street 92")
#6
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
#10
it_companies[4]="Ozon"
print(it_companies)
#11
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.append("SAP")
print(it_companies)
#12
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.insert(3,"SAP")
print(it_companies)
#13 didn't understand the question
#14 didn't understand the question
#15
print("Apple" in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies[:3])
#19
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies[4:])
#20
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies[3:4])
#21
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.pop(0)
print(it_companies)
#22
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.pop(3)
print(it_companies)
#23
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.pop(6)
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies 
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#27
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

#lvl 2
#1
ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)

min_age=ages[0]
max_age=ages[-1]
print(min_age)
print(max_age)

ages.extend([min_age,max_age])
print(ages)

middle1= ages[len(ages)//2]
middle2=ages[len(ages)//2-1]
midian_age=(middle1 + middle2)/2 
print(midian_age)

average_age=sum(ages) / len(ages)
print(average_age)

age_range= max_age - min_age
print(age_range)

min_average=abs(min_age - average_age)
max_average=abs(max_age - average_age)
print(min_average)
print(max_average)

#2 i couldn't do it



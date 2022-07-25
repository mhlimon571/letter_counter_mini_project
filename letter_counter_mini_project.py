print("I am an application that takes massage and latter from you.\
My task is too count how many times this letter occured and calculate the percentage.")

user_massage = input("Please enter your massage : ")
user_letter = input("Please enter a letter : ")

count_result = user_massage.count(user_letter)
length_result = len(user_massage)
percentage_result = (count_result/length_result)*100

print("your massage is : ",user_massage)

result_1 = "The total count value of {value_1} is : {value_2}".format(value_1 = user_letter,value_2 = count_result)
print(result_1)

result_2 = "The total percentage of {value_3} is : {value_4}".format(value_3 = user_letter,value_4 = percentage_result)
print(result_2)
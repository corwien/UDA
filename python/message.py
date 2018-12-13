# -*- coding:utf-8 -*-


"""
写一个完成以下操作的脚本：

 1. 请求用户输入三次。一次是名字列表，一次是未交作业数量列表，一次是分数列表。使用该输入创建 names、assignments 和 grades 列表。
 2. 使用循环为每个学生输出一条信息并包含正确的值。潜在分数是 2 乘以未交作业数加上当前分数。
"""


names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

mess_str = """
Hi {},

This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.

"""

for i in range(4):
    name = names[i]
    assign = assignments[i]
    grade = grades[i]
    next_grade = assgin * 2 + grade

    print(mess_str.format(name,assgin,grade,next_grade))

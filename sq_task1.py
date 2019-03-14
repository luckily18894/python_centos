import sqlite3


conn = sqlite3.connect('homework.sqlite')
cursor = conn.cursor()

user_notify = """
请输入查询选项：
输入 1 ：查询整个数据库
输入 2 ：基于姓名查询
输入 3 ：基于年龄查询
输入 4 ：基于作业数查询
输入 0 ：退出
"""
while True:
    print(user_notify)
    user_input = input('请选择:')
    if user_input == '0':
        break
    elif user_input == '1':
        cursor.execute("select * from students_homework_info")
        res = cursor.fetchall()
        if not res:
            print('学员信息未找到!')
        for student in res:
            print('学员姓名:{0} 学院年龄:{1} 学员作业数:{2}'.format(student[0], student[1], student[2]))
    elif user_input == '2':
        user_sn = input('请输入学员姓名:')
        if not user_sn:
            continue
        cursor.execute("select * from students_homework_info where 姓名 = ?", [user_sn])
        res = cursor.fetchall()
        if not res:
            print('学员信息未找到!')
        for student in res:
            print('学员姓名:{0} 学员年龄:{1} 学员作业数:{2}'.format(student[0], student[1], student[2]))
    elif user_input == '3':
        user_age = input('搜索大于输入年龄的学员，请输入学员年龄:')
        if not user_age:
            continue
        cursor.execute("select * from students_homework_info where 年龄 > ?", [user_age])
        res = cursor.fetchall()
        if not res:
            print('学员信息未找到!')
        for student in res:
            print('学员姓名:{0} 学员年龄:{1} 学员作业数:{2}'.format(student[0], student[1], student[2]))
    elif user_input == '4':
        user_homework = input('搜索大于输入作业数的学员，请输入作业数:')
        if not user_homework:
            continue
        cursor.execute("select * from students_homework_info where 作业数 > ?", [user_homework])
        res = cursor.fetchall()
        if not res:
            print('学员信息未找到!')
        for student in res:
            print('学员姓名:{0} 学员年龄:{1} 学员作业数:{2}'.format(student[0], student[1], student[2]))
    else:
        print('输入错误！请重试！')


from tkinter import *
from tkinter import ttk
from student import Student
from courses import Course
from admin import Admin
import json

students = []
admins = []
courses = []
logged_in_student = Student
logged_in_admin = Admin
background ="#b3daff"
text_color = "#003566"
entry_color = "#e6f3ff"

logged_in = 0

#for loading student data


def from_dict_admin(dictionary):
    return Admin(dictionary["username"], dictionary["password"])


def to_dict_admin(self):
    return {
        "username" : self.username ,
        "password" : self.password
    }


def save_admin_data():
    dictionary = {"admins": [to_dict_admin(admin) for admin in admins]}
    with open("admins.json", "w") as f:
        json.dump(dictionary, f)


def load_admin_data():
    with open("admins.json") as f:
        dictionary = json.load(f)
    for admin in dictionary['admins']:
        admins.append(from_dict_admin(admin))


def save_students_data():
    list_of_student = [to_dict_student(student) for student in students]
    dictonary = {"students": list_of_student}
    with open("students.json",'w') as f:
        json.dump(dictonary, f)


def from_dict_course(dictionary):

    return Course(dictionary["name"],
                  dictionary["code"],
                  dictionary["group_code"],
                  dictionary["capacity"],
                  dictionary["enrolled"],
                  dictionary["day"],
                  dictionary["hour"]
                  )


def to_dict_course(self):
    return {
        "name" : self.name,
        "code" : self.code,
        "group_code" : self.group_code,
        "capacity" : self.capacity,
        "enrolled" : self.enrolled,
        "day" : self.day,
        "hour" : self.hour
        }


def to_dict_student(self):
    return {
            "name" : self.name,
            "last_name" : self.last_name,
            "father_name" : self.father_name,
            "student_num" : self.student_num,
            "password" : self.password,
            "id_num" : self.id_num,
            "entrance_year" : self.entrance_year,
            "major" : self.major,
            "university" : self.university,
            "college" : self.college,
            "phone_number" : self.phone_number,
            "address" : self.address,
            "card_num" : self.card_num,
            "religion" : self.religion,
            "father_number" : self.father_number,
            "mothers_number" : self.mother_number,
            "courses" : [to_dict_course(course) for course in self.courses]
            }


def from_dict_student(dictionary):
    course_list = []
    for course in dictionary["courses"]:
        course_list.append(from_dict_course(course))
    return Student(dictionary["name"],
                   dictionary["last_name"],
                   dictionary["father_name"],
                   dictionary["student_num"],
                   dictionary["id_num"],
                   dictionary["entrance_year"],
                   dictionary["major"],
                   dictionary["university"],
                   dictionary["college"],
                   dictionary["password"],
                   dictionary["phone_number"],
                   dictionary["address"],
                   dictionary["card_num"],
                   dictionary["religion"],
                   dictionary["father_number"],
                   dictionary["mothers_number"],
                   course_list
                   )


def load_students():
    with open("students.json") as f:
        dictionary = json.load(f)
    for student in dictionary['students']:
        students.append(from_dict_student(student))

#for loading course data
def save_courses():
    list_of_courses = [to_dict_course(course) for course in courses]
    dictionary = {"courses": list_of_courses}
    with open("courses.json", 'w') as f:
        json.dump(dictionary, f)


def load_courses():
    with open("courses.json") as f:
        dictionary = json.load(f)
    for course_dict in dictionary['courses']:
        courses.append(from_dict_course(course_dict))


# for loging in
def submiting(iusername,ipassword):
    if login.get() == 1:
        for student in students:
            if student.student_num == iusername:
                if student.password == ipassword:
                    global logged_in
                    global  logged_in_student
                    logged_in_student = student
                    logged_in = 1
                    root.destroy()
                    return
                elif student.password != ipassword:
                    logged_in = 0
                    Label(login_page,text="رمزعبور اشتباه است",bg=background,fg=text_color).grid(row=4,column=1)
                    return
        Label(login_page, text="نام کاربری صحیح نیست", bg=background, fg=text_color).grid(row=4, column=1)

    if login.get() == 2:
        for admin in admins:
            if admin.username == iusername:
                if admin.password == ipassword:
                    global logged_in_admin
                    logged_in_admin = admin
                    logged_in = 2
                    root.destroy()
                    return
                elif admin.password != ipassword:
                    logged_in = 0
                    Label(login_page,text="رمزعبور اشتباه است",bg=background,fg=text_color).grid(row=4,column=1)
                    return
        Label(login_page, text="نام کاربری صحیح نیست", bg=background, fg=text_color).grid(row=4, column=1)

# student functions
def open_profile():
    ViewFrame.pack_forget()
    ProfileFrame.pack_forget()
    selectionFrame.pack_forget()
    my_courses_Frame.pack_forget()
    editor_Frame.pack_forget()

    for detail in ProfileFrame.winfo_children():
        detail.destroy()
    name_lable = Label(ProfileFrame, text="نام: " + logged_in_student.name, bg=background).pack(anchor=E)
    family_name_lable = Label(ProfileFrame, text="نام خانواگی: " + logged_in_student.last_name, bg=background).pack(
        anchor=E)
    father_name_lable = Label(ProfileFrame, text="نام پدر: " + logged_in_student.father_name, bg=background).pack(
        anchor=E)
    student_num_lable = Label(ProfileFrame, text="شماره دانشجویی: " + logged_in_student.student_num,
                              bg=background).pack(anchor=E)
    id_num_lable = Label(ProfileFrame, text="کد ملی: " + logged_in_student.id_num, bg=background).pack(anchor=E)
    entrance_year_lable = Label(ProfileFrame, text="سال ورود: " + logged_in_student.entrance_year, bg=background).pack(
        anchor=E)
    major_lable = Label(ProfileFrame, text="رشته: " + logged_in_student.major, bg=background).pack(anchor=E)
    university_lable = Label(ProfileFrame, text="دانشگاه: " + logged_in_student.university, bg=background).pack(
        anchor=E)
    college_lable = Label(ProfileFrame, text="دانشکده: " + logged_in_student.college, bg=background).pack(anchor=E)
    ProfileFrame.pack(anchor=CENTER,fill=BOTH, expand=1)



def open_courses():
    ViewFrame.pack_forget()
    ProfileFrame.pack_forget()
    selectionFrame.pack_forget()
    my_courses_Frame.pack_forget()
    editor_Frame.pack_forget()

    for course_widget in ViewFrame.winfo_children():
        course_widget.destroy()
    # scrollbar config
    main_frame = Frame(ViewFrame, bg=background)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, bg=background)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, bg=background)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, bg=background)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    for course in courses:
        course_name_name = Label(second_frame, text="نام درس: " + course.name, bg=background, width=60).pack(
            anchor=CENTER)
        course_code_label = Label(second_frame, text="کد درس: " + course.code, bg=background).pack(anchor=CENTER)
        course_group_label = Label(second_frame, text="شماره گروه: " + course.group_code, bg=background).pack(
            anchor=CENTER)
        course_capacity_label = Label(second_frame, text="ظرفیت: " + course.capacity, bg=background).pack(anchor=CENTER)
        course_day_label = Label(second_frame, text="روز: " + course.day, bg=background).pack(anchor=CENTER)
        course_hour_label = Label(second_frame, text="ساعت: " + course.hour, bg=background).pack(anchor=CENTER)
        devider_label = Label(second_frame, text="_______________________________________" * 2, bg=background).pack(
            anchor=CENTER)
    ViewFrame.pack(anchor=CENTER,fill=BOTH, expand=1)


def open_selection():
    ViewFrame.pack_forget()
    ProfileFrame.pack_forget()
    selectionFrame.pack_forget()
    my_courses_Frame.pack_forget()
    editor_Frame.pack_forget()

    selectionFrame.pack(anchor=CENTER, fill=BOTH, expand=1)
    for ws in SelectionOptons.winfo_children():
        ws.destroy()
    group_number = Entry(SelectionOptons, width=30, bg=entry_color)
    group_number.grid(row=5, column=1)
    course_number = Entry(SelectionOptons, width=30, bg=entry_color)
    course_number.grid(row=4, column=1)
    Label(SelectionOptons, text="شماره گروه", bg=background).grid(row=5, column=2)
    Label(SelectionOptons, text="کد درس", bg=background).grid(row=4, column=2)
    Label(SelectionOptons, text="", bg=background).grid(row=0, column=1)
    Label(SelectionOptons, text="", bg=background).grid(row=1, column=1)
    Label(SelectionOptons, text="", bg=background).grid(row=2, column=1)
    Label(SelectionOptons, text="انتخاب واحد", bg=background).grid(row=3, column=1)
    select = Button(SelectionOptons, text="ثبت کلاس", width=15, bg=entry_color,
                    command=lambda: select_course(group_number.get(), course_number.get())).grid(row=6,
                                                                                                          column=1)

def open_my_courses():
    ViewFrame.pack_forget()
    ProfileFrame.pack_forget()
    selectionFrame.pack_forget()
    my_courses_Frame.pack_forget()
    editor_Frame.pack_forget()

    my_courses_Frame.pack(anchor=CENTER, fill=BOTH, expand=1)

    for i in my_courses_Frame.winfo_children():
        i.destroy()
    if len(logged_in_student.courses) != 0:
        main_c_frame = Frame(my_courses_Frame, bg=background)
        main_c_frame.pack(fill=BOTH, expand=1)

        my_c_canvas = Canvas(main_c_frame, bg=background)
        my_c_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_c_frame, orient=VERTICAL, command=my_c_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_c_canvas.configure(yscrollcommand=my_scrollbar.set, bg=background)
        my_c_canvas.bind('<Configure>', lambda e: my_c_canvas.configure(scrollregion=my_c_canvas.bbox("all")))

        second_c_frame = Frame(my_c_canvas, bg=background)

        my_c_canvas.create_window((0, 0), window=second_c_frame, anchor="nw")

        for a in logged_in_student.courses:
            Label(second_c_frame, text="نام درس: " + a.name, bg=background, width=60).pack(anchor=CENTER)
            Label(second_c_frame, text="کد درس: " + a.code, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="شماره گروه: " + a.group_code, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="روز: " + a.day, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="ساعت: " + a.hour, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="_______________________________________" * 2, bg=background).pack(anchor=CENTER)
    else:
        Label(my_courses_Frame, text="شما درسی را انتخاب نکرده اید!" * 2, bg=background).pack(anchor=CENTER)


def open_editor():
    religion_var = StringVar()
    religion_var.set(logged_in_student.religion)
    ViewFrame.pack_forget()
    ProfileFrame.pack_forget()
    selectionFrame.pack_forget()
    my_courses_Frame.pack_forget()
    editor_Frame.pack_forget()
    for edit in editor_Frame.winfo_children():
        edit.destroy()
    editor_Frame.pack(anchor=CENTER, fill=BOTH, expand=1)
    phone_number = Entry(editor_Frame , width = 15 ,bg=entry_color)
    address = Entry(editor_Frame , width = 15 ,bg=entry_color)
    card_number = Entry(editor_Frame , width = 15 ,bg=entry_color)
    religion = OptionMenu(editor_Frame , religion_var, "مسلمان(شیعه)","مسلمان(سنی)","مسیحی","یهودی","زرتشتی","ارمنی")
    religion.configure(width=10,padx=3)
    father_phone_number = Entry(editor_Frame , width = 15 ,bg=entry_color)
    mother_phone_number = Entry(editor_Frame , width = 15 ,bg=entry_color)
    phone_number.insert(0,str(logged_in_student.phone_number))
    address.insert(0,str(logged_in_student.address))
    card_number.insert(0,logged_in_student.card_num)
    father_phone_number.insert(0,logged_in_student.father_number)
    mother_phone_number.insert(0,logged_in_student.mother_number)
    Label(editor_Frame,text=":مشخصات قابل تغییر ",anchor=E, width = 15,bg=background).grid(row=1,column=4,sticky=E)
    Label(editor_Frame,text=":تلفن ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=2,column=4,sticky=E)
    Label(editor_Frame,text=":آدرس محل سکونت ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=3,column=4,sticky=E)
    Label(editor_Frame,text=":شماره کارت بانکی ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=4,column=4,sticky=E)
    Label(editor_Frame,text=":مذهب ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=5,column=4,sticky=E)
    Label(editor_Frame,text=":شماره تلفن پدر ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=6,column=4,sticky=E)
    Label(editor_Frame,text=":شماره تلفن مادر ",anchor=E, width = 15,bg=text_color,fg=background).grid(row=7,column=4,sticky=E)
    Label(editor_Frame,bg=background).grid(row=2,column=2,padx=179)
    phone_number.grid(row=2,column=3)
    address.grid(row=3,column=3)
    card_number.grid(row=4,column=3)
    religion.grid(row=5,column=3)
    father_phone_number.grid(row=6,column=3)
    mother_phone_number.grid(row=7,column=3)
    save = Button(editor_Frame,text="ذخیره اطلاعات",bg=text_color,fg=background, width = 11,command=lambda :saving(
        phone_number.get(),address.get(),card_number.get(),religion_var.get(),father_phone_number.get()
        , mother_phone_number.get()
    ))
    save.grid(row=8,column=3)


def saving(phonenumber,address,cardnumber,religion_,fatherphone,motherphone):
    logged_in_student.phone_number=phonenumber
    logged_in_student.address=address
    logged_in_student.card_num=cardnumber
    logged_in_student.religion=religion_
    logged_in_student.father_number=fatherphone
    logged_in_student.mother_number=motherphone
    Label(editor_Frame,text=".اطلاعات شما با موفقیت بروز رسانی شد",bg=background,fg="Green").grid(row=8,column=2)
    save_students_data()





def select_course(group_code,code):
    global courses
    for error in errors.winfo_children():
        error.destroy()
    for a in courses:
        if a.code == code:
            if a.group_code==group_code:
                global logged_in_student
                if int(a.capacity) != int(a.enrolled):
                    for b in logged_in_student.courses:
                        if b.code == a.code:
                            error4 = Label(errors, text="درس " + a.name + " قبلا برای شما ثبت شده", bg=background)
                            error4.pack(anchor=CENTER)

                            return
                    if logged_in_student.courses.count(a) == 0:
                        a.enrolled = str(int(a.enrolled)+1)
                        logged_in_student.courses.append(a)
                        error1 = Label(errors,text="درس "+ a.name +" موفقیت انتخاب شد",bg=background,fg="Green")
                        error1.pack(anchor=CENTER)
                        save_students_data()
                        save_courses()
                        return

                elif int(a.capacity) == int(a.enrolled):
                    error5 = Label(errors, text=" درس " + a.name + " پر است", bg=background,fg="Red")
                    error5.pack(anchor=CENTER)
                    return


    erorr2 = Label(errors, text="کد درس نامعتبر", bg=background,fg="Red")
    erorr2.pack(anchor=CENTER)


#admin functions
def signup_student(
        name,
        last_name,
        father_name,
        student_num,
        id_num,
        entrance_year,
        major,
        university,
        college,
        password,
        phone_number,
        address,
        card_num,
        religion,
        father_number,
        mothers_number,
        ):
    if name=="" or last_name=="" or father_name=="" or student_num==""or id_num=="" or entrance_year==""or major=="" or university==""or college=="" or password=="":
        Label(signup_frame,text="تمامی قسمت های ستاره دار باید پر شوند",bg="Red").grid(row=17,column=0)
        return
    for student in students:
        if student_num == student.student_num:
            Label(signup_frame,text="از این شماره دانشجویی قبلا استفاده شده",bg="Red").grid(row=18,column=0)
            return


    students.append(Student(name,
        last_name,
        father_name,
        student_num,
        id_num,
        entrance_year,
        major,
        university,
        college,
        password,
        phone_number,
        address,
        card_num,
        religion,
        father_number,
        mothers_number,
        ))
    save_students_data()
    Label(signup_frame, text="دانشجو با موفقیت ثبت شد", bg="Green").grid(row=18, column=0)


def show_signup():
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()



    for widget in signup_frame.winfo_children():
        widget.destroy()

    signup_frame.pack(anchor=CENTER, fill=BOTH, expand=1)
    admin_window.geometry("590x430")

    new_religion_var = StringVar()
    new_religion_var.set("مسلمان(شیعه)")
    Label(signup_frame, bg=background, text=" ", padx=108).grid(row=2, column=0)
    Label(signup_frame, bg=background, text="ثبت نام دانشجوی جدید").grid(row=2, column=2)
    Label(signup_frame, bg=background, text="نام*", width=12).grid(row=3, column=2)
    Label(signup_frame, bg=background, text="نام خانوادگی*", width=12).grid(row=4, column=2)
    Label(signup_frame, bg=background, text="نام پدر*", width=12).grid(row=5, column=2)
    Label(signup_frame, bg=background, text="شماره دانشجویی*", width=12).grid(row=6, column=2)
    Label(signup_frame, bg=background, text="کد ملی*", width=12).grid(row=7, column=2)
    Label(signup_frame, bg=background, text="شماره تلفن همراه", width=12).grid(row=8, column=2)
    Label(signup_frame, bg=background, text="تلفن پدر", width=12).grid(row=9, column=2)
    Label(signup_frame, bg=background, text="تلفن مادر", width=12).grid(row=10, column=2)
    Label(signup_frame, bg=background, text="مذهب", width=12).grid(row=11, column=2)
    Label(signup_frame, bg=background, text="شماره کارت بانکی", width=12).grid(row=12, column=2)
    Label(signup_frame, bg=background, text="محل سکونت", width=12).grid(row=13, column=2)
    Label(signup_frame, bg=background, text="رشته*", width=12).grid(row=14, column=2)
    Label(signup_frame, bg=background, text="تاریخ تولد", width=12).grid(row=15, column=2)
    Label(signup_frame, bg=background, text="سال ورود*", width=12).grid(row=16, column=2)
    Label(signup_frame, bg=background, text="دانشگاه*", width=12).grid(row=17, column=2)
    Label(signup_frame, bg=background, text="دانشکده*", width=12).grid(row=18, column=2)
    Label(signup_frame, bg=background, text="رمز عبور*", width=12).grid(row=19, column=2)

    new_name = Entry(signup_frame, bg=entry_color)
    new_lastname = Entry(signup_frame, bg=entry_color)
    new_father_name = Entry(signup_frame, bg=entry_color)
    new_student_num = Entry(signup_frame, bg=entry_color)
    new_id_num = Entry(signup_frame, bg=entry_color)
    new_phone_number = Entry(signup_frame, bg=entry_color)
    new_father_number = Entry(signup_frame, bg=entry_color)
    new_mother_number = Entry(signup_frame, bg=entry_color)
    new_religion = OptionMenu(signup_frame, new_religion_var, "مسلمان(شیعه)", "مسلمان(سنی)", "مسیحی", "یهودی", "زرتشتی",
                              "ارمنی")
    new_religion.configure(width=13, padx=3, bg=entry_color)
    new_card_num = Entry(signup_frame, bg=entry_color)
    new_address = Entry(signup_frame, bg=entry_color)
    new_major = Entry(signup_frame, bg=entry_color)
    new_birthday = Entry(signup_frame, bg=entry_color)
    new_entryyear = Entry(signup_frame, bg=entry_color)
    new_entryyear.insert(0,"1399")
    new_university = Entry(signup_frame, bg=entry_color)
    new_college = Entry(signup_frame, bg=entry_color)
    new_password = Entry(signup_frame, bg=entry_color)
    new_name.grid(row=3, column=1)
    new_lastname.grid(row=4, column=1)
    new_father_name.grid(row=5, column=1)
    new_student_num.grid(row=6, column=1)
    new_id_num.grid(row=7, column=1)
    new_phone_number.grid(row=8, column=1)
    new_father_number.grid(row=9, column=1)
    new_mother_number.grid(row=10, column=1)
    new_religion.grid(row=11, column=1)
    new_card_num.grid(row=12, column=1)
    new_address.grid(row=13, column=1)
    new_major.grid(row=14, column=1)
    new_birthday.grid(row=15, column=1)
    new_entryyear.grid(row=16, column=1)
    new_university.grid(row=17, column=1)
    new_college.grid(row=18, column=1)
    new_password.grid(row=19, column=1)

    signup_new_student = Button(signup_frame, bg=text_color, fg=background, text="ثبت نام دانشجوی جدید", command=lambda :
    signup_student(
        new_name.get(),
        new_lastname.get(),
        new_father_name.get(),
        new_student_num.get(),
        new_id_num.get(),
        new_entryyear.get(),
        new_major.get(),
        new_university.get(),
        new_college.get(),
        new_password.get(),
        new_phone_number.get(),
        new_address.get(),
        new_card_num.get(),
        new_religion_var.get(),
        new_father_number.get(),
        new_mother_number.get()
        ))
    signup_new_student.grid(row=19,column=0)


def signup_admin_new(username,password):
    if username == "":
        Label(admin_signup_frame,text="نام کاربری کاربر جدید را وارد کنید",bg=background,fg="Red",width=32).grid(row=5,column=1)
        return
    elif password == "":
        Label(admin_signup_frame,text="رمز عبور کاربر جدید را وارد کنید",bg=background,fg="Red",width=32).grid(row=5,column=1)
        return
    for admin in admins:
        if username == admin.username:
            Label(admin_signup_frame, text="این نام کاربری قبلا انتخاب شده", bg=background, fg="Red",
                  width=22).grid(row=5, column=1)
            return
    admins.append(Admin(username, password))
    save_admin_data()
    Label(admin_signup_frame,text="ادمین به صورت موفقیت آمیز ثبت شد",bg=background,fg="Green",width=32).grid(row=5,column=1)


def show_admin_signup():
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()


    admin_window.geometry("590x340")

    for widget in admin_signup_frame.winfo_children():
        widget.destroy()
    admin_signup_frame.pack(anchor=CENTER, fill=BOTH, expand=1)
    Label(admin_signup_frame, bg=background, width=32).grid(row=5,
                                                                                                                 column=1)
    Label(admin_signup_frame,text=" ",padx=45,pady=40,bg=background).grid(row=1,column=0)
    Label(admin_signup_frame,text=":نام کاربری",bg=background).grid(row=2,column=2)
    Label(admin_signup_frame,text=":رمز عبور",bg=background).grid(row=3,column=2)
    new_admin_username = Entry(admin_signup_frame,bg=entry_color)
    new_admin_username.grid(row=2,column=1)
    new_admin_password = Entry(admin_signup_frame,bg=entry_color)
    new_admin_password.grid(row=3,column=1)
    signup_admin= Button(admin_signup_frame,text="ثبت نام",bg=text_color,fg=background,command=lambda :signup_admin_new(new_admin_username.get(),new_admin_password.get()))
    signup_admin.grid(row=4,column=1)


def submit_edit(entry,
            new_name,
            new_lastname,
            new_father_name,
            new_student_num,
            new_id_num,
            new_phone_number,
            new_father_number,
            new_mother_number,
            new_religion,
            new_card_num,
            new_address,
            new_major,
            new_entryyear,
            new_university,
            new_college,
            new_password,
                ):
    for widget in edit_err.winfo_children():
        widget.destroy()

    edit_err.pack(anchor=CENTER,fill=BOTH, expand=1)

    for student in students:
        if student.student_num == entry:
            student.name = new_name
            student.last_name = new_lastname
            student.father_name = new_father_name
            student.student_num = new_student_num
            student.password = new_password
            student.id_num = new_id_num
            student.entrance_year = new_entryyear
            student.major = new_major
            student.university = new_university
            student.college = new_college
            student.phone_number = new_phone_number
            student.address = new_address
            student.card_num = new_card_num
            student.religion = new_religion
            student.father_number = new_father_number
            student.mother_number = new_mother_number
            save_students_data()
            Label(edit_err, bg=background, text="ثبت موفقیت آمیز", width=12,fg="Green").pack()


def search(entry):
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()



    for widget in result_frame.winfo_children():
        widget.destroy()
    admin_window.geometry("590x450")
    show_students_frame.pack(anchor=CENTER,fill=BOTH, expand=1)
    result_frame.pack(anchor=CENTER,fill=BOTH, expand=1)
    errors.pack(anchor=CENTER,fill=BOTH, expand=1)
    for student in students:
        if student.student_num == entry:
            new_religion_var = StringVar()
            new_religion_var.set(student.religion)
            Label(result_frame, bg=background, text=" ", padx=110).grid(row=2, column=0)
            Label(result_frame, bg=background, text="نام*", width=12).grid(row=3, column=2)
            Label(result_frame, bg=background, text="نام خانوادگی*", width=12).grid(row=4, column=2)
            Label(result_frame, bg=background, text="نام پدر*", width=12).grid(row=5, column=2)
            Label(result_frame, bg=background, text="شماره دانشجویی*", width=12).grid(row=6, column=2)
            Label(result_frame, bg=background, text="کد ملی*", width=12).grid(row=7, column=2)
            Label(result_frame, bg=background, text="شماره تلفن همراه", width=12).grid(row=8, column=2)
            Label(result_frame, bg=background, text="تلفن پدر", width=12).grid(row=9, column=2)
            Label(result_frame, bg=background, text="تلفن مادر", width=12).grid(row=10, column=2)
            Label(result_frame, bg=background, text="مذهب", width=12).grid(row=11, column=2)
            Label(result_frame, bg=background, text="شماره کارت بانکی", width=12).grid(row=12, column=2)
            Label(result_frame, bg=background, text="محل سکونت", width=12).grid(row=13, column=2)
            Label(result_frame, bg=background, text="رشته*", width=12).grid(row=14, column=2)
            Label(result_frame, bg=background, text="سال ورود*", width=12).grid(row=16, column=2)
            Label(result_frame, bg=background, text="دانشگاه*", width=12).grid(row=17, column=2)
            Label(result_frame, bg=background, text="دانشکده*", width=12).grid(row=18, column=2)
            Label(result_frame, bg=background, text="رمز عبور*", width=12).grid(row=19, column=2)

            new_name = Entry(result_frame, bg=entry_color)
            new_lastname = Entry(result_frame, bg=entry_color)
            new_father_name = Entry(result_frame, bg=entry_color)
            new_student_num = Entry(result_frame, bg=entry_color)
            new_id_num = Entry(result_frame, bg=entry_color)
            new_phone_number = Entry(result_frame, bg=entry_color)
            new_father_number = Entry(result_frame, bg=entry_color)
            new_mother_number = Entry(result_frame, bg=entry_color)
            new_religion = OptionMenu(result_frame, new_religion_var, "مسلمان(شیعه)", "مسلمان(سنی)", "مسیحی", "یهودی",
                                      "زرتشتی",
                                      "ارمنی")
            new_religion.configure(width=13, padx=3, bg=entry_color)
            new_card_num = Entry(result_frame, bg=entry_color)
            new_address = Entry(result_frame, bg=entry_color)
            new_major = Entry(result_frame, bg=entry_color)
            new_birthday = Entry(result_frame, bg=entry_color)
            new_entryyear = Entry(result_frame, bg=entry_color)
            if(student.entrance_year==""):
                new_entryyear.insert(0, "1399")
            new_university = Entry(result_frame, bg=entry_color)
            new_college = Entry(result_frame, bg=entry_color)
            new_password = Entry(result_frame, bg=entry_color)
            new_name.grid(row=3, column=1)
            new_lastname.grid(row=4, column=1)
            new_father_name.grid(row=5, column=1)
            new_student_num.grid(row=6, column=1)
            new_id_num.grid(row=7, column=1)
            new_phone_number.grid(row=8, column=1)
            new_father_number.grid(row=9, column=1)
            new_mother_number.grid(row=10, column=1)
            new_religion.grid(row=11, column=1)
            new_card_num.grid(row=12, column=1)
            new_address.grid(row=13, column=1)
            new_major.grid(row=14, column=1)
            new_entryyear.grid(row=16, column=1)
            new_university.grid(row=17, column=1)
            new_college.grid(row=18, column=1)
            new_password.grid(row=19, column=1)

            new_name.insert(0,student.name)
            new_lastname.insert(0,student.last_name)
            new_father_name.insert(0,student.father_name)
            new_student_num.insert(0,student.student_num)
            new_id_num.insert(0,student.id_num)
            new_phone_number.insert(0,student.phone_number)
            new_father_number.insert(0,student.father_number)
            new_mother_number.insert(0,student.mother_number)

            new_card_num.insert(0,student.card_num)
            new_address.insert(0,student.address)
            new_major.insert(0,student.major)
            new_entryyear.insert(0,student.entrance_year)
            new_university.insert(0,student.university)
            new_college.insert(0,student.college)
            new_password.insert(0,student.password)
            signup_new_student = Button(result_frame, bg=text_color, fg=background, text="ثبت تغییرات",
                                        command=lambda :submit_edit(entry,
            new_name.get(),
            new_lastname.get(),
            new_father_name.get(),
            new_student_num.get(),
            new_id_num.get(),
            new_phone_number.get(),
            new_father_number.get(),
            new_mother_number.get(),
            new_religion_var.get(),
            new_card_num.get(),
            new_address.get(),
            new_major.get(),
            new_entryyear.get(),
            new_university.get(),
            new_college.get(),
            new_password.get(),
                ))
            signup_new_student.grid(row=19, column=0)


def show_students():
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()


    for widget in result_frame.winfo_children():
        widget.destroy()
    for wid in search_frame.winfo_children():
        wid.destroy()
    admin_window.geometry("590x340")
    show_students_frame.pack(anchor=CENTER,fill=BOTH, expand=1)
    search_frame.pack(anchor=CENTER,fill=BOTH, expand=1)
    search_entry=Entry(search_frame,bg=entry_color,width=20)
    search_button=Button(search_frame,bg=text_color,fg=background,text="جستجو",command=lambda :search(search_entry.get()))
    search_button.grid(row=1,column=1)
    search_entry.grid(row=1,column=2)


def open_students():
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()

    show_students_list_frame.pack(anchor=CENTER, fill=BOTH, expand=1)
    admin_window.geometry("590x300")

    for i in show_students_list_frame.winfo_children():
        i.destroy()
    if len(students) != 0:
        main_c_frame = Frame(show_students_list_frame, bg=background)
        main_c_frame.pack(fill=BOTH, expand=1)

        my_c_canvas = Canvas(main_c_frame, bg=background)
        my_c_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_c_frame, orient=VERTICAL, command=my_c_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_c_canvas.configure(yscrollcommand=my_scrollbar.set, bg=background)
        my_c_canvas.bind('<Configure>', lambda e: my_c_canvas.configure(scrollregion=my_c_canvas.bbox("all")))

        second_c_frame = Frame(my_c_canvas, bg=background)

        my_c_canvas.create_window((0, 0), window=second_c_frame, anchor="nw")

        for student in students:
            Label(second_c_frame, text="نام: " + student.name, bg=background, width=60).pack(anchor=CENTER)
            Label(second_c_frame, text="نام خاوادگی: " + student.last_name, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="شماره دانشجویی: " + student.student_num, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="کدملی: " + student.id_num, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="سال ورود: " + student.entrance_year, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="رشته: " + student.major, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="دانشگاه: " + student.university, bg=background).pack(anchor=CENTER)
            Label(second_c_frame, text="دانشکده: " + student.college, bg=background).pack(anchor=CENTER)

            Label(second_c_frame, text="_______________________________________" * 2, bg=background).pack(anchor=CENTER)
    else:
        Label(show_students_list_frame, text="هیچ دانشجویی برای نمایش وجود ندارد" * 2, bg=background).pack(anchor=CENTER)


def open_courses_admin():

    course_window = Toplevel()
    course_window.title("درس ها")
    # scrollbar config
    main_frame = Frame(course_window, bg=background)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, bg=background)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, bg=background)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, bg=background)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    for course in courses:
        course_name_name = Label(second_frame, text="نام درس: " + course.name, bg=background, width=60).pack(
            anchor=CENTER)
        course_code_label = Label(second_frame, text="کد درس: " + course.code, bg=background).pack(anchor=CENTER)
        course_group_label = Label(second_frame, text="شماره گروه: " + course.group_code, bg=background).pack(
            anchor=CENTER)
        course_capacity_label = Label(second_frame, text="ظرفیت: " + course.capacity, bg=background).pack(anchor=CENTER)
        course_day_label = Label(second_frame, text="روز: " + course.day, bg=background).pack(anchor=CENTER)
        course_hour_label = Label(second_frame, text="ساعت: " + course.hour, bg=background).pack(anchor=CENTER)
        devider_label = Label(second_frame, text="_______________________________________" * 2, bg=background).pack(
            anchor=CENTER)


def open_chosen_course(code,group_num):
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    chosen_course_frame.pack(anchor=E,fill=BOTH, expand=1)
    for widget in chosen_course_frame.winfo_children():
        widget.destroy()

    def find_course(c, g):
        for course in courses:
            if course.code == c and course.group_code == g:
                return "yes"
        return "no"

    def save_course_changes(course_name,
                            course_code,
                            course_group,
                            course_capacity,
                            course_day,
                            course_hour):
        course.name = course_name
        course.code = course_code
        course.group_code = course_group
        course.capacity = course_capacity
        course.day = course_day
        course.hour = course_hour
        save_courses()
        Label(chosen_course_frame, text="تغییرات ذخیره شد", bg=background,fg="Green").grid(row=8, column=0)

    course_name = Entry(chosen_course_frame, bg=entry_color)
    course_code = Entry(chosen_course_frame, bg=entry_color)
    course_group = Entry(chosen_course_frame, bg=entry_color)
    course_capacity = Entry(chosen_course_frame, bg=entry_color)
    course_day = Entry(chosen_course_frame, bg=entry_color)
    course_hour = Entry(chosen_course_frame, bg=entry_color)
    if find_course(code, group_num) == "yes":
        for course in courses:
            if course.code == code and course.group_code == group_num:
                course_name.insert(0, course.name)
                course_code.insert(0, course.code)
                course_group.insert(0, course.group_code)
                course_capacity.insert(0, course.capacity)
                course_day.insert(0, course.day)
                course_hour.insert(0, course.hour)
                break
    elif find_course(code, group_num) == "no":
        Label(chosen_course_frame, text="درسی با این کد و شماره گروه وجود ندارد", bg=background).pack()
        return
    Label(chosen_course_frame, text="", bg=background, padx=200).grid(row=0, column=0)
    Label(chosen_course_frame, text="", bg=background, pady=10).grid(row=0, column=1)
    Label(chosen_course_frame, text="نام درس", bg=background).grid(row=1, column=1)
    Label(chosen_course_frame, text="کد درس", bg=background).grid(row=2, column=1)
    Label(chosen_course_frame, text="شماره گروه ", bg=background).grid(row=3, column=1)
    Label(chosen_course_frame, text="ظرفیت", bg=background).grid(row=4, column=1)
    Label(chosen_course_frame, text="روز", bg=background).grid(row=5, column=1)
    Label(chosen_course_frame, text="ساعت", bg=background).grid(row=6, column=1)

    edit_course_button = Button(chosen_course_frame, text="ثبت تغییرات", bg=text_color, fg=background,
                            command=lambda :save_course_changes(course_name.get(),
                            course_code.get(),
                            course_group.get(),
                            course_capacity.get(),
                            course_day.get(),
                            course_hour.get()))

    edit_course_button.grid(row=7,column=0)
    course_name.grid(row=1, column=0)
    course_code.grid(row=2, column=0)
    course_group.grid(row=3, column=0)
    course_capacity.grid(row=4, column=0)
    course_day.grid(row=5, column=0)
    course_hour.grid(row=6, column=0)







def open_new_course_page():
    new_course_page = Toplevel()
    new_course_page.configure(bg=background)
    new_course_page.title("درس جدید")
    new_course_page.geometry("300x300")
    new_frame = Frame(new_course_page, bg=background)
    new_frame.pack(anchor=CENTER)
    new_course_error = Frame(new_course_page, bg=background)




    def create_new_course(name, code, group_code, capacity, day, hour):
        new_course_error.pack()
        for widget in new_course_error.winfo_children():
            widget.destroy()
        if name!="" and code!="" and group_code!=""and capacity!=""and day!="" and hour!="":
            for course in courses:
                if course.code == code and course.group_code==group_code:
                    Label(new_course_error, bg = background, text = "درسی با این کد درس و شماره گروه وجود دارد",fg="Red").pack()
                    return
            courses.append(Course(name, code, group_code, capacity, "0", day, hour))
            save_courses()
            Label(new_course_error, bg = background, text = "درس با موفقیت ثبت شد",fg="Green").pack()
        else:
            Label(new_course_error, bg=background, text="لطفا تمامی خانه ها را پر کنید", fg="Red").pack()

    Label(new_frame,text="",bg=background,pady=10).grid(row=0,column=1)
    Label(new_frame,text="نام درس",bg=background).grid(row=1,column=1)
    Label(new_frame,text="کد درس",bg=background).grid(row=2,column=1)
    Label(new_frame,text="شماره گروه ",bg=background).grid(row=3,column=1)
    Label(new_frame,text="ظرفیت",bg=background).grid(row=4,column=1)
    Label(new_frame,text="روز",bg=background).grid(row=5,column=1)
    Label(new_frame,text="ساعت",bg=background).grid(row=6,column=1)
    new_course_name = Entry(new_frame,bg=entry_color)
    new_course_code = Entry(new_frame,bg=entry_color)
    new_course_group = Entry(new_frame,bg=entry_color)
    new_course_capacity = Entry(new_frame,bg=entry_color)
    new_course_day = Entry(new_frame,bg=entry_color)
    new_course_hour = Entry(new_frame,bg=entry_color)
    new_course_name.grid(row=1,column=0)
    new_course_code.grid(row=2,column=0)
    new_course_group.grid(row=3,column=0)
    new_course_capacity.grid(row=4,column=0)
    new_course_day.grid(row=5,column=0)
    new_course_hour.grid(row=6,column=0)
    create_new_course_button = Button(new_frame,text="ثبت درس جدید",bg=text_color,fg=background,command = lambda :
    create_new_course(
        new_course_name.get(),
        new_course_code.get(),
        new_course_group.get(),
        new_course_capacity.get(),
        new_course_day.get(),
        new_course_hour.get()
    ))

    create_new_course_button.grid(row=7,column=0)




def open_course_editor():
    signup_frame.pack_forget()
    admin_signup_frame.pack_forget()
    show_students_frame.pack_forget()
    show_students_list_frame.pack_forget()
    chosen_course_frame.pack_forget()
    course_editor.pack_forget()
    for widget in toper_frame.winfo_children():
        widget.destroy()


    course_editor.pack(anchor=CENTER,fill=BOTH, expand=1)
    toper_frame.pack(anchor=CENTER,fill=BOTH, expand=1)
    open_courses_button = Button(toper_frame,bg=text_color,fg=background,text="مشاهده همه درس ها",command=open_courses_admin)
    search_courses_code_entry = Entry(toper_frame,bg=entry_color,width=10)
    search_courses_group_entry = Entry(toper_frame,bg=entry_color,width=10)
    search_courses_button = Button(toper_frame,bg=text_color,fg=background,text="نمایش درس",command=lambda :open_chosen_course(search_courses_code_entry.get(),search_courses_group_entry.get()))
    new_course_button = Button(toper_frame,bg=text_color,fg=background,text="اضافه کردن درس جدید",command=open_new_course_page)
    Label(toper_frame,text="کد درس",bg=background,width=8,padx=5).grid(row=1,column=5)
    Label(toper_frame,text="شماره گروه",bg=background,width=8,padx=5).grid(row=1,column=3)
    new_course_button.grid(row=1,column=7)
    search_courses_button.grid(row=1,column=1)
    open_courses_button.grid(row=1,column=6)
    search_courses_code_entry.grid(row=1,column=4)
    search_courses_group_entry.grid(row=1,column=2)



load_admin_data()
load_students()
load_courses()

if logged_in == 0:
    root = Tk()
    root.configure(bg=background)
    root.title("صفحه ورود")
    MainPage = Frame(root, bg=background, padx=200, pady=150)
    MainPage.pack()
    login = IntVar()
    login.set(1)
    login_page = Frame(MainPage,bg=background)
    login_page.grid(sticky=NSEW)
    student_option = Radiobutton(login_page, text="دانشجو", variable=login, value=1,bg=background,activeforeground="#26004d").grid(row = 0 , column = 0)
    admin_option = Radiobutton(login_page, text="ادمین",variable=login, value=2,bg=background,activeforeground="#26004d").grid(row = 0 , column = 1)
    username = Entry(login_page , width = 30 ,bg=entry_color)
    username.grid(row = 1, column =0,columnspan=2)
    password = Entry(login_page , width = 30 ,bg=entry_color)
    password.grid(row = 2, column =0,columnspan=2)
    Label(login_page, text = "نام کاربری",bg=background,fg=text_color).grid(row=1,column=2)
    Label(login_page, text = "رمز عبور",bg=background,fg=text_color).grid(row=2,column=2)
    submit = Button(login_page,text="ورود",width=15,bg=entry_color,command=lambda: submiting(username.get(), password.get()))
    submit.grid(row=3, column=1)
    root.mainloop()
if logged_in == 1:
    student_window = Tk()
    student_window.geometry("575x300")
    student_window.configure(bg=background)
    student_window.title(logged_in_student.name + " " + logged_in_student.last_name)
    MainFrame = Frame(student_window, bg=background)
    MainFrame.pack(anchor=N)
    OptionFrame = Frame(MainFrame, bg=background)
    profile_button = Button(OptionFrame, text="پروفایل", width=15, command=lambda: open_profile(), bg=text_color,
                            fg=background)
    course_button = Button(OptionFrame, text="دروس ارائه شده", width=15, command=lambda: open_courses(), bg=text_color,
                           fg=background)
    my_course_button = Button(OptionFrame, text="دروس من", width=15, command=lambda: open_my_courses(), bg=text_color,
                              fg=background)
    selection_button = Button(OptionFrame, text="انتخاب واحد", width=15, command=lambda: open_selection(),
                              bg=text_color, fg=background)
    editor_button = Button(OptionFrame, text="ویرایش اطلاعات", width=15, command=lambda: open_editor(), bg=text_color,
                           fg=background)
    OptionFrame.pack(anchor=N)
    ViewFrame = Frame(MainFrame, bg=background)
    ProfileFrame = Frame(MainFrame, bg=background)
    selectionFrame = Frame(MainFrame, bg=background)
    my_courses_Frame = Frame(MainFrame, bg=background)
    editor_Frame = Frame(MainFrame, bg=background)
    ##for viewing profile

    ##for opening courses

    ##for viewing selections page
    SelectionOptons = Frame(selectionFrame, bg=background)
    SelectionOptons.pack(anchor=CENTER)
    errors = Frame(selectionFrame, bg=background)
    errors.pack()

    ## my courses view

    ##for editing

    profile_button.grid(row=1, column=1, sticky=W)
    course_button.grid(row=1, column=2, sticky=W)
    my_course_button.grid(row=1, column=3, sticky=W)
    selection_button.grid(row=1, column=4, sticky=W)
    editor_button.grid(row=1, column=5, sticky=W)

    student_window.mainloop()

if logged_in == 2:
    admin_window = Tk()
    admin_window.title(logged_in_admin.username)
    admin_window.geometry("590x340")
    admin_window.configure(bg=background)
    admin_frame = Frame(admin_window, bg=background)
    admin_frame.pack(anchor=N, )
    admin_options_frame = Frame(admin_frame, bg=background)
    admin_options_frame.pack(anchor=N)

    signup_frame = Frame(admin_frame, bg=background)
    admin_signup_frame = Frame(admin_frame, bg=background)
    show_students_frame = Frame(admin_frame, bg=background)
    show_students_list_frame = Frame(admin_frame, bg=background)
    result_frame = Frame(show_students_frame, bg=background)
    search_frame = Frame(show_students_frame, bg=background)
    errors = Frame(show_students_frame, bg=background)
    edit_err = Frame(errors, bg=background)
    # for editing courses
    course_editor = Frame(admin_frame, bg=background)
    toper_frame = Frame(course_editor, bg=background)
    chosen_course_frame = Frame(course_editor, bg=background)

    add_course_button = Button(admin_options_frame, text="ویرایش و ثبت درس", width=15, bg=text_color, fg=background,
                               command=open_course_editor)
    signup_button = Button(admin_options_frame, text="ثبت نام دانشجو", width=15, bg=text_color, fg=background,
                           command=show_signup)
    edit_button = Button(admin_options_frame, text="ویرایش داشجو ها", width=15, bg=text_color, fg=background,
                         command=show_students)
    add_admin_button = Button(admin_options_frame, text="ثبت نام ادمین جدید", width=15, bg=text_color, fg=background,
                              command=show_admin_signup)
    show_users_button = Button(admin_options_frame, text="مشاهده دانشجو ها", width=15, bg=text_color, fg=background,
                               command=open_students)

    add_course_button.grid(row=1, column=1)
    signup_button.grid(row=1, column=2)
    edit_button.grid(row=1, column=3)
    add_admin_button.grid(row=1, column=5)
    show_users_button.grid(row=1, column=4)

    admin_window.mainloop()





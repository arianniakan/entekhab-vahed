class Student:
    def __init__(self,
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
                 phone_number=" ",
                 address=" ",
                 card_num=" ",
                 religion=" ",
                 father_number=" ",
                 mothers_number=" ",
                 courses=[]
                 ):
        self.name = name
        self.last_name = last_name
        self.father_name = father_name
        self.student_num = student_num
        self.password = password
        self.id_num = id_num
        self.entrance_year = entrance_year
        self.major = major
        self.university = university
        self.college = college
        self.phone_number = phone_number
        self.address = address
        self.card_num = card_num
        self.religion = religion
        self.father_number = father_number
        self.mother_number = mothers_number
        self.courses = courses




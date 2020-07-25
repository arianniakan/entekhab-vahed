class Course:
    def __init__(self,name , code, group_code, capacity, enrolled, day, hour ):
        self.name = name
        self.code = code
        self.group_code = group_code
        self.capacity = capacity
        self.enrolled = enrolled
        self.day = day
        self.hour = hour

    def available(self):
        if int(self.capacity) > int(self.enrolled):
            return True
        elif int(self.capacity) == int(self.enrolled):
            return False
        else:
            print("error more people in the course than possible")


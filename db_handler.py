from database.config import combined_Database_Class, \
    Academies_Database_Class, Courses_Database_Class,\
    Students_Database_Class, session

class DBHandler:

    @classmethod
    def get_enrolled_list(cls, student_id):
        result_enrolled_list = []
        data = session.query(combined_Database_Class).all()
        for data_row in data:
            if data_row.student_id == student_id:
                result_enrolled_list.append(data_row.course_id)
        return cls.get_course_name(result_enrolled_list)

    @staticmethod
    def get_student():    
        students = session.query(Students_Database_Class).order_by(Students_Database_Class.roll_number.asc()).all()
        student_dict = {}
        for student in students:
            student_dict[student.roll_number] = {
                "first_name":student.first_name,
                "last_name":student.last_name,
                "total_course_cost":student.total_course_cost,
                "total_paid":student.total_paid}
        return student_dict

    @staticmethod
    def get_courses():
        course_dict = {}
        courses = session.query(Courses_Database_Class).all()
        for course in courses:
            course_dict[course.course_id] = {
                "course_name":course.course_name,
                "academy_id":course.academy_id,
                "course_price":course.course_price
                }
        return course_dict

    @staticmethod
    def get_academies():
        academy_dict = {}
        academies = session.query(Academies_Database_Class).all()
        for academy in academies:
            academy_dict[academy.academy_id] = academy.academy_name
        return academy_dict

    @staticmethod
    def get_course_name(enrolled_list):
        course_list = []
        courses = session.query(Courses_Database_Class).\
            filter(Courses_Database_Class.course_id.in_(enrolled_list))
        for course in courses:
            course_list.append(course.course_name)
        return course_list

    @staticmethod
    def add_student(student_tuple):
        new_student = Students_Database_Class(
            first_name=student_tuple[0],
            last_name = student_tuple[1],
            total_paid = student_tuple[2]
            )
        session.add(new_student)
        session.commit()


    @staticmethod
    def update_student(roll_number, student_tuple):

        session.query(Students_Database_Class).\
        filter(Students_Database_Class.roll_number == roll_number).\
        update({
        "first_name" :student_tuple[0],
        "last_name" :student_tuple[1],
        "total_course_cost" : student_tuple[2],
        "total_paid" : student_tuple[3]
    })
        session.commit()

    @staticmethod
    def remove_student(student_id):

        session.query(Students_Database_Class).\
            filter(Students_Database_Class.roll_number == student_id).\
                delete()
        session.commit()

    @staticmethod
    def get_student_courses(student_id, course_id):

        result = session.query(combined_Database_Class).\
            filter_by(
                student_id= student_id,
                course_id = course_id).first() is not None
        return result

    @staticmethod
    def get_student_all_courses(student_id):

        course_list= []
        results = session.query(combined_Database_Class).\
            filter_by(student_id = student_id).all()
        for result in results:
            course_list.append(result.course_id)
            # print(result.course_id)
        return course_list

    @staticmethod
    def join_course(student_id, course_id):

        combined_student = combined_Database_Class(
            student_id = student_id,
            course_id = course_id
            )
        session.add(combined_student)
        session.commit()

    @staticmethod
    def opt_course(student_id, course_id):

        session.query(combined_Database_Class).filter(
            combined_Database_Class.student_id == student_id,
            combined_Database_Class.course_id == course_id
            ).delete()
        session.commit()

    @staticmethod
    def add_academy(academy_name):

        new_student = Academies_Database_Class(
            academy_name = academy_name
            )
        session.add(new_student)
        session.commit()
    
    @staticmethod
    def remove_academy(academy_name):

        session.query(Academies_Database_Class).\
            filter(Academies_Database_Class.academy_name == academy_name).\
                delete()
        session.commit()
    
    


if __name__ == "__main__":
    #  initilize_db(load_db_config())

    # db_config = start_db_handeling()
    handler = DBHandler()
    students = handler.get_student()
    academies = handler.get_academies()
    cources = handler.get_courses()

from Settings import config_paths as cp
import json

paths = cp.paths()


def courses():
    yellow_courses = []
    yellow_curriculo_number = []
    courses_list = []
    with open(paths.yellow_path, "r") as json_file:
        summary_json = json.load(json_file)
    for list_courses in summary_json:
        for course_name in list_courses:
            if course_name == 'yellow_designation':
                yellow_courses.append(list_courses['yellow_designation'])
                courses_list.append(list_courses['yellow_designation'] + ' / ' + list_courses['curriculo_number'])
            if course_name == 'curriculo_number':
                yellow_curriculo_number.append(list_courses['curriculo_number'])

    json_file.close()

    return yellow_courses, yellow_curriculo_number, courses_list


def students(course, course_number, subject_ask):

    list_students_selec = []

    with open(paths.students_path, "r") as json_file:
        summary_json = json.load(json_file)
    for list_students in summary_json:
        student_prov = {}
        if course == list_students['course_yellow'] and course_number == list_students['number_curriculo']:
            cn=list_students['complete_name']
            sn=list_students['student_number']
            for list_subjects in list_students['plan_matricula']:
                if str(course[0])+'º - '+list_subjects['subject'] == subject_ask:
                    c=list_subjects['call']
                    a=list_subjects['acumulate']

            student_prov = dict(nombre=cn, numero=sn, acumulado=a, convocatoria=c)
        list_students_selec.append(student_prov)

    def mysort(e):
        return e['numero']

    list_students_selec.sort(key=mysort)

    return list_students_selec

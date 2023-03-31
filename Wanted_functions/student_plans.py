from Settings import config_paths as cp
import json

paths = cp.paths()

def sujects(number_curr):
    subject_list = []

    with open(paths.curriculos_path, "r") as json_file:
        summary_json = json.load(json_file)
    for list_curriculos in summary_json:
        if list_curriculos['number_designation'] == number_curr:
            for courses_curr in list_curriculos['courses']:
                c = courses_curr['course']
                for plan_course in courses_curr['plan']:
                    subject_list.append(str(c) + 'º - ' + plan_course['subject'])
    json_file.close()

    return subject_list
#
#def students(course, course_number):
    #list_students_selec = []
#
    #    with open(paths.students_path, "r") as json_file:
#    summary_json = json.load(json_file)
    #for list_students in summary_json:
        #for student in list_students:
            #student_prov = {}
            #if student == 'course_yellow':
                #if course == list_students['course_yellow'] and course_number == list_students['number_curriculo']:
                   #student_prov = dict(nombre=list_students['complete_name'],
                   #                              numero=list_students['student_number'])
                #           list_students_selec.append(student_prov)
    #   def mysort(e):
#    return e['numero']
    #    list_students_selec.sort(key=mysort)
    #
    #    return list_students_selec
#
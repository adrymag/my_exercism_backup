def extend_list(initial_list, extension_list):
    return initial_list.extend(extension_list)

class School:
    def __init__(self):
        self._students_by_grade = {}   # grade -> set of student names ( possible due to names uniqueness (property) )
        self._all_students = set()     # all names for duplicate checking
        self._add_results = []         # True/False for each add_student call

    def add_student(self, name, grade):
        if name in self._all_students: # checking if the name already exists
            self._add_results.append(False) # cannot append the same name (the same student) to the roster (which has to contain each student just once)
            return False
        self._all_students.add(name)
        self._students_by_grade.setdefault(grade, set()).add(name) # removes the need for existence check + conditional appending / initialization
        self._add_results.append(True)
        return True

    def roster(self):
        return [student for grade in sorted(self._students_by_grade) # sort by grade
            for student in sorted(self._students_by_grade[grade])] # sort students with the same grade

    def grade(self, grade_number):
        return sorted(self._students_by_grade.get(grade_number, [])) # dict.get(key, default) is the read-side mirror of setdefault(key, default)'s write-side pattern.

    # @property # TypeError: 'list' object is not callable - this is not possible unless I make sure to always access this as a property/attribute, not as a method (call), i.e. not followed by "([optional_arguments])"
    def added(self):
        return self._add_results
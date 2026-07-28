class School:
    def __init__(self):
        self._students_by_grade = {}   # grade -> set of student names ( possible due to names uniqueness (property) )
        self._all_students = set()     # all names for duplicate checking
        self._add_results = []         # True/False for each add_student call

    def add_student(self, name, grade):
        if name in self._all_students:
            self._add_results.append(False)
            return False
        self._all_students.add(name)
        self._students_by_grade.setdefault(grade, set()).add(name) # ****
        self._add_results.append(True)
        return True

    def roster(self):
        result = []
        for grade in sorted(self._students_by_grade.keys()):
            result.extend(sorted(self._students_by_grade[grade]))
        return result

    def grade(self, grade_number):
        return sorted(self._students_by_grade.get(grade_number, []))

    # @property # TypeError: 'list' object is not callable
    def added(self):
        return self._add_results
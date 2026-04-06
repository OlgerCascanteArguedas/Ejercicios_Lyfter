class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science

    def calculate_average(self):
        return (self.spanish + self.english + self.social + self.science) / 4

    def get_failed_subjects(self):
        failed = []

        if self.spanish < 60:
            failed.append(("Spanish", self.spanish))
        if self.english < 60:
            failed.append(("English", self.english))
        if self.social < 60:
            failed.append(("Social Studies", self.social))
        if self.science < 60:
            failed.append(("Science", self.science))

        return failed

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science
        }

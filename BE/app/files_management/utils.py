import csv
import random

import faker as faker

from app.data_layer.constants import TestType
from app.common.model_schema_container.model_schema_container import ModelSchemaContainer


class FilesGenerator:
    fake = faker.Faker()

    @classmethod
    def generate_users_csv_file(cls, location):
        users = []
        for _ in range(100):
            name = cls.fake.name()
            email = cls.fake.email()
            user = {'name': name, 'email': email}
            users.append(user)

        with open(location + '\\users.csv', mode='w', newline='') as file:
            fieldnames = ['name', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for user in users:
                writer.writerow(user)

    @classmethod
    def generate_courses_csv_file(cls, location):
        courses = []
        for _ in range(25):
            title = cls.fake.text(max_nb_chars=20)[:-1]
            description = cls.fake.paragraph(nb_sentences=5)
            course = {'title': title, 'description': description}
            courses.append(course)

        with open(location + '\\courses.csv', mode='w', newline='') as file:
            fieldnames = ['title', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for course in courses:
                writer.writerow(course)

    @classmethod
    def generate_lections_csv_file(cls, location):
        lections = []
        for _ in range(75):
            title = cls.fake.text(max_nb_chars=20)[:-1]
            description = cls.fake.paragraph(nb_sentences=5)
            text = cls.fake.paragraph(nb_sentences=20)
            video_url = cls.fake.url()
            lection = {'title': title, 'description': description, 'text': text, 'video_url': video_url}
            lections.append(lection)

        with open(location + '\\lections.csv', mode='w', newline='') as file:
            fieldnames = ['title', 'description', 'text', 'video_url']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for lection in lections:
                writer.writerow(lection)

    @classmethod
    def generate_tests_csv_file(cls, location):
        tests = []
        for i in range(100):
            title = cls.fake.text(max_nb_chars=20)[:-1]
            description = cls.fake.paragraph(nb_sentences=5)
            type = TestType.EXAM.value if (i + 1) % 4 == 0 else TestType.PRACTISE.value
            test = {'title': title, 'description': description, 'type': type}
            tests.append(test)

        with open(location + '\\tests.csv', mode='w', newline='') as file:
            fieldnames = ['title', 'description', 'type']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for test in tests:
                writer.writerow(test)

    @classmethod
    def generate_questions_csv_file(cls, location):
        questions = []
        for _ in range(500):
            text = cls.fake.sentence()[:-1] + '?'
            question = {'text': text}
            questions.append(question)

        with open(location + '\\questions.csv', mode='w', newline='') as file:
            fieldnames = ['text']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for question in questions:
                writer.writerow(question)

    @classmethod
    def generate_answers_csv_file(cls, location):
        answers = []
        is_right_index = random.randint(0, 3)
        for i in range(2000):
            text = cls.fake.sentence()[:-1]
            if i % 4 == is_right_index:
                is_right = True
            else:
                is_right = False

            if (i + 1) % 4 == 0:
                is_right_index = random.randint(0, 3)

            answer = {'text': text, 'is_right': is_right}
            answers.append(answer)

        with open(location + '\\answers.csv', mode='w', newline='') as file:
            fieldnames = ['text', 'is_right']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # write header row
            for answer in answers:
                writer.writerow(answer)

    @classmethod
    def generate_csv_files(cls, location):
        cls.generate_users_csv_file(location)
        cls.generate_courses_csv_file(location)
        cls.generate_lections_csv_file(location)
        cls.generate_tests_csv_file(location)
        cls.generate_questions_csv_file(location)
        cls.generate_answers_csv_file(location)


class FilesLoader:
    @classmethod
    def read_users_csv(cls, location):
        with open(location + '\\users.csv', mode='r') as file:
            reader = csv.DictReader(file)
            users = [row for row in reader]
            return users

    @classmethod
    def read_courses_csv(cls, location):
        with open(location + '\\courses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            courses = [row for row in reader]
            return courses

    @classmethod
    def read_lections_csv(cls, location):
        with open(location + '\\lections.csv', mode='r') as file:
            reader = csv.DictReader(file)
            lections = [row for row in reader]
            return lections

    @classmethod
    def read_tests_csv(cls, location):
        with open(location + '\\tests.csv', mode='r') as file:
            reader = csv.DictReader(file)
            tests = [row for row in reader]
            return tests

    @classmethod
    def read_questions_csv(cls, location):
        with open(location + '\\questions.csv', mode='r') as file:
            reader = csv.DictReader(file)
            questions = [row for row in reader]
            return questions

    @classmethod
    def read_answers_csv(cls, location):
        with open(location + '\\answers.csv', mode='r') as file:
            reader = csv.DictReader(file)
            answers = [row for row in reader]
            for answer in answers:
                answer['is_right'] = True if answer['is_right'] == 'True' else False
            return answers

    @classmethod
    def write_csv_data_into_db(cls, location):
        print('Creating users...')
        users = cls.read_users_csv(location)
        user_ids = ModelSchemaContainer.get_model_manager('user').create_many(users)

        print('Creating courses...')
        courses = cls.read_courses_csv(location)
        courses_ids = ModelSchemaContainer.get_model_manager('course').create_many(courses)

        print('Creating lections...')
        lections = cls.read_lections_csv(location)
        for i in range(len(lections)):
            lections[i]['course_id'] = courses_ids[i // 3]
        lections_ids = ModelSchemaContainer.get_model_manager('lection').create_many(lections)

        print('Creating tests...')
        tests = cls.read_tests_csv(location)
        for i in range(len(tests)):
            tests[i]['course_id'] = courses_ids[i // 4]
        tests_ids = ModelSchemaContainer.get_model_manager('test').create_many(tests)

        print('Creating questions...')
        questions = cls.read_questions_csv(location)
        for i in range(len(questions)):
            questions[i]['test_id'] = tests_ids[i // 5]
        questions_ids = ModelSchemaContainer.get_model_manager('question').create_many(questions)

        print('Creating answers...')
        answers = cls.read_answers_csv(location)
        for i in range(len(answers)):
            answers[i]['question_id'] = questions_ids[i // 4]
        answers_ids = ModelSchemaContainer.get_model_manager('answer').create_many(answers)

        print('Assigning users to courses...')
        users_courses = []
        for user_id in user_ids:
            number_of_courses = random.randint(0, 10)
            chosen_courses_ids = random.sample(courses_ids, number_of_courses)
            for chosen_courses_id in chosen_courses_ids:
                users_courses.append({'user_id': user_id, 'course_id': chosen_courses_id})
        user_courses_ids = ModelSchemaContainer.get_model_manager('user_course').create_many(users_courses)

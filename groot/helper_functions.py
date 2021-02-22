import yaml
import random


class HelperFunctions(object):

    def read_yaml_file(self, filename):
        with open(filename, 'r') as stream:
            try:
                schema = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return schema

    def random_integer_generator(self, num_ints):
        nums = []
        for i in range(0, num_ints):
            nums.append(i)
        return nums

    def random_name_generator(self, num_names):

        first_names = ('John', 'Andy', 'Joe')
        last_names = ('Johnson', 'Smith', 'Williams')

        random_names = []
        for name in range(num_names):
            name = "".join(random.choice(first_names) + " " + random.choice(last_names))
            random_names.append(name)

        return random_names

    def generate_test_data(self, num_items):
        some_random_names = self.random_name_generator(num_items)
        some_random_numbers = self.random_integer_generator(num_items)
        test_data = dict(zip(some_random_numbers, some_random_names))

        return test_data

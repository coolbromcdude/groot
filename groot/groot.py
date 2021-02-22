
from groot.helper_functions import HelperFunctions
import subprocess


class Groot(HelperFunctions):
    @staticmethod
    def run():

        arguments = ['pwd']
        path = subprocess.check_output(arguments)
        #schema = HelperFunctions().read_yaml_file(f"{path}/groot/schemas/character.yml")


        #print(schema)
        print(HelperFunctions().generate_test_data(2))


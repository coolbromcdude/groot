
from groot.helper_functions import HelperFunctions
import os
import click

class Groot(HelperFunctions):
    @staticmethod
    @click.command()
    @click.option("--schema", required=True, type=str, help="the schema to use")
    def run(schema):

        path = os.getcwd()
        file = f"""{path}/groot/schemas/{schema}.yml"""
        schema_file = HelperFunctions().read_yaml_file(file)

        print(schema_file)
        print(HelperFunctions().generate_test_data(2))


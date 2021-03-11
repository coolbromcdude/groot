
from groot.helper_functions import HelperFunctions
import os
import click
import csv

class Groot(HelperFunctions):
    @staticmethod
    @click.command()
    @click.option("--schema", required=True, type=str, help="The schema to use for generating data")
    @click.option("--records", required=True, type=int, help="Number of records to generate")
    @click.option("--output-format", required=True, type=str, help="The output format for the generated data")
    def run(schema, records, output_format):

        path = os.getcwd()
        file = f"""{path}/groot/schemas/{schema}.yml"""
        schema_file = HelperFunctions().read_schema_file(file)
        header = []
        for k, v in schema_file.items():
            for k1, v1 in v.items():
                header.append(k1)

        data = HelperFunctions().generate_test_data(records)

        if output_format == "csv":
            with open('output_data.csv', 'w', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(header)

                for k, v in data.items():
                    writer.writerow([k, v])

        else:
            print(f"{output_format} was chosen, not sure what to do yet")

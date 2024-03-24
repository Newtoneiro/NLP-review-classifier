# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import json
import csv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # Open the JSON file
    # Function to extract text and rating
    def extract_text_rating(data):
        data_json = json.loads(data)
        text = data_json['text']
        rating = data_json['rating']
        return text, rating
    
    def adjust_rating(rating):
        return int(rating) - 1

    # Read data from file
    with open(input_filepath, 'r', encoding='utf-8') as file:
        data = file.readlines()

    # Write text-rating pairs to CSV
    with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            text, rating = extract_text_rating(item)
            writer.writerow({'text': text, 'rating': adjust_rating(rating)})


def stream_data(input_file, output_file, num_lines):
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            # Initialize a counter to keep track of the number of lines streamed
            line_count = 0
            # Read each line from the input file
            for line in infile:
                # Write the line to the output file
                outfile.write(line)
                # Increment the line count
                line_count += 1
                # Check if we have reached the desired number of lines
                if line_count >= num_lines:
                    break


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

# =============================================================================
# This file was used to convert the 50 million reviews dataset from JSON to 
# arround 1M data in CSV format. The data was then used to train the model.
# The original dataset is available at:
# https://aclanthology.org/2020.lrec-1.605/
# =============================================================================
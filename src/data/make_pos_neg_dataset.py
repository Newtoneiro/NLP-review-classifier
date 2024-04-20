# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import csv

NO_SAMPLES_PER_CLASS = 65_000


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
        text = data['text']
        rating = data['rating']
        return text, rating

    def adjust_rating(rating):
        if int(rating) < 4:
            return 0
        else:
            return 1

    # Read data from file
    with open(input_filepath, 'r', encoding='utf-8') as file:
        data = file.readlines()

    # Write text-rating pairs to CSV
    with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        pos_count, neg_count = 0, 0

        for i, item in enumerate(csv.DictReader(data)):
            logger.info(f'Processing line {i}')
            text, rating = extract_text_rating(item)
            rating = adjust_rating(rating)
            if rating == 0 and neg_count < NO_SAMPLES_PER_CLASS:
                writer.writerow({'text': text, 'rating': rating})
                neg_count += 1
            elif rating == 1 and pos_count < NO_SAMPLES_PER_CLASS:
                writer.writerow({'text': text, 'rating': rating})
                pos_count += 1

            if pos_count == NO_SAMPLES_PER_CLASS \
                    and neg_count == NO_SAMPLES_PER_CLASS:
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
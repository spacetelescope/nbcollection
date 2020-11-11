import argparse

def validate_and_parse_inputs(options: argparse.Namespace) -> argparse.Namespace:
    options.collection_names = options.collection_names.split(',')
    options.category_names = options.category_names.split(',')
    options.notebook_names = options.notebook_names.split(',')

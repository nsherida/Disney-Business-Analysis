"""
Creates sample data and unit tests for group_agg_script function
"""
# Import our function and pandas
from group_agg_script import group_agg
import pandas as pd

# Define test function
def test_group_agg():

    # Create data to build test dataframe
    input_data = {
        "title": ["HP1", "HP2", "HP3", "LR1", "LR2", "LR3", "SW1", "SW2", "SW3"],
        "genre": [
            "Fantasy",
            "Fantasy",
            "Fantasy",
            "Fantasy",
            "Fantasy",
            "Fantasy",
            "Sci-fi",
            "Sci-fi",
            "Sci-fi",
        ],
        "author": ["JKR", "JKR", "JKR", "JRRT", "JRRT", "JRRT", "GL", "GL", "GL"],
        "pages": [300, 350, 390, 500, 650, 550, 200, 700, 900],
        "rating": [9.0, 8.0, 7.5, 9.9, 9.8, 9.7, 5.0, 7.5, 9.8],
    }
    # Build test dataframe
    test_data = pd.DataFrame.from_dict(input_data)

    # Apply function to test dataframe
    testing = group_agg(test_data, "author", "pages", "rating", ["sum"], ["min"])

    # Test outputs against expected results
    assert testing.shape == (3, 2)
    assert list(testing[("pages", "sum")]) == [1800, 1040, 1700]
    assert list(testing[("rating", "min")]) == [5.0, 7.5, 9.7]

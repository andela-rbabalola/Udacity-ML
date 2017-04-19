#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    for pred, age, net_worth in zip(predictions, ages, net_worths):
      cleaned_data.append((age, net_worth, pred - net_worth ))

    # Sort by the third element in the tuple, the error
    # reverse = True because we want it sorted in descending order
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=True)
    # slice off 10% of points with worst predictions
    cleaned_data = cleaned_data[9: len(cleaned_data) + 1]

    return cleaned_data


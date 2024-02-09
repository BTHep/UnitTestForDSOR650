from collections import defaultdict

def transform_data(data, transform_func):
    """
    Applies a transformation function to each item in a list of data.

    Parameters:
    - data: A list of data items, typically rows fetched from an SQLite database.
    - transform_func: A function that takes a data item as input and returns a transformed version of the item.

    Returns:
    - A list of transformed data items.
    """
    return [transform_func(item) for item in data]

def aggregate_data(data, key_func, aggregate_func):
    """
    Aggregates data by a specified key and applies an aggregation function to the grouped data.

    Parameters:
    - data: A list of data items, typically rows fetched from an SQLite database.
    - key_func: A function to determine the key used to group data items.
    - aggregate_func: A function applied to the list of items for each key to produce a result.

    Returns:
    - A dictionary with keys determined by key_func and values determined by applying aggregate_func to grouped items.
    """
    grouped_data = defaultdict(list)
    for item in data:
        key = key_func(item)
        grouped_data[key].append(item)
    return {key: aggregate_func(group) for key, group in grouped_data.items()}

def filter_data(data, filter_func):
    """
    Filters a list of data based on a specified condition.

    Parameters:
    - data: A list of data items, typically rows fetched from an SQLite database.
    - filter_func: A function that evaluates each item against a condition, returning True if the item should be included.

    Returns:
    - A list of data items that meet the condition specified by filter_func.
    """
    return [item for item in data if filter_func(item)]

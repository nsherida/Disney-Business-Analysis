def group_agg(data, grouping_col, agg_col1, agg_col2, agg_act1, agg_act2):
    """
    Given a dataframe, one grouping column, two aggregating columns, and two lists, return a dataframe that has been
    grouped by the column and the list of aggregate functions applied to the aggregating columns.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to group and aggregate on
    grouping_col : str
        The column to group the data on
    agg_col1 : str
        After grouping, the first column to apply aggregate functions to
    agg_col2 : str
        After grouping, the second column to apply aggregate functions to
    agg_act1 : list
        The list of actions to apply to the first column being aggregated
    agg_act2 : list
        The list of actions to apply to the second column being aggregated

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe with the group by column and the aggregate actions applied

    Raises
    ------
    TypeError
        If the input argument data is not of type dataframe
    AssertError
        If the input argument grouping_col is not a column in the dataframe
    AssertError
        If the input argument agg_col1 is not a column in the dataframe
    Assertrror
        If the input argument agg_col2 is not a column in the dataframe

    Examples
    --------
    >>> group_agg(test_data, 'author', 'pages', 'rating', ['sum'], ['min'])
    author pages rating
           sum   min
    GL     1800  5.0
    JKR    1040  7.5
    JRRT   1700  9.7

    """
    # Import pandas
    import pandas as pd

    # Check if data input is of type DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # Check if the grouping and aggregating columns exist in the input DataFrame
    assert (
        grouping_col in data.columns
    ), "The grouping column does not exist in the dataframe"

    assert (
        agg_col1 in data.columns
    ), "The first aggregating column does not exist in the dataframe"

    assert (
        agg_col2 in data.columns
    ), "The second aggregating column does not exist in the dataframe"

    # Group data by grouping_col
    data_grouped = data.groupby(by=grouping_col)
    # Aggregate data on agg columns 1 & 2 using aggregate actions 1 & 2
    data_agg = data_grouped.agg({agg_col1: agg_act1, agg_col2: agg_act2})

    # Return final dataframe
    return data_agg

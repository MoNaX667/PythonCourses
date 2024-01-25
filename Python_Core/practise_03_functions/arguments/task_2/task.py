from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """

    result = selector(data)
    for filter_func in filters:
        result = filter_func(result)
    return result

    pass


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    def select_columns(data: DataType) -> DataType:
        return [{column: entry[column] for column in columns} for entry in data]

    return select_columns

    pass


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filter_by_field(data: DataType) -> DataType:
        return [entry for entry in data if entry.get(column) in values]

    return filter_by_field

    pass


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()


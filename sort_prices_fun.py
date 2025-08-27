def sort_prices(list_of_tuples: list[tuple[str,str]]):
    """Sorts list of tuples of (item name, price) by price (descending order)."""
    sorted_by_prices = sorted(list_of_tuples, key=lambda item: float(item[1]), reverse=True)
    return sorted_by_prices

def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))

if __name__ == '__main__':
    main()
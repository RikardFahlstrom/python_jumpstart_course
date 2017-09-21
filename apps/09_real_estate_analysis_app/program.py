import csv
import os

try:
    import statistics  # statistics module is not available in Py2
except:
    #  error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_data(filename)
    query_data(data)

def print_header():
    print('--------------------------------------')
    print('    REAL ESTATE DATA MINING APP')
    print('--------------------------------------')

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)  # use purchases[0].__dict__ to use internal dictionary and look at the data
        return purchases

def query_data(data): # list[Purchase]):  # Specify what kind of data that will be passed in the function, will adapt functionality in the function

    #  easy if data was sorted by price:
    data.sort(key=lambda p: p.price)  # Key= value that we will use to sort on. Lambda = small inline function

    #  most expensive house?
    high_purchase = data[-1]  # data is now a list sorted on price low->high, last item is most expensive
    print("The most expensive house is ${:,} with {} beds and {} baths.".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    #  least expensive house?
    low_purchase = data[0]  # data is now a list sorted on price low->high, first item is least expensive
    print("The most expensive house is ${:,} with {} beds and {} baths.".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    #  average price house?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
    ]

    avg_price = statistics.mean(prices)
    print("The average home price is {:,}.".format(int(avg_price)))

    #  average price of 2 bedroom house?
    # prices = []
    # bats = []
    # for pur in data:
    #      if pur.beds == 2:
    #          prices.append(pur.price)
    #          prices.append(pur.baths)

    two_bed_homes = [
        p  # projection or items
        for p in data  # the set to process
        if p.beds == 2  # test / condition
    ]

    avg_price = statistics.mean(p.price for p in two_bed_homes)
    avg_baths = statistics.mean(p.baths for p in two_bed_homes)
    avg_sqft = statistics.mean(p.sq__ft for p in two_bed_homes)
    print("Avergae 2-bedroom home is {:,}, baths={}, sq ft={:,}."
          .format(int(avg_price), round(avg_baths,1), round(avg_sqft,1)))


if __name__ == '__main__':
    main()


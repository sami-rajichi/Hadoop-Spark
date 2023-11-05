from mrjob.job import MRJob

class Purchases(MRJob):
    """
    A MapReduce job to process purchases data.

    This class defines the mapper and reducer methods to process
    purchase data and calculate the total purchase amount for each key.
    """

    def mapper(self, key, value):
        """
        Mapper function to extract and emit purchase data.

        Args:
            key (str): Input key.
            value (str): Input value containing purchase data separated by '\t'.

        Yields:
            (str, float): A tuple containing the purchase category (key) and the
            purchase amount (value) as a float.
        """
        purchases = value.split('\t')
        yield purchases[2], float(purchases[-2])

    def reducer(self, key, values):
        """
        Reducer function to calculate the total purchase amount for each category.

        Args:
            key (str): Purchase category.
            values (iterable): Iterator of purchase amounts for the given category.

        Yields:
            (str, float): A tuple containing the purchase category (key) and the
            total purchase amount (value) as a float.
        """
        yield key, sum(values)

if __name__ == '__main__':
    Purchases.run()
# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestAveragePerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_type_results(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_length_results(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 5)

    def test_first_result(self):
        results = self.query_db(self.result.query)
        expected = (1, 673.9)
        self.assertEqual(results[0], expected)

    def test_results(self):
        results = self.query_db(self.result.query)
        expected = [(1, 673.9), (2, 1031.24), (3, 266.32), (4, 2175.03), (5, 1096.3)]
        self.assertEqual(results[0], expected[0])
        self.assertEqual(results[-1], expected[-1])

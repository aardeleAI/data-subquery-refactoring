# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestBestCustomers(ChallengeResultTestCase):
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
        self.assertEqual(len(results), 3)


    def test_results(self):
        results = self.query_db(self.result.query)
        expected = [(4, 2175.03), (5, 1096.3), (2, 1031.24)]
        self.assertEqual(results, expected)

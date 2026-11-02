# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestGeneralAverage(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchone()
        return results

    def test_type_result(self):
        result = self.query_db(self.result.query)
        self.assertIsInstance(result[0], float)

    def test_value_result(self):
        result = self.query_db(self.result.query)
        self.assertGreaterEqual(result[0], 983)
        self.assertLessEqual(result[0], 984)

# coding=utf-8
# Copyright 2018-2023 EvaDB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from test.markers import ludwig_skip_marker, sklearn_skip_marker, xgboost_skip_marker
=======
from test.markers import ludwig_skip_marker, sklearn_skip_marker
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
from test.markers import ludwig_skip_marker, sklearn_skip_marker, xgboost_skip_marker
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
from test.markers import ludwig_skip_marker, sklearn_skip_marker, xgboost_skip_marker
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from test.util import get_evadb_for_testing, shutdown_ray

import pytest

from evadb.configuration.constants import EvaDB_ROOT_DIR
from evadb.server.command_handler import execute_query_fetch_all


@pytest.mark.notparallel
class ModelTrainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evadb = get_evadb_for_testing()
        # reset the catalog manager before running each test
        cls.evadb.catalog().reset()

        create_table_query = """
           CREATE TABLE IF NOT EXISTS HomeRentals (
               number_of_rooms INTEGER,
               number_of_bathrooms INTEGER,
               sqft INTEGER,
               location TEXT(128),
               days_on_market INTEGER,
               initial_price INTEGER,
               neighborhood TEXT(128),
               rental_price FLOAT(64,64)
           );"""
        execute_query_fetch_all(cls.evadb, create_table_query)

        path = f"{EvaDB_ROOT_DIR}/data/ludwig/home_rentals.csv"
        load_query = f"LOAD CSV '{path}' INTO HomeRentals;"
        execute_query_fetch_all(cls.evadb, load_query)

        # Load data for classification tasks.
        create_table_query = """
           CREATE TABLE IF NOT EXISTS Employee (
               education TEXT(128),
               joining_year INTEGER,
               city TEXT(128),
               payment_tier INTEGER,
               age INTEGER,
               gender TEXT(128),
               ever_benched TEXT(128),
               experience_in_current_domain INTEGER,
               leave_or_not INTEGER
           );"""
        execute_query_fetch_all(cls.evadb, create_table_query)

        path = f"{EvaDB_ROOT_DIR}/data/classification/Employee.csv"
        load_query = f"LOAD CSV '{path}' INTO Employee;"
        execute_query_fetch_all(cls.evadb, load_query)

    @classmethod
    def tearDownClass(cls):
        shutdown_ray()

        # clean up
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS HomeRentals;")
<<<<<<< HEAD
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS Employee;")
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        execute_query_fetch_all(
            cls.evadb, "DROP FUNCTION IF EXISTS PredictHouseRentLudwig;"
        )
        execute_query_fetch_all(
            cls.evadb, "DROP FUNCTION IF EXISTS PredictHouseRentSklearn;"
        )
<<<<<<< HEAD
        execute_query_fetch_all(
            cls.evadb, "DROP FUNCTION IF EXISTS PredictRentXgboost;"
        )
        execute_query_fetch_all(
            cls.evadb, "DROP FUNCTION IF EXISTS PredictEmployeeXgboost;"
        )
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

    @pytest.mark.skip(
        reason="Model training intergration test takes too long to complete."
    )
    @ludwig_skip_marker
    def test_ludwig_automl(self):
        create_predict_function = """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
=======
            CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
            CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
=======
            CREATE FUNCTION IF NOT EXISTS PredictHouseRent FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
=======
=======
=======
            CREATE OR REPLACE FUNCTION PredictHouseRentLudwig FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
            ( SELECT * FROM HomeRentals )
            TYPE Ludwig
            PREDICT 'rental_price'
            TIME_LIMIT 120;
        """
        execute_query_fetch_all(self.evadb, create_predict_function)

        predict_query = """
            SELECT PredictHouseRentLudwig(*) FROM HomeRentals LIMIT 10;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)

<<<<<<< HEAD
    @pytest.mark.skip(
        reason="Model training intergration test takes too long to complete."
    )
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
    @sklearn_skip_marker
    def test_sklearn_regression(self):
        create_predict_function = """
            CREATE OR REPLACE FUNCTION PredictHouseRentSklearn FROM
            ( SELECT number_of_rooms, number_of_bathrooms, days_on_market, rental_price FROM HomeRentals )
            TYPE Sklearn
<<<<<<< HEAD
            PREDICT 'rental_price'
            MODEL 'extra_tree'
            METRIC 'r2';
=======
            PREDICT 'rental_price';
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
        """
        execute_query_fetch_all(self.evadb, create_predict_function)

        predict_query = """
            SELECT PredictHouseRentSklearn(number_of_rooms, number_of_bathrooms, days_on_market, rental_price) FROM HomeRentals LIMIT 10;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)

    @xgboost_skip_marker
    def test_xgboost_regression(self):
        create_predict_function = """
<<<<<<< HEAD
            CREATE OR REPLACE FUNCTION PredictRentXgboost FROM
=======
            CREATE FUNCTION IF NOT EXISTS PredictRent FROM
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
            ( SELECT number_of_rooms, number_of_bathrooms, days_on_market, rental_price FROM HomeRentals )
            TYPE XGBoost
            PREDICT 'rental_price'
            TIME_LIMIT 180
<<<<<<< HEAD
            METRIC 'r2'
            TASK 'regression';
        """
        result = execute_query_fetch_all(self.evadb, create_predict_function)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 3)

        predict_query = """
            SELECT PredictRentXgboost(number_of_rooms, number_of_bathrooms, days_on_market, rental_price) FROM HomeRentals LIMIT 10;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)

    @xgboost_skip_marker
    def test_xgboost_classification(self):
        create_predict_function = """
            CREATE OR REPLACE FUNCTION PredictEmployeeXgboost FROM
            ( SELECT payment_tier, age, gender, experience_in_current_domain, leave_or_not FROM Employee )
            TYPE XGBoost
            PREDICT 'leave_or_not'
            TIME_LIMIT 180
            METRIC 'accuracy'
            TASK 'classification';
        """
        result = execute_query_fetch_all(self.evadb, create_predict_function)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 3)

        predict_query = """
            SELECT PredictEmployeeXgboost(payment_tier, age, gender, experience_in_current_domain, leave_or_not) FROM Employee LIMIT 10;
=======
            METRIC 'r2';
        """
        execute_query_fetch_all(self.evadb, create_predict_function)

        predict_query = """
            SELECT PredictRent(number_of_rooms, number_of_bathrooms, days_on_market, rental_price) FROM HomeRentals LIMIT 10;
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)

    @xgboost_skip_marker
    def test_xgboost_regression(self):
        create_predict_function = """
            CREATE FUNCTION IF NOT EXISTS PredictRent FROM
            ( SELECT number_of_rooms, number_of_bathrooms, days_on_market, rental_price FROM HomeRentals )
            TYPE XGBoost
            PREDICT 'rental_price'
            TIME_LIMIT 180
            METRIC 'r2';
        """
        execute_query_fetch_all(self.evadb, create_predict_function)

        predict_query = """
            SELECT PredictRent(number_of_rooms, number_of_bathrooms, days_on_market, rental_price) FROM HomeRentals LIMIT 10;
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)

    @xgboost_skip_marker
    def test_xgboost_regression(self):
        create_predict_function = """
            CREATE FUNCTION IF NOT EXISTS PredictRent FROM
            ( SELECT number_of_rooms, number_of_bathrooms, days_on_market, rental_price FROM HomeRentals )
            TYPE XGBoost
            PREDICT 'rental_price'
            TIME_LIMIT 180
            METRIC 'r2';
        """
        execute_query_fetch_all(self.evadb, create_predict_function)

        predict_query = """
            SELECT PredictRent(number_of_rooms, number_of_bathrooms, days_on_market, rental_price) FROM HomeRentals LIMIT 10;
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result.columns), 1)
        self.assertEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()

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
from test.markers import forecast_skip_marker
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
            CREATE TABLE AirData (\
            unique_id TEXT(30),\
            ds TEXT(30),\
            y INTEGER);"""
        execute_query_fetch_all(cls.evadb, create_table_query)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
        create_table_query = """
            CREATE TABLE AirDataPanel (\
            unique_id TEXT(30),\
            ds TEXT(30),\
            y INTEGER,\
            trend INTEGER,\
            ylagged INTEGER);"""
        execute_query_fetch_all(cls.evadb, create_table_query)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
        create_table_query = """
            CREATE TABLE AirDataPanel (\
            unique_id TEXT(30),\
            ds TEXT(30),\
            y INTEGER,\
            trend INTEGER,\
            ylagged INTEGER);"""
        execute_query_fetch_all(cls.evadb, create_table_query)

<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
        create_table_query = """
            CREATE TABLE HomeData (\
            saledate TEXT(30),\
            ma INTEGER,
            type TEXT(30),\
            bedrooms INTEGER);"""
        execute_query_fetch_all(cls.evadb, create_table_query)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
        path = f"{EvaDB_ROOT_DIR}/data/forecasting/air-passengers.csv"
        load_query = f"LOAD CSV '{path}' INTO AirData;"
        execute_query_fetch_all(cls.evadb, load_query)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
        path = f"{EvaDB_ROOT_DIR}/data/forecasting/AirPassengersPanel.csv"
        load_query = f"LOAD CSV '{path}' INTO AirDataPanel;"
        execute_query_fetch_all(cls.evadb, load_query)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
        path = f"{EvaDB_ROOT_DIR}/data/forecasting/home_sales.csv"
        load_query = f"LOAD CSV '{path}' INTO HomeData;"
        execute_query_fetch_all(cls.evadb, load_query)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
    @classmethod
    def tearDownClass(cls):
        shutdown_ray()

        # clean up
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS AirData;")
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS HomeData;")

        execute_query_fetch_all(cls.evadb, "DROP FUNCTION IF EXISTS AirForecast;")
        execute_query_fetch_all(cls.evadb, "DROP FUNCTION IF EXISTS HomeForecast;")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS HomeRentals;")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-master
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS HomeRentals;")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
        execute_query_fetch_all(cls.evadb, "DROP TABLE IF EXISTS HomeRentals;")
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

    @forecast_skip_marker
    def test_forecast(self):
        create_predict_udf = """
<<<<<<< HEAD
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
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
            CREATE FUNCTION AirForecast FROM
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            CREATE FUNCTION AirForecast FROM
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
            CREATE FUNCTION AirForecast FROM
=======
            CREATE FUNCTION Forecast FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
            CREATE FUNCTION AirForecast FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
            CREATE FUNCTION Forecast FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
            CREATE FUNCTION AirForecast FROM
=======
            CREATE FUNCTION Forecast FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
            (SELECT unique_id, ds, y FROM AirData)
            TYPE Forecasting
            HORIZON 12
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
            CREATE FUNCTION Forecast FROM
            (SELECT unique_id, ds, y FROM AirData)
            TYPE Forecasting
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
            CREATE FUNCTION AirForecast FROM
            (SELECT unique_id, ds, y FROM AirData)
            TYPE Forecasting
            HORIZON 12
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
            CREATE FUNCTION Forecast FROM
            (SELECT unique_id, ds, y FROM AirData)
            TYPE Forecasting
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
            PREDICT 'y';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            SELECT AirForecast() order by y;
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            SELECT AirForecast(12) order by y;
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
            SELECT AirForecast() order by y;
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
            SELECT AirForecast() order by y;
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
            SELECT AirForecast(12) order by y;
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 12)
        self.assertEqual(
            result.columns,
            [
                "airforecast.unique_id",
                "airforecast.ds",
                "airforecast.y",
                "airforecast.y-lo",
                "airforecast.y-hi",
            ],
        )

    @pytest.mark.skip(
        reason="Neuralforecast intergration test takes too long to complete without GPU."
    )
    @forecast_skip_marker
    def test_forecast_neuralforecast(self):
        create_predict_udf = """
            CREATE FUNCTION AirPanelForecast FROM
            (SELECT unique_id, ds, y, trend FROM AirDataPanel)
            TYPE Forecasting
            HORIZON 12
            PREDICT 'y'
            LIBRARY 'neuralforecast'
            AUTO 'false'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT AirPanelForecast() order by y;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            [
                "airpanelforecast.unique_id",
                "airpanelforecast.ds",
                "airpanelforecast.y",
                "airpanelforecast.y-lo",
                "airpanelforecast.y-hi",
            ],
        )

        create_predict_udf = """
            CREATE FUNCTION AirPanelForecast FROM
            (SELECT unique_id, ds, y, trend FROM AirDataPanel)
            TYPE Forecasting
            HORIZON 12
            PREDICT 'y'
            LIBRARY 'neuralforecast'
            AUTO 'false'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT AirPanelForecast() order by y;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            ["airpanelforecast.unique_id", "airpanelforecast.ds", "airpanelforecast.y"],
        )

    @forecast_skip_marker
    def test_forecast_with_column_rename(self):
        create_predict_udf = """
            CREATE FUNCTION HomeForecast FROM
            (
                SELECT type, saledate, ma FROM HomeData
                WHERE bedrooms = 2
            )
            TYPE Forecasting
            HORIZON 12
            PREDICT 'ma'
            ID 'type'
            TIME 'saledate'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT HomeForecast();
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            [
                "homeforecast.type",
                "homeforecast.saledate",
                "homeforecast.ma",
                "homeforecast.ma-lo",
                "homeforecast.ma-hi",
            ],
        )
=======
            SELECT Forecast(12) FROM AirData;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(int(list(result.frames.iloc[:, -1])[-1]), 459)
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
            SELECT AirForecast() order by y;
=======
            SELECT AirForecast(12) order by y;
>>>>>>> 53dafecf (feat: sync master staging (#1050))
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 12)
        self.assertEqual(
            result.columns, ["airforecast.unique_id", "airforecast.ds", "airforecast.y"]
        )

        create_predict_udf = """
            CREATE FUNCTION AirPanelForecast FROM
            (SELECT unique_id, ds, y, trend FROM AirDataPanel)
            TYPE Forecasting
            HORIZON 12
            PREDICT 'y'
            LIBRARY 'neuralforecast'
            AUTO 'false'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT AirPanelForecast() order by y;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            ["airpanelforecast.unique_id", "airpanelforecast.ds", "airpanelforecast.y"],
        )

    @forecast_skip_marker
    def test_forecast_with_column_rename(self):
        create_predict_udf = """
            CREATE FUNCTION HomeForecast FROM
            (
                SELECT type, saledate, ma FROM HomeData
                WHERE bedrooms = 2
            )
            TYPE Forecasting
            HORIZON 12
            PREDICT 'ma'
            ID 'type'
            TIME 'saledate'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT HomeForecast();
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            ["homeforecast.type", "homeforecast.saledate", "homeforecast.ma"],
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
            SELECT Forecast(12) FROM AirData;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(int(list(result.frames.iloc[:, -1])[-1]), 459)
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
=======
            SELECT Forecast(12) FROM AirData;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(int(list(result.frames.iloc[:, -1])[-1]), 459)
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
            SELECT AirForecast() order by y;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 12)
        self.assertEqual(
            result.columns, ["airforecast.unique_id", "airforecast.ds", "airforecast.y"]
        )

        create_predict_udf = """
            CREATE FUNCTION AirPanelForecast FROM
            (SELECT unique_id, ds, y, trend FROM AirDataPanel)
            TYPE Forecasting
            HORIZON 12
            PREDICT 'y'
            LIBRARY 'neuralforecast'
            AUTO 'false'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT AirPanelForecast() order by y;
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            ["airpanelforecast.unique_id", "airpanelforecast.ds", "airpanelforecast.y"],
        )

    @forecast_skip_marker
    def test_forecast_with_column_rename(self):
        create_predict_udf = """
            CREATE FUNCTION HomeForecast FROM
            (
                SELECT type, saledate, ma FROM HomeData
                WHERE bedrooms = 2
            )
            TYPE Forecasting
            HORIZON 12
            PREDICT 'ma'
            ID 'type'
            TIME 'saledate'
            FREQUENCY 'M';
        """
        execute_query_fetch_all(self.evadb, create_predict_udf)

        predict_query = """
            SELECT HomeForecast();
        """
        result = execute_query_fetch_all(self.evadb, predict_query)
        self.assertEqual(len(result), 24)
        self.assertEqual(
            result.columns,
            ["homeforecast.type", "homeforecast.saledate", "homeforecast.ma"],
        )
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))


if __name__ == "__main__":
    unittest.main()

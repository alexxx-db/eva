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


<<<<<<< HEAD
import os
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
import pickle

import pandas as pd

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
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
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
>>>>>>> 53dafecf (feat: sync master staging (#1050))
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
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
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
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
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
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import setup


class ForecastModel(AbstractFunction):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
from evadb.catalog.catalog_type import NdArrayType
from evadb.udfs.abstract.abstract_udf import AbstractUDF
from evadb.udfs.decorators.decorators import forward, setup
from evadb.udfs.decorators.io_descriptors.data_types import PandasDataframe


class ForecastModel(AbstractUDF):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import setup


class ForecastModel(AbstractFunction):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    @property
    def name(self) -> str:
        return "ForecastModel"

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
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
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
<<<<<<< HEAD
>>>>>>> eva-source
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
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
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
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    @setup(cacheable=False, function_type="Forecasting", batchable=True)
    def setup(
        self,
        model_name: str,
        model_path: str,
        predict_column_rename: str,
        time_column_rename: str,
        id_column_rename: str,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        horizon: int,
        library: str,
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
    ):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
    ):
=======
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> 8eeef957 (Add support for Neuralforecast (#1115))
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
        horizon: int,
        library: str,
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
    ):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
    ):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        horizon: int,
        library: str,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        conf: int,
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
    ):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
    ):
<<<<<<< HEAD
        self.library = library
        if "neuralforecast" in self.library:
            from neuralforecast import NeuralForecast

            loaded_model = NeuralForecast.load(path=model_path)
            self.model_name = model_name[4:] if "Auto" in model_name else model_name
        else:
            with open(model_path, "rb") as f:
                loaded_model = pickle.load(f)
            self.model_name = model_name
        self.model = loaded_model
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library
        self.suggestion_dict = {
            1: "Predictions are flat. Consider using LIBRARY 'neuralforecast' for more accrate predictions.",
        }
        self.conf = conf
        self.hypers = None
        self.rmse = None
        if os.path.isfile(model_path + "_rmse"):
            with open(model_path + "_rmse", "r") as f:
                self.rmse = float(f.readline())
                if "arima" in model_name.lower():
                    self.hypers = "p,d,q: " + f.readline()

    def forward(self, data) -> pd.DataFrame:
        log_str = ""
        if self.library == "statsforecast":
            forecast_df = self.model.predict(
                h=self.horizon, level=[self.conf]
            ).reset_index()
        else:
            forecast_df = self.model.predict().reset_index()

        # Feedback
        if len(data) == 0 or list(list(data.iloc[0]))[0] is True:
            # Suggestions
            suggestion_list = []
            # 1: Flat predictions
            if self.library == "statsforecast":
                for type_here in forecast_df["unique_id"].unique():
                    if (
                        forecast_df.loc[forecast_df["unique_id"] == type_here][
                            self.model_name
                        ].nunique()
                        == 1
                    ):
                        suggestion_list.append(1)

            for suggestion in set(suggestion_list):
                log_str += "\nSUGGESTION: " + self.suggestion_dict[suggestion]

            # Metrics
            if self.rmse is not None:
                log_str += "\nMean normalized RMSE: " + str(self.rmse)
            if self.hypers is not None:
                log_str += "\nHyperparameters: " + self.hypers

            print(log_str)

        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name
                if self.library == "statsforecast"
                else self.model_name + "-median": self.predict_column_rename,
                self.model_name
                + "-lo-"
                + str(self.conf): self.predict_column_rename
                + "-lo",
                self.model_name
                + "-hi-"
                + str(self.conf): self.predict_column_rename
                + "-hi",
            }
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
=======
    @setup(cacheable=False, udf_type="Forecasting", batchable=True)
    def setup(self, model_name: str, model_path: str):
=======
    ):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
    @setup(cacheable=False, udf_type="Forecasting", batchable=True)
    def setup(self, model_name: str, model_path: str):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
        horizon: int,
        library: str,
    ):
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> eva-master
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
    @setup(cacheable=False, udf_type="Forecasting", batchable=True)
    def setup(self, model_name: str, model_path: str):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
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
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
        horizon: int,
        library: str,
    ):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
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
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
=======
        horizon: int,
        library: str,
    ):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
    @setup(cacheable=False, udf_type="Forecasting", batchable=True)
    def setup(self, model_name: str, model_path: str):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
        horizon: int,
        library: str,
    ):
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
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        f = open(model_path, "rb")
        loaded_model = pickle.load(f)
        f.close()
        self.model = loaded_model
        self.model_name = model_name
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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main

=======

    @forward(
        input_signatures=[],
        output_signatures=[
            PandasDataframe(
                columns=["y"],
                column_types=[
                    NdArrayType.FLOAT32,
                ],
                column_shapes=[(None,)],
            )
        ],
    )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
=======
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
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
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library
<<<<<<< HEAD

=======

    @forward(
        input_signatures=[],
        output_signatures=[
            PandasDataframe(
                columns=["y"],
                column_types=[
                    NdArrayType.FLOAT32,
                ],
                column_shapes=[(None,)],
            )
        ],
    )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
=======
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> georgia-tech-db-main
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
>>>>>>> eva-source
=======
=======
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
=======
=======
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        )[: self.horizon * forecast_df["unique_id"].nunique()]
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
        )
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        return forecast_df
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        )
<<<<<<< HEAD
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        return forecast_df
=======
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
        return forecast_df
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)

    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
        forecast_df = forecast_df.rename(columns={self.model_name: "y"})
        return pd.DataFrame(
            forecast_df,
            columns=[
                "y",
            ],
        )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        )[: self.horizon * forecast_df["unique_id"].nunique()]
=======
<<<<<<< HEAD
        )
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        return forecast_df
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        )
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        return forecast_df
=======
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)

    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
        forecast_df = forecast_df.rename(columns={self.model_name: "y"})
        return pd.DataFrame(
            forecast_df,
            columns=[
                "y",
            ],
        )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
<<<<<<< HEAD
        )[: self.horizon * forecast_df["unique_id"].nunique()]
=======
<<<<<<< HEAD
        )
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        return forecast_df
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
=======
        forecast_df = forecast_df.rename(columns={self.model_name: "y"})
        return pd.DataFrame(
            forecast_df,
            columns=[
                "y",
            ],
        )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 8eeef957 (Add support for Neuralforecast (#1115))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
=======
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
=======
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
=======
=======
=======
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
        )[: self.horizon * forecast_df["unique_id"].nunique()]
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
        )
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
        return forecast_df
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        )
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
        return forecast_df
<<<<<<< HEAD
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
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
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
=======
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)

    def forward(self, data) -> pd.DataFrame:
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
        forecast_df = forecast_df.rename(columns={self.model_name: "y"})
        return pd.DataFrame(
            forecast_df,
            columns=[
                "y",
            ],
        )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
=======
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
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
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main

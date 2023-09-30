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


import pickle

import pandas as pd

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import setup


class ForecastModel(AbstractFunction):
<<<<<<< HEAD
=======
=======
from evadb.catalog.catalog_type import NdArrayType
from evadb.udfs.abstract.abstract_udf import AbstractUDF
from evadb.udfs.decorators.decorators import forward, setup
from evadb.udfs.decorators.io_descriptors.data_types import PandasDataframe


class ForecastModel(AbstractUDF):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import setup


class ForecastModel(AbstractFunction):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
    @property
    def name(self) -> str:
        return "ForecastModel"

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
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
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        horizon: int,
        library: str,
    ):
=======
<<<<<<< HEAD
    ):
=======
    @setup(cacheable=False, udf_type="Forecasting", batchable=True)
    def setup(self, model_name: str, model_path: str):
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
        horizon: int,
        library: str,
    ):
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
        f = open(model_path, "rb")
        loaded_model = pickle.load(f)
        f.close()
        self.model = loaded_model
        self.model_name = model_name
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

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
        horizon = list(data.iloc[:, -1])[0]
        assert (
            type(horizon) is int
        ), "Forecast UDF expects integral horizon in parameter."
        forecast_df = self.model.predict(h=horizon)
<<<<<<< HEAD
=======
>>>>>>> eva-master
        self.predict_column_rename = predict_column_rename
        self.time_column_rename = time_column_rename
        self.id_column_rename = id_column_rename
        self.horizon = int(horizon)
        self.library = library

    def forward(self, data) -> pd.DataFrame:
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        if self.library == "statsforecast":
            forecast_df = self.model.predict(h=self.horizon)
        else:
            forecast_df = self.model.predict()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        forecast_df.reset_index(inplace=True)
        forecast_df = forecast_df.rename(
            columns={
                "unique_id": self.id_column_rename,
                "ds": self.time_column_rename,
                self.model_name: self.predict_column_rename,
            }
<<<<<<< HEAD
<<<<<<< HEAD
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
=======
<<<<<<< HEAD
        )
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
        return forecast_df
=======
        forecast_df = forecast_df.rename(columns={self.model_name: "y"})
        return pd.DataFrame(
            forecast_df,
            columns=[
                "y",
            ],
        )
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
        )[: self.horizon * forecast_df["unique_id"].nunique()]
        return forecast_df
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master

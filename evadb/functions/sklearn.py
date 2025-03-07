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

from evadb.functions.abstract.abstract_function import AbstractFunction
<<<<<<< HEAD
from evadb.utils.generic_utils import try_to_import_flaml_automl
=======
from evadb.utils.generic_utils import try_to_import_sklearn
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)


class GenericSklearnModel(AbstractFunction):
    @property
    def name(self) -> str:
        return "GenericSklearnModel"

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
    def setup(self, model_path: str, predict_col: str, **kwargs):
        try_to_import_flaml_automl()

        self.model = pickle.load(open(model_path, "rb"))
        self.predict_col = predict_col

    def forward(self, frames: pd.DataFrame) -> pd.DataFrame:
        # Do not pass the prediction column in the predict method for sklearn.
        frames.drop([self.predict_col], axis=1, inplace=True)
        predictions = self.model.predict(frames)
        predict_df = pd.DataFrame(predictions)
        # We need to rename the column of the output dataframe. For this we
        # shall rename it to the column name same as that of the predict column
        # passed in the training frames in EVA query.
        predict_df.rename(columns={0: self.predict_col}, inplace=True)
=======
    def setup(self, model_path: str, **kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
    def setup(self, model_path: str, predict_col: str, **kwargs):
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
        try_to_import_sklearn()

        self.model = pickle.load(open(model_path, "rb"))
        self.predict_col = predict_col

    def forward(self, frames: pd.DataFrame) -> pd.DataFrame:
        # Do not pass the prediction column in the predict method for sklearn.
        frames.drop([self.predict_col], axis=1, inplace=True)
        predictions = self.model.predict(frames)
        predict_df = pd.DataFrame(predictions)
        # We need to rename the column of the output dataframe. For this we
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
    def setup(self, model_path: str, predict_col: str, **kwargs):
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
        try_to_import_sklearn()

        self.model = pickle.load(open(model_path, "rb"))
        self.predict_col = predict_col

    def forward(self, frames: pd.DataFrame) -> pd.DataFrame:
        # Do not pass the prediction column in the predict method for sklearn.
        frames.drop([self.predict_col], axis=1, inplace=True)
        predictions = self.model.predict(frames)
        predict_df = pd.DataFrame(predictions)
        # We need to rename the column of the output dataframe. For this we
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
>>>>>>> georgia-tech-db-main
        try_to_import_sklearn()

        self.model = pickle.load(open(model_path, "rb"))

    def forward(self, frames: pd.DataFrame) -> pd.DataFrame:
        # The last column is the predictor variable column. Hence we do not
        # pass that column in the predict method for sklearn.
        predictions = self.model.predict(frames.iloc[:, :-1])
        predict_df = pd.DataFrame(predictions)
        # We need to rename the column of the output dataframe. For this we
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        # shall rename it to the column name same as that of the last column of
        # frames. This is because the last column of frames corresponds to the
        # variable we want to predict.
        predict_df.rename(columns={0: frames.columns[-1]}, inplace=True)
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
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
        # shall rename it to the column name same as that of the predict column
        # passed in the training frames in EVA query.
        predict_df.rename(columns={0: self.predict_col}, inplace=True)
>>>>>>> 4771bdec (Starting the change for XGBoost integration into EVADb. (#1232))
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> dda3558c (Starting the change for XGBoost integration into EVADb. (#1232))
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
        return predict_df

    def to_device(self, device: str):
        # TODO figure out how to control the GPU for ludwig models
        return self

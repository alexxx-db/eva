<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
.. _forecast:

>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
.. _forecast:

=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
.. _forecast:

>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
Time Series Forecasting
========================

You can train a forecasting model easily in EvaDB.

.. note::

   Install `statsforecast` in your EvaDB virtual environment: ``pip install eva[forecasting]``.

First, we create a table to insert required data.

.. code-block:: sql
   
   CREATE TABLE AirData (
    unique_id TEXT(30),
    ds TEXT(30),
    y INTEGER);

   LOAD CSV 'data/forecasting/air-passengers.csv' INTO AirData;


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
Next, we create a function of `TYPE Forecasting`. We must enter the column name on which we wish to forecast using `PREDICT`.

.. code-block:: sql
   
   CREATE FUNCTION IF NOT EXISTS Forecast FROM
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
Next, we create a UDF of `TYPE Forecasting`. We must enter the column name on which we wish to forecast using `predict`. Other options include `id` and `time` (they represent the unique id of the items and the time data if available).

.. code-block:: sql
   
   CREATE UDF IF NOT EXISTS Forecast FROM
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
Next, we create a function of `TYPE Forecasting`. We must enter the column name on which we wish to forecast using `PREDICT`.

.. code-block:: sql
   
   CREATE FUNCTION IF NOT EXISTS Forecast FROM
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
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
   (SELECT y FROM AirData)
   TYPE Forecasting
   PREDICT 'y';

This trains a forecasting model. The model can be called by providing the horizon for forecasting.

.. code-block:: sql

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
   SELECT Forecast(12);

Here, the horizon is `12`, which represents the forecast 12 steps into the future.


Forecast Parameters
-------------------

EvaDB's default forecast framework is `statsforecast <https://nixtla.github.io/statsforecast/>`_.

.. list-table:: Available Parameters
   :widths: 25 75

   * - PREDICT (str, required) 
     - The name of the column we wish to forecast.
   * - HORIZON (int, required) 
     - The number of steps into the future we wish to forecast.
   * - TIME (str, default: 'ds')
     - The name of the column that contains the datestamp, which should be of a format expected by Pandas, ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp. Please visit the `pandas documentation <https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html>`_ for details. If relevant column is not found, an auto increasing ID column will be used.
   * - ID (str, default: 'unique_id')
     - The name of column that represents an identifier for the series. If relevant column is not found, the whole table is considered as one series of data.
   * - LIBRARY (str, default: 'statsforecast')
     - We can select one of `statsforecast` (default) or `neuralforecast`. `statsforecast` provides access to statistical forecasting methods, while `neuralforecast` gives access to deep-learning based forecasting methods.
   * - MODEL (str, default: 'ARIMA')
<<<<<<< HEAD
<<<<<<< HEAD
     - If LIBRARY is `statsforecast`, we can select one of ARIMA, ting, ETS, Theta. The default is ARIMA. Check `Automatic Forecasting <https://nixtla.github.io/statsforecast/src/core/models_intro.html#automatic-forecasting>`_ to learn details about these models. If LIBRARY is `neuralforecast`, we can select one of NHITS or NBEATS. The default is NBEATS. Check `NBEATS docs <https://nixtla.github.io/neuralforecast/models.nbeats.html>`_ for details.
   * - AUTO (str, default: 'T')
     - If set to 'T', it enables automatic hyperparameter optimization. Must be set to 'T' for `statsforecast` library. One may set this parameter to `false` if LIBRARY is `neuralforecast` for faster (but less reliable) results.
   * - Frequency (str, default: 'auto')
     - A string indicating the frequency of the data. The common used ones are D, W, M, Y, which respectively represents day-, week-, month- and year- end frequency. The default value is M. Check `pandas available frequencies <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`_ for all available frequencies. If it is not provided, the frequency is attempted to be determined automatically.
=======
     - If LIBRARY is `statsforecast`, we can select one of ARIMA, CES, ETS, Theta. The default is ARIMA. Check `Automatic Forecasting <https://nixtla.github.io/statsforecast/src/core/models_intro.html#automatic-forecasting>`_ to learn details about these models. If LIBRARY is `neuralforecast`, we can select one of NHITS or NBEATS. The default is NBEATS. Check `NBEATS docs <https://nixtla.github.io/neuralforecast/models.nbeats.html>`_ for details.
   * - AUTO (str, default: 'T')
     - If set to 'T', it enables automatic hyperparameter optimization. Must be set to 'T' for `statsforecast` library. One may set this parameter to `false` if LIBRARY is `neuralforecast` for faster (but less reliable) results.
   * - Frequency (str, default: 'auto')
     - A string indicating the frequency of the data. The common used ones are D, W, M, Y, which repestively represents day-, week-, month- and year- end frequency. The default value is M. Check `pandas available frequencies <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`_ for all available frequencies. If it is not provided, the frequency is attempted to be determined automatically.
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
     - If LIBRARY is `statsforecast`, we can select one of ARIMA, ting, ETS, Theta. The default is ARIMA. Check `Automatic Forecasting <https://nixtla.github.io/statsforecast/src/core/models_intro.html#automatic-forecasting>`_ to learn details about these models. If LIBRARY is `neuralforecast`, we can select one of NHITS or NBEATS. The default is NBEATS. Check `NBEATS docs <https://nixtla.github.io/neuralforecast/models.nbeats.html>`_ for details.
   * - AUTO (str, default: 'T')
     - If set to 'T', it enables automatic hyperparameter optimization. Must be set to 'T' for `statsforecast` library. One may set this parameter to `false` if LIBRARY is `neuralforecast` for faster (but less reliable) results.
   * - Frequency (str, default: 'auto')
     - A string indicating the frequency of the data. The common used ones are D, W, M, Y, which respectively represents day-, week-, month- and year- end frequency. The default value is M. Check `pandas available frequencies <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`_ for all available frequencies. If it is not provided, the frequency is attempted to be determined automatically.
>>>>>>> 5b27053e (ran spellchecker)

Note: If columns other than the ones required as mentioned above are passed while creating the function, they will be treated as exogenous variables if LIBRARY is `neuralforecast`. Otherwise, they would be ignored.

Below is an example query specifying the above parameters:

.. code-block:: sql
   
   CREATE FUNCTION IF NOT EXISTS HomeRentalForecast FROM
   (SELECT saledate, ma, type FROM HomeData)
   TYPE Forecasting
   HORIZON 12
   PREDICT 'ma'
   TIME 'saledate'
   ID 'type'
   Frequency 'W';
<<<<<<< HEAD
<<<<<<< HEAD

Below is an example query with `neuralforecast` with `trend` column as exogenous and without automatic hyperparameter optimization:

.. code-block:: sql
   
    CREATE FUNCTION AirPanelForecast FROM
    (SELECT unique_id, ds, y, trend FROM AirDataPanel)
    TYPE Forecasting
    HORIZON 12
    PREDICT 'y'
    LIBRARY 'neuralforecast'
    AUTO 'f'
    FREQUENCY 'M';
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
   SELECT Forecast(12) FROM AirData;

Here, the horizon is `12`.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
   SELECT Forecast(12);

Here, the horizon is `12`, which represents the forecast 12 steps into the future.


Forecast Parameters
-------------------

EvaDB's default forecast framework is `statsforecast <https://nixtla.github.io/statsforecast/>`_.

.. list-table:: Available Parameters
   :widths: 25 75

   * - PREDICT (str, required) 
     - The name of the column we wish to forecast.
   * - HORIZON (int, required) 
     - The number of steps into the future we wish to forecast.
   * - TIME (str, default: 'ds')
     - The name of the column that contains the datestamp, which should be of a format expected by Pandas, ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp. Please visit the `pandas documentation <https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html>`_ for details. If relevant column is not found, an auto increasing ID column will be used.
   * - ID (str, default: 'unique_id')
     - The name of column that represents an identifier for the series. If relevant column is not found, the whole table is considered as one series of data.
   * - LIBRARY (str, default: 'statsforecast')
     - We can select one of `statsforecast` (default) or `neuralforecast`. `statsforecast` provides access to statistical forecasting methods, while `neuralforecast` gives access to deep-learning based forecasting methods.
   * - MODEL (str, default: 'ARIMA')
     - If LIBRARY is `statsforecast`, we can select one of ARIMA, CES, ETS, Theta. The default is ARIMA. Check `Automatic Forecasting <https://nixtla.github.io/statsforecast/src/core/models_intro.html#automatic-forecasting>`_ to learn details about these models. If LIBRARY is `neuralforecast`, we can select one of NHITS or NBEATS. The default is NBEATS. Check `NBEATS docs <https://nixtla.github.io/neuralforecast/models.nbeats.html>`_ for details.
   * - AUTO (str, default: 'T')
     - If set to 'T', it enables automatic hyperparameter optimization. Must be set to 'T' for `statsforecast` library. One may set this parameter to `false` if LIBRARY is `neuralforecast` for faster (but less reliable) results.
   * - Frequency (str, default: 'auto')
     - A string indicating the frequency of the data. The common used ones are D, W, M, Y, which repestively represents day-, week-, month- and year- end frequency. The default value is M. Check `pandas available frequencies <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`_ for all available frequencies. If it is not provided, the frequency is attempted to be determined automatically.

Note: If columns other than the ones required as mentioned above are passed while creating the function, they will be treated as exogenous variables if LIBRARY is `neuralforecast`. Otherwise, they would be ignored.

Below is an example query specifying the above parameters:

.. code-block:: sql
   
   CREATE FUNCTION IF NOT EXISTS HomeRentalForecast FROM
   (SELECT saledate, ma, type FROM HomeData)
   TYPE Forecasting
   HORIZON 12
   PREDICT 'ma'
   TIME 'saledate'
   ID 'type'
   Frequency 'W';
=======
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))

Below is an example query with `neuralforecast` with `trend` column as exogenous and without automatic hyperparameter optimization:

.. code-block:: sql
   
    CREATE FUNCTION AirPanelForecast FROM
    (SELECT unique_id, ds, y, trend FROM AirDataPanel)
    TYPE Forecasting
    HORIZON 12
    PREDICT 'y'
    LIBRARY 'neuralforecast'
    AUTO 'f'
<<<<<<< HEAD
    FREQUENCY 'M';
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    FREQUENCY 'M';
=======
    FREQUENCY 'M';
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> eva-master
=======
    FREQUENCY 'M';
>>>>>>> e8a181c5 (Add support for Neuralforecast (#1115))
<<<<<<< HEAD
>>>>>>> ca239aea (Add support for Neuralforecast (#1115))
=======
=======
    FREQUENCY 'M';
=======
   SELECT Forecast(12) FROM AirData;

Here, the horizon is `12`.
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
   SELECT Forecast(12);

Here, the horizon is `12`, which represents the forecast 12 steps into the future.


Forecast Parameters
-------------------

EvaDB's default forecast framework is `statsforecast <https://nixtla.github.io/statsforecast/>`_.

.. list-table:: Available Parameters
   :widths: 25 75

   * - PREDICT (str, required) 
     - The name of the column we wish to forecast.
   * - HORIZON (int, required) 
     - The number of steps into the future we wish to forecast.
   * - TIME (str, default: 'ds')
     - The name of the column that contains the datestamp, which should be of a format expected by Pandas, ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp. Please visit the `pandas documentation <https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html>`_ for details. If relevant column is not found, an auto increasing ID column will be used.
   * - ID (str, default: 'unique_id')
     - The name of column that represents an identifier for the series. If relevant column is not found, the whole table is considered as one series of data.
   * - LIBRARY (str, default: 'statsforecast')
     - We can select one of `statsforecast` (default) or `neuralforecast`. `statsforecast` provides access to statistical forecasting methods, while `neuralforecast` gives access to deep-learning based forecasting methods.
   * - MODEL (str, default: 'ARIMA')
     - If LIBRARY is `statsforecast`, we can select one of ARIMA, CES, ETS, Theta. The default is ARIMA. Check `Automatic Forecasting <https://nixtla.github.io/statsforecast/src/core/models_intro.html#automatic-forecasting>`_ to learn details about these models. If LIBRARY is `neuralforecast`, we can select one of NHITS or NBEATS. The default is NBEATS. Check `NBEATS docs <https://nixtla.github.io/neuralforecast/models.nbeats.html>`_ for details.
   * - AUTO (str, default: 'T')
     - If set to 'T', it enables automatic hyperparameter optimization. Must be set to 'T' for `statsforecast` library. One may set this parameter to `false` if LIBRARY is `neuralforecast` for faster (but less reliable) results.
   * - Frequency (str, default: 'auto')
     - A string indicating the frequency of the data. The common used ones are D, W, M, Y, which repestively represents day-, week-, month- and year- end frequency. The default value is M. Check `pandas available frequencies <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`_ for all available frequencies. If it is not provided, the frequency is attempted to be determined automatically.

Note: If columns other than the ones required as mentioned above are passed while creating the function, they will be treated as exogenous variables if LIBRARY is `neuralforecast`. Otherwise, they would be ignored.

Below is an example query specifying the above parameters:

.. code-block:: sql
   
   CREATE FUNCTION IF NOT EXISTS HomeRentalForecast FROM
   (SELECT saledate, ma, type FROM HomeData)
   TYPE Forecasting
   HORIZON 12
   PREDICT 'ma'
   TIME 'saledate'
   ID 'type'
   Frequency 'W';

Below is an example query with `neuralforecast` with `trend` column as exogenous and without automatic hyperparameter optimization:

.. code-block:: sql
   
    CREATE FUNCTION AirPanelForecast FROM
    (SELECT unique_id, ds, y, trend FROM AirDataPanel)
    TYPE Forecasting
    HORIZON 12
    PREDICT 'y'
    LIBRARY 'neuralforecast'
    AUTO 'f'
    FREQUENCY 'M';
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)

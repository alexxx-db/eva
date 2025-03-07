=========
Concepts
=========

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
=======
>>>>>>> d8799826 (docs: updates)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
EvaDB is designed around three key concepts: 
=======
Here is a list of key concepts in EvaDB. If you have any questions, ask the community on `Slack <https://evadb.ai/community>`__.
=======
EvaDB is designed around three key concepts: 
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
=======
>>>>>>> eva-source
EvaDB is designed around three key concepts: 
=======
Here is a list of key concepts in EvaDB. If you have any questions, ask the community on `Slack <https://evadb.ai/community>`__.
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
EvaDB is designed around three key concepts: 
=======
Here is a list of key concepts in EvaDB. If you have any questions, ask the community on `Slack <https://evadb.ai/community>`__.
<<<<<<< HEAD
=======
EvaDB is designed around three key concepts: 
=======
Here is a list of key concepts in EvaDB. If you have any questions, ask the community on `Slack <https://evadb.ai/community>`__.
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> d8799826 (docs: updates)
=======
>>>>>>> georgia-tech-db-main

EvaQL: AI-Centric Query Language
--------------------------------

EvaDB supports a SQL-like query language, called ``EvaQL``, designed to assist software developers in bringing AI into their applications.

Here is set of illustrative EvaQL queries for a ChatGPT-based video question answering app. This EvaDB app connects to collection of news videos stored in a folder and runs an AI query for extracting audio transcripts from the videos using a Hugging Face model, followed by another AI query for question answering using ChatGPT.

.. code-block::sql

    --- Load a collection of news videos into the 'news_videos' table
    --- This command returns a Pandas Dataframe with the query's output
    --- In this case, the output indicates the number of loaded videos
    LOAD VIDEO 'news_videos/*.mp4' INTO VIDEOS;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

(1) AI Queries
(2) AI Functions
(3) AI-Centric Query Optimization

<<<<<<< HEAD
.. note::

    Have a question or want to give feedback? Join us on `Slack <https://evadb.ai/community>`__!

AI Queries
----------

EvaDB supports a high-level, declarative language for writing AI queries that is similar to SQL. Software developers can bring AI-powered features into their database applications using AI queries. 

Here are some illustrative **AI queries** for a ChatGPT-based video question answering app. This AI app first connects to collection of news videos stored in a local folder. It then runs an AI query for extracting audio transcripts from the videos using a Hugging Face model. Lastly, it runs another AI query for answering the user's question over the transcript using ChatGPT.

.. code-block:: sql

    --- Load a collection of news videos into the 'news_videos' table
    --- This command returns a Pandas Dataframe with the query's output
    --- In this case, the output indicates the number of loaded videos
    LOAD VIDEO 'news_videos/*.mp4' INTO VIDEOS;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

(1) AI Queries
(2) AI Functions
(3) AI-Centric Query Optimization

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
.. note::

    Have a question or want to give feedback? Join us on `Slack <https://evadb.ai/community>`__!

AI Queries
----------

EvaDB supports a high-level, declarative language for writing AI queries that is similar to SQL. Software developers can bring AI-powered features into their database applications using AI queries. 

Here are some illustrative **AI queries** for a ChatGPT-based video question answering app. This AI app first connects to collection of news videos stored in a local folder. It then runs an AI query for extracting audio transcripts from the videos using a Hugging Face model. Lastly, it runs another AI query for answering the user's question over the transcript using ChatGPT.

.. code-block:: sql

    --- Load a collection of news videos into the 'news_videos' table
    --- This command returns a Pandas Dataframe with the query's output
    --- In this case, the output indicates the number of loaded videos
    LOAD VIDEO 'news_videos/*.mp4' INTO VIDEOS;
>>>>>>> 2dacff69 (feat: sync master staging (#1050))

(1) AI Queries
(2) AI Functions
(3) AI-Centric Query Optimization

<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
.. note::

    Have a question or want to give feedback? Join us on `Slack <https://evadb.ai/community>`__!

AI Queries
----------

EvaDB supports a high-level, declarative language for writing AI queries that is similar to SQL. Software developers can bring AI-powered features into their database applications using AI queries. 

Here are some illustrative **AI queries** for a ChatGPT-based video question answering app. This AI app first connects to collection of news videos stored in a local folder. It then runs an AI query for extracting audio transcripts from the videos using a Hugging Face model. Lastly, it runs another AI query for answering the user's question over the transcript using ChatGPT.

.. code-block:: sql

    --- Load a collection of news videos into the 'news_videos' table
    --- This command returns a Pandas Dataframe with the query's output
    --- In this case, the output indicates the number of loaded videos
    LOAD VIDEO 'news_videos/*.mp4' INTO VIDEOS;


<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    --- Define an AI function that wraps around a speech-to-text model 
    --- This model is hosted on Hugging Face which has built-in support in EvaDB
    --- After creating the function, we can use the function in any future query
    CREATE FUNCTION SpeechRecognizer 
        TYPE HuggingFace 
        TASK 'automatic-speech-recognition' 
        MODEL 'openai/whisper-base';

    --  EvaDB automatically extracts the audio from the videos
    --- We only need to run the SpeechRecognizer function on the 'audio' column 
    --- to get the transcript and persist it in a table called 'transcripts'
    CREATE TABLE transcripts AS 
        SELECT SpeechRecognizer(audio) from news_videos;
=======
The :ref:`Getting Started` page shows how you can use EvaDB for different AI tasks and how you can easily extend EvaDB to support your custom deep learning model through user-defined functions.

The :ref:`User Guides<image classification>` section contains Jupyter Notebooks that demonstrate how to use various features of EvaDB. Each notebook includes a link to Google Colab, where you can run the code yourself.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main

    --- Lastly, we run the ChatGPT query for question answering 
    --- This query is based on the 'transcripts' table 
    --- The 'transcripts' table has a column called 'text' with the transcript text
    --- Since ChatGPT is a built-in function in EvaDB, we don't have to define it
    --- We can directly use ChatGPT() in any query
    --- We will only need to set the OPENAI_API_KEY as an environment variable
    SELECT ChatGPT('Is this video summary related to Ukraine russia war', text) 
        FROM TEXT_SUMMARY;

By reducing the complexity of the AI app to a few short, simple queries, EvaDB helps in writing **more maintainable, extensible, and scalable** AI apps. 

You can build on top of AI queries written by other developers. You can **chain together** multiple AI models in a single query to accomplish complicated tasks with minimal programming.

AI Functions
------------

In EvaDB, ``functions`` are typically thin wrappers around AI models and are extensively used in AI queries.

Here is an `illustrative AI function for classifying the digit in MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 

To register an user-defined function, we use the :ref:`CREATE FUNCTION<create-function>` statement:

.. code-block:: sql

    --- Create an MNIST image classifier function
    --- The function's implementation is in the 'mnist_image_classifier.py' file
=======
<<<<<<< HEAD
    --- Define an AI function that wraps around a speech-to-text model 
    --- This model is hosted on Hugging Face which has built-in support in EvaDB
    --- After creating the function, we can use the function in any future query
    CREATE UDF SpeechRecognizer 
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
    --- Define an AI function that wraps around a speech-to-text model 
    --- This model is hosted on Hugging Face which has built-in support in EvaDB
    --- After creating the function, we can use the function in any future query
    CREATE FUNCTION SpeechRecognizer 
>>>>>>> georgia-tech-db-main
        TYPE HuggingFace 
        TASK 'automatic-speech-recognition' 
        MODEL 'openai/whisper-base';

    --  EvaDB automatically extracts the audio from the videos
<<<<<<< HEAD
    --- We only need to run the SpeechRecognizer UDF on the 'audio' column 
=======
    --- We only need to run the SpeechRecognizer function on the 'audio' column 
>>>>>>> georgia-tech-db-main
    --- to get the transcript and persist it in a table called 'transcripts'
    CREATE TABLE transcripts AS 
        SELECT SpeechRecognizer(audio) from news_videos;
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
The :ref:`Getting Started` page shows how you can use EvaDB for different AI tasks and how you can easily extend EvaDB to support your custom deep learning model through user-defined functions.

The :ref:`User Guides<image classification>` section contains Jupyter Notebooks that demonstrate how to use various features of EvaDB. Each notebook includes a link to Google Colab, where you can run the code yourself.
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

    --- Lastly, we run the ChatGPT query for question answering 
    --- This query is based on the 'transcripts' table 
    --- The 'transcripts' table has a column called 'text' with the transcript text
    --- Since ChatGPT is a built-in function in EvaDB, we don't have to define it
    --- We can directly use ChatGPT() in any query
    --- We will only need to set the OPENAI_KEY as an environment variable
    SELECT ChatGPT('Is this video summary related to Ukraine russia war', text) 
        FROM TEXT_SUMMARY;

By reducing the complexity of the AI app to a few short, simple queries, EvaDB helps in writing **more maintainable, extensible, and scalable** AI apps. 

You can build on top of AI queries written by other developers. You can **chain together** multiple AI models in a single query to accomplish complicated tasks with minimal programming.

AI Functions
------------

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
<<<<<<< HEAD
=======
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
<<<<<<< HEAD
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_. 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
In EvaDB, ``functions`` are typically thin wrappers around AI models and are extensively used in AI queries.
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
>>>>>>> eva-source
=======
>>>>>>> 9cc72b7b (docs: updates)
>>>>>>> georgia-tech-db-main

Here is an `illustrative AI function for classifying the digit in MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 

To register an user-defined function, we use the :ref:`CREATE FUNCTION<create-function>` statement:

.. code-block:: sql

    --- Create an MNIST image classifier function
<<<<<<< HEAD
<<<<<<< HEAD
    --- The function's implementation is in the 'mnist_image_classifier.py' file
=======
<<<<<<< HEAD
=======
>>>>>>> georgia-tech-db-main
    --- The function's implementation code is in 'mnist_image_classifier.py'
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
    --- The function's implementation is in the 'mnist_image_classifier.py' file
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
=======
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 9cc72b7b (docs: updates)
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    --- Define an AI function that wraps around a speech-to-text model 
    --- This model is hosted on Hugging Face which has built-in support in EvaDB
    --- After creating the function, we can use the function in any future query
    CREATE UDF SpeechRecognizer 
        TYPE HuggingFace 
        TASK 'automatic-speech-recognition' 
        MODEL 'openai/whisper-base';

    --  EvaDB automatically extracts the audio from the videos
    --- We only need to run the SpeechRecognizer UDF on the 'audio' column 
    --- to get the transcript and persist it in a table called 'transcripts'
    CREATE TABLE transcripts AS 
        SELECT SpeechRecognizer(audio) from news_videos;

    --- Lastly, we run the ChatGPT query for question answering 
    --- This query is based on the 'transcripts' table 
    --- The 'transcripts' table has a column called 'text' with the transcript text
    --- Since ChatGPT is a built-in function in EvaDB, we don't have to define it
<<<<<<< HEAD
=======
<<<<<<< HEAD
    --- We can directly use ChatGPT() in any query
    --- We will only need to set the OPENAI_KEY as an environment variable
    SELECT ChatGPT('Is this video summary related to Ukraine russia war', text) 
        FROM TEXT_SUMMARY;

By reducing the complexity of the AI app to a few short, simple queries, EvaDB helps in writing **more maintainable, extensible, and scalable** AI apps. 

You can build on top of AI queries written by other developers. You can **chain together** multiple AI models in a single query to accomplish complicated tasks with minimal programming.
=======
>>>>>>> georgia-tech-db-main
    --- We can directly use it in any query
    --- We need to set the OPENAI_KEY as an environment variable
    SELECT ChatGPT('Is this video summary related to Ukraine russia war', text) 
        FROM TEXT_SUMMARY;

EvaQL reduces the complexity of the app, leading to more maintainable code that allows developers to build on top of each other's queries. A single AI query can use multiple AI models to accomplish complicated tasks with minimal programming.

AI-Centric Query Optimization 
-----------------------------

EvaDB optimizes the AI queries to save money spent on running models and reduce query execution time. It contains a novel `Cascades-style extensible query optimizer <https://www.cse.iitb.ac.in/infolab/Data/Courses/CS632/Papers/Cascades-graefe.pdf>`__  tailored for AI queries. Query optimization has powered traditional SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware.

EvaDB accelerates AI queries using a collection of optimizations inspired by SQL database systems including cost-based function predicate reordering, function caching, sampling, etc.
<<<<<<< HEAD
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

AI Functions
------------

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
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
>>>>>>> d8799826 (docs: updates)
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_. 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)

To register an user-defined function, use the ``CREATE FUNCTION`` statement:
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_. 
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
>>>>>>> eva-master
=======
In EvaDB, ``functions`` are typically thin wrappers around AI models and are extensively used in AI queries.
>>>>>>> 5f27824c (docs: updates)
>>>>>>> 9cc72b7b (docs: updates)
>>>>>>> d8799826 (docs: updates)

Here is an `illustrative AI function for classifying the digit in MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 

To register an user-defined function, we use the :ref:`CREATE FUNCTION<create-function>` statement:
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_. 
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/udfs/mnist_image_classifier.py>`_. 
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
=======
=======
``Functions`` are typically thin wrappers around AI models and are extensively used in queries. Here is an `illustrative AI function for classifying MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)

To register an user-defined function, use the ``CREATE FUNCTION`` statement:
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

.. code-block:: sql

    --- Create an MNIST image classifier function
<<<<<<< HEAD
    --- The function's implementation code is in 'mnist_image_classifier.py'
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
    --- The function's implementation code is in 'mnist_image_classifier.py'
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
    --- The function's implementation is in the 'mnist_image_classifier.py' file
>>>>>>> 9cc72b7b (docs: updates)
>>>>>>> d8799826 (docs: updates)
=======
    --- The function's implementation code is in 'mnist_image_classifier.py'
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    CREATE FUNCTION MnistImageClassifier
        IMPL 'mnist_image_classifier.py'

After registering ``MnistImageClassifier`` function, you can call the function in the ``SELECT`` and/or ``WHERE`` clauses of any query.

.. code-block:: sql

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
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> d8799826 (docs: updates)
=======
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    --- Get the output of 'MnistImageClassifier' on the 30th video frame (id=30)
=======
    --- Get the output of 'MnistImageClassifier' on frame id 30
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
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
>>>>>>> georgia-tech-db-main
=======
    --- Get the output of 'MnistImageClassifier' on the 30th video frame (id=30)
>>>>>>> 9cc72b7b (docs: updates)
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
    --- Get the output of 'MnistImageClassifier' on the 30th video frame (id=30)
>>>>>>> 9cc72b7b (docs: updates)
>>>>>>> d8799826 (docs: updates)
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    --- This query returns the results of the image classification function
    --- In this case, it is the digit in the 30th frame in the video
    SELECT data, id, MnistImageClassifier(data).label 
    FROM MnistVideo  
    WHERE id = 30;

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
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> eva-master
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
    --- Use the 'MnistImageClassifier' function's output to filter frames
    --- This query returns the frame ids of the frames with digit 6
    --- We limit to the first five frames containing digit 6
    SELECT data, id, MnistImageClassifier(data).label 
    FROM MnistVideo  
    WHERE MnistImageClassifier(data).label = '6'
    LIMIT 5;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9cc72b7b (docs: updates)
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
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))

AI-Centric Query Optimization
-----------------------------

EvaDB optimizes the AI queries to save money spent on running models and reduce query execution time. It contains a novel `Cascades-style query optimizer <https://faculty.cc.gatech.edu/~jarulraj/courses/8803-s21/slides/22-cascades.pdf>`__  tailored for AI queries.

<<<<<<< HEAD
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
Save time and money
----------------------

EvaDB automatically optimizes the queries to save inference cost and query execution time using its Cascades-style extensible query optimizer. EvaDB's optimizer is tailored for AI pipelines. The Cascades query optimization framework has worked well in SQL database systems for several decades. Query optimization in EvaDB is the bridge that connects the declarative query language to efficient execution.

EvaDB accelerates AI pipelines using a collection of optimizations inspired by SQL database systems including function caching, sampling, and cost-based operator reordering.

EvaDB supports an AI-oriented query language for analyzing both structured and unstructured data. Here are some illustrative apps:


The :ref:`Getting Started` page shows how you can use EvaDB for different AI tasks and how you can easily extend EvaDB to support your custom deep learning model through user-defined functions.

The :ref:`User Guides<image classification>` section contains Jupyter Notebooks that demonstrate how to use various features of EvaDB. Each notebook includes a link to Google Colab, where you can run the code yourself.




User-Defined Function (UDF) or Function
------------------------------------------

User-defined functions are thin wrappers around deep learning models. They 
allow us to use deep learning models in AI queries.

Here is an illustrative UDF for classifying MNIST images.

.. code-block:: bash

    !wget -nc https://raw.githubusercontent.com/georgia-tech-db/evadb/master/evadb/udfs/mnist_image_classifier.py

.. code-block:: python

    cursor.create_function("MnistImageClassifier", True, 'mnist_image_classifier.py')
    response = cursor.df()
    print(response)

That's it! You can now use the newly registered UDF anywhere in the query -- in the ``select`` or ``filter`` calls.

.. code-block:: python

    query = cursor.table("MNISTVideo")
    query = query.filter("id = 30 OR id = 50 OR id = 70")

    # Here, we are selecting the output of the function
    query = query.select("data, MnistImageClassifier(data).label")
    response = query.df()

.. code-block:: python

>>>>>>> c63abee7 (release: merge staging into master (#1032))
    query2 = cursor.table("MNISTVideo")

    # Here, we are also filtering based on the output of the function
    query2 = query2.filter("MnistImageClassifier(data).label = '6' AND id < 10")
    query2 = query2.select("data, MnistImageClassifier(data).label")
    response = query2.df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> eva-master
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> d8799826 (docs: updates)
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

AI-Centric Query Optimization
-----------------------------

EvaDB optimizes the AI queries to save money spent on running models and reduce query execution time. It contains a novel `Cascades-style query optimizer <https://www.cse.iitb.ac.in/infolab/Data/Courses/CS632/Papers/Cascades-graefe.pdf>`__  tailored for AI queries.

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
<<<<<<< HEAD
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
Save time and money
----------------------

EvaDB automatically optimizes the queries to save inference cost and query execution time using its Cascades-style extensible query optimizer. EvaDB's optimizer is tailored for AI pipelines. The Cascades query optimization framework has worked well in SQL database systems for several decades. Query optimization in EvaDB is the bridge that connects the declarative query language to efficient execution.

EvaDB accelerates AI pipelines using a collection of optimizations inspired by SQL database systems including function caching, sampling, and cost-based operator reordering.

EvaDB supports an AI-oriented query language for analyzing both structured and unstructured data. Here are some illustrative apps:


The :ref:`Getting Started` page shows how you can use EvaDB for different AI tasks and how you can easily extend EvaDB to support your custom deep learning model through user-defined functions.

The :ref:`User Guides<image classification>` section contains Jupyter Notebooks that demonstrate how to use various features of EvaDB. Each notebook includes a link to Google Colab, where you can run the code yourself.




User-Defined Function (UDF) or Function
------------------------------------------

User-defined functions are thin wrappers around deep learning models. They 
allow us to use deep learning models in AI queries.

Here is an illustrative UDF for classifying MNIST images.

.. code-block:: bash

    !wget -nc https://raw.githubusercontent.com/georgia-tech-db/evadb/master/evadb/udfs/mnist_image_classifier.py

.. code-block:: python

    cursor.create_function("MnistImageClassifier", True, 'mnist_image_classifier.py')
    response = cursor.df()
    print(response)

That's it! You can now use the newly registered UDF anywhere in the query -- in the ``select`` or ``filter`` calls.

.. code-block:: python

    query = cursor.table("MNISTVideo")
    query = query.filter("id = 30 OR id = 50 OR id = 70")

    # Here, we are selecting the output of the function
    query = query.select("data, MnistImageClassifier(data).label")
    response = query.df()

.. code-block:: python

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    query2 = cursor.table("MNISTVideo")

    # Here, we are also filtering based on the output of the function
    query2 = query2.filter("MnistImageClassifier(data).label = '6' AND id < 10")
    query2 = query2.select("data, MnistImageClassifier(data).label")
    response = query2.df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
=======
>>>>>>> eva-source
>>>>>>> eva-master
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))

AI-Centric Query Optimization
-----------------------------

EvaDB optimizes the AI queries to save money spent on running models and reduce query execution time. It contains a novel `Cascades-style query optimizer <https://www.cse.iitb.ac.in/infolab/Data/Courses/CS632/Papers/Cascades-graefe.pdf>`__  tailored for AI queries.

<<<<<<< HEAD
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
>>>>>>> 70850a8b (feat: sync master staging (#1050))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 03a6c555 (feat: sync master staging (#1050))
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
>>>>>>> 5f27824c (docs: updates)
<<<<<<< HEAD
>>>>>>> 9cc72b7b (docs: updates)
<<<<<<< HEAD
>>>>>>> d8799826 (docs: updates)
=======
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
=======
=======
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
Save time and money
----------------------

EvaDB automatically optimizes the queries to save inference cost and query execution time using its Cascades-style extensible query optimizer. EvaDB's optimizer is tailored for AI pipelines. The Cascades query optimization framework has worked well in SQL database systems for several decades. Query optimization in EvaDB is the bridge that connects the declarative query language to efficient execution.

EvaDB accelerates AI pipelines using a collection of optimizations inspired by SQL database systems including function caching, sampling, and cost-based operator reordering.

EvaDB supports an AI-oriented query language for analyzing both structured and unstructured data. Here are some illustrative apps:


The :ref:`Getting Started` page shows how you can use EvaDB for different AI tasks and how you can easily extend EvaDB to support your custom deep learning model through user-defined functions.

The :ref:`User Guides<image classification>` section contains Jupyter Notebooks that demonstrate how to use various features of EvaDB. Each notebook includes a link to Google Colab, where you can run the code yourself.




User-Defined Function (UDF) or Function
------------------------------------------

User-defined functions are thin wrappers around deep learning models. They 
allow us to use deep learning models in AI queries.

Here is an illustrative UDF for classifying MNIST images.

.. code-block:: bash

    !wget -nc https://raw.githubusercontent.com/georgia-tech-db/evadb/master/evadb/udfs/mnist_image_classifier.py

.. code-block:: python

    cursor.create_function("MnistImageClassifier", True, 'mnist_image_classifier.py')
    response = cursor.df()
    print(response)

That's it! You can now use the newly registered UDF anywhere in the query -- in the ``select`` or ``filter`` calls.

.. code-block:: python

    query = cursor.table("MNISTVideo")
    query = query.filter("id = 30 OR id = 50 OR id = 70")

    # Here, we are selecting the output of the function
    query = query.select("data, MnistImageClassifier(data).label")
    response = query.df()

.. code-block:: python

>>>>>>> c63abee7 (release: merge staging into master (#1032))
    query2 = cursor.table("MNISTVideo")

    # Here, we are also filtering based on the output of the function
    query2 = query2.filter("MnistImageClassifier(data).label = '6' AND id < 10")
    query2 = query2.select("data, MnistImageClassifier(data).label")
    response = query2.df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
=======
>>>>>>> eva-source
=======
>>>>>>> 9fe75f29 (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
>>>>>>> 53dafecf (feat: sync master staging (#1050))
>>>>>>> 2eef5e8f (feat: sync master staging (#1050))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> eva-source
=======
>>>>>>> 70850a8b (feat: sync master staging (#1050))
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main

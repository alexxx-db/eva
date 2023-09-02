=========
Concepts
=========

EvaDB is designed around three key concepts: 

(1) AI Queries
(2) AI Functions
(3) AI-Centric Query Optimization

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

In EvaDB, ``functions`` are typically thin wrappers around AI models and are extensively used in AI queries.

Here is an `illustrative AI function for classifying the digit in MNIST images <https://github.com/georgia-tech-db/evadb/blob/master/evadb/functions/mnist_image_classifier.py>`_. 

To register an user-defined function, we use the :ref:`CREATE FUNCTION<create-function>` statement:

.. code-block:: sql

    --- Create an MNIST image classifier function
    --- The function's implementation is in the 'mnist_image_classifier.py' file
    CREATE FUNCTION MnistImageClassifier
        IMPL 'mnist_image_classifier.py'

After registering ``MnistImageClassifier`` function, you can call the function in the ``SELECT`` and/or ``WHERE`` clauses of any query.

.. code-block:: sql

    --- Get the output of 'MnistImageClassifier' on the 30th video frame (id=30)
    --- This query returns the results of the image classification function
    --- In this case, it is the digit in the 30th frame in the video
    SELECT data, id, MnistImageClassifier(data).label 
    FROM MnistVideo  
    WHERE id = 30;

    --- Use the 'MnistImageClassifier' function's output to filter frames
    --- This query returns the frame ids of the frames with digit 6
    --- We limit to the first five frames containing digit 6
    SELECT data, id, MnistImageClassifier(data).label 
    FROM MnistVideo  
    WHERE MnistImageClassifier(data).label = '6'
    LIMIT 5;

AI-Centric Query Optimization
-----------------------------

EvaDB optimizes the AI queries to save money spent on running models and reduce query execution time. It contains a novel `Cascades-style query optimizer <https://www.cse.iitb.ac.in/infolab/Data/Courses/CS632/Papers/Cascades-graefe.pdf>`__  tailored for AI queries.

<<<<<<< HEAD
Query optimization has powered SQL database systems for several decades. It is the bridge that connects the declarative query language to efficient query execution on hardware. EvaDB accelerates AI queries using a collection of optimizations detailed in the :ref:`optimizations<optimizations>` page.
=======
    query2 = cursor.table("MNISTVideo")

    # Here, we are also filtering based on the output of the function
    query2 = query2.filter("MnistImageClassifier(data).label = '6' AND id < 10")
    query2 = query2.select("data, MnistImageClassifier(data).label")
    response = query2.df()
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

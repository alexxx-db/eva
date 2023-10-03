.. _optimizations:

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
EvaDB Optimizations 🛠️
======================

EvaDB optimizes the evaluation of *AI functions* using these optimizations:
<<<<<<< HEAD

1️⃣ *Function Result Caching*: EvaDB caches results of expensive function invocations during query processing. This accelerates subsequent queries over the same dataset. 📂

2️⃣ *Query Predicate Reordering*: Efficiency is key. EvaDB strategically reorders query predicates to prioritize evaluation of lower-cost and more selective predicates. 🔀

3️⃣ *Parallel Query Processing*: EvaDB runs AI models in parallel to optimize GPU utilization by leveraging the Ray execution framework. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🎩

<<<<<<< HEAD
<<<<<<< HEAD
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 5678c9a3 (docs: updated images)
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
.. include:: ../shared/designs/design6.rst
=======
Optimizations
=============
<<<<<<< HEAD
<<<<<<< HEAD
=======
EvaDB Optimizations 🛠️
======================
>>>>>>> 278683f6 (updates)

EvaDB optimizes the evaluation of AI functions using these optimizations:
=======
>>>>>>> aed2d9cf (docs: updated outdated reference to SHOW UDF)

1️⃣ *Function Result Caching*: EvaDB caches results of expensive function invocations during query processing. This accelerates subsequent queries over the same dataset. 📂

2️⃣ *Query Predicate Reordering*: Efficiency is key. EvaDB strategically reorders query predicates to prioritize evaluation of lower-cost and more selective predicates. 🔀

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

EvaDB optimizes the evaluation of user-defined functions in three manifolds.

>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======

EvaDB optimizes the evaluation of user-defined functions in three manifolds.

>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
1. Cache expensive function invocations and reuse their results in future invocations.
2. Cost-based predicate reordering to evaluate fast and selective predicate first.
3. Ray-based distributed inference. EvaDB not only parallelizes model inference to improve GPU utilization but also builds pipeline to parallelize CPU processing (i.e., loading and decoding data).
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> e1643547 (updates)
=======
3️⃣ Parallel Processing with Ray: Leveraging the Ray framework, EvaDB runs AI models in parallel, optimizing GPU utilization. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🚀

These techniques ensure superior performance and responsiveness in EvaDB's AI function evaluations.
>>>>>>> 278683f6 (updates)
=======
3️⃣ Parallel Processing with Ray: Leveraging the Ray framework, EvaDB runs AI models in parallel, optimizing GPU utilization. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🚄🎩

These techniques ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉
>>>>>>> ecf47955 (updates)
=======
3️⃣ *Parallel Query Processing*: EvaDB runs AI models in parallel to optimize GPU utilization by leveraging the Ray execution framework. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🎩

These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉
>>>>>>> aed2d9cf (docs: updated outdated reference to SHOW UDF)
=======
.. include:: ../shared/design6.rst
>>>>>>> df4d8a35 (docs: updates)
=======
.. include:: ../shared/designs/design6.rst
>>>>>>> e867f37e (docs: updated images)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉
>>>>>>> aed2d9cf (docs: updated outdated reference to SHOW UDF)
<<<<<<< HEAD
>>>>>>> 0d46eb7c (docs: updated outdated reference to SHOW UDF)
=======
=======
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

.. include:: ../shared/design6.rst
>>>>>>> df4d8a35 (docs: updates)
<<<<<<< HEAD
>>>>>>> f1e2bddc (docs: updates)
=======
=======
.. include:: ../shared/designs/design6.rst
>>>>>>> e867f37e (docs: updated images)
>>>>>>> 5678c9a3 (docs: updated images)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)

.. _optimizations:

<<<<<<< HEAD
EvaDB Optimizations 🛠️
======================

EvaDB optimizes the evaluation of *AI functions* using these optimizations:

1️⃣ *Function Result Caching*: EvaDB caches results of expensive function invocations during query processing. This accelerates subsequent queries over the same dataset. 📂

2️⃣ *Query Predicate Reordering*: Efficiency is key. EvaDB strategically reorders query predicates to prioritize evaluation of lower-cost and more selective predicates. 🔀

3️⃣ *Parallel Query Processing*: EvaDB runs AI models in parallel to optimize GPU utilization by leveraging the Ray execution framework. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🎩

<<<<<<< HEAD
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

=======
<<<<<<< HEAD
<<<<<<< HEAD
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
.. include:: ../shared/designs/design6.rst
=======
Optimizations
=============

EvaDB optimizes the evaluation of user-defined functions in three manifolds.

1. Cache expensive function invocations and reuse their results in future invocations.
2. Cost-based predicate reordering to evaluate fast and selective predicate first.
3. Ray-based distributed inference. EvaDB not only parallelizes model inference to improve GPU utilization but also builds pipeline to parallelize CPU processing (i.e., loading and decoding data).
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉
>>>>>>> aed2d9cf (docs: updated outdated reference to SHOW UDF)
=======
These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

.. include:: ../shared/design6.rst
>>>>>>> df4d8a35 (docs: updates)
=======
.. include:: ../shared/designs/design6.rst
>>>>>>> e867f37e (docs: updated images)
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source

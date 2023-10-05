.. _optimizations:

<<<<<<< HEAD
EvaDB Optimizations 🛠️
======================

EvaDB optimizes the evaluation of *AI functions* using these optimizations:

1️⃣ *Function Result Caching*: EvaDB caches results of expensive function invocations during query processing. This accelerates subsequent queries over the same dataset. 📂

2️⃣ *Query Predicate Reordering*: Efficiency is key. EvaDB strategically reorders query predicates to prioritize evaluation of lower-cost and more selective predicates. 🔀

3️⃣ *Parallel Query Processing*: EvaDB runs AI models in parallel to optimize GPU utilization by leveraging the Ray execution framework. Additionally, an AI pipeline is established for concurrent CPU tasks, such as data loading and decoding. 🎩

These built-in optimizations ensure superior performance and responsiveness in EvaDB's AI function evaluations. Dive in and experience the EvaDB difference! 🌟🎉

.. include:: ../shared/designs/design6.rst
=======
Optimizations
=============

EvaDB optimizes the evaluation of AI functions using these optimizations:

1. EvaDB automatically caches the results of expensive function invocations while processing a query and reuses the results in future queries.
2. EvaDB reorder predicates based on cost to evaluate fast, more selective predicates earlier.
3. EvaDB runs AI models using the Ray framework in parallel to improve GPU utilization and sets up an AI pipeline to parallelize CPU processing (i.e., loading and decoding data).


<<<<<<< HEAD
1. Cache expensive function invocations and reuse their results in future invocations.
2. Cost-based predicate reordering to evaluate fast and selective predicate first.
3. Ray-based distributed inference. EvaDB not only parallelizes model inference to improve GPU utilization but also builds pipeline to parallelize CPU processing (i.e., loading and decoding data).
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
=======
>>>>>>> e1643547 (updates)

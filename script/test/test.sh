#!/bin/bash

##################################################
## FUNCTION START
##################################################

usage() {                                 # Function: Print a help message.
  echo "Usage: $0 [ -m MODE ]"  
}

exit_abnormal() {                         # Function: Exit with error.
  usage
  exit 1 # Failure
}

print_error_code() {
  code=$1
  info=$2
  if [ $code -ne 0 ];
  then
    echo "${info} CODE: --|${code}|-- FAILURE"
    exit $code
  else
    echo "${info} CODE: --|${code}|-- SUCCESS"
  fi
}

check_formatter() {
  sh script/formatting/pre-push.sh
  code=$?
  print_error_code $code "FORMATTER"
}

check_linter() {
  PYTHONPATH=./ python -m flake8 --config=.flake8 evadb/ test/ 
  code=$?
  print_error_code $code "LINTER"
}

check_doc_build() {
  pushd docs
  make html
  code=$?
  popd
  print_error_code $code "DOC BUILD"  
}

check_doc_link() {
  pushd docs
  make linkcheck
  code=$?
  popd
  print_error_code $code "DOC LINK CHECK"  
}

check_readme_link() {
  if command -v npm > /dev/null && command -v npx >/dev/null && npm list --depth=0 | grep markdown-link-check; then
    npx markdown-link-check -c ./script/test/link_check_config.json ./README.md 
    code=$?
    print_error_code $code "README LINK CHECK"
  else
    echo "README LINK CHECK: --||-- SKIPPED (missing dependency: npm install markdown-link-check)"		  
  fi
}

unit_test() {
  PYTHONPATH=./ pytest test/unit_tests/ --durations=20 --cov-report term-missing:skip-covered  --cov-config=.coveragerc --cov-context=test --cov=evadb/ --capture=sys --tb=short -v -rsf --log-level=WARNING -m "not benchmark"
  code=$?
  print_error_code $code "UNIT TEST"
}

short_integration_test() {
  PYTHONPATH=./ pytest test/integration_tests/short/ --durations=20 --cov-report term-missing:skip-covered  --cov-config=.coveragerc --cov-context=test --cov=evadb/ --capture=sys --tb=short -v -rsf --log-level=WARNING -m "not benchmark"
  code=$?
  print_error_code $code "SHORT INTEGRATION TEST"
}

short_third_party_test(){
  PYTHONPATH=./ python -m pytest -p no:cov test/third_party_tests/test_native_executor.py::NativeExecutorTest::test_should_run_query_in_sqlite -m "not benchmark" 
  code=$?
  print_error_code $code "SHORT THIRDPARTY TEST"
}

long_integration_test() {
  cache=$1
  if [[ "$cache" = "WITH_CACHE" ]];
  then
    PYTHONPATH=./ python -m pytest -ra --testmon-forceselect test/integration_tests/long/ -p no:cov -m "not benchmark"
  else
    PYTHONPATH=./ python -m pytest -ra --testmon-noselect test/integration_tests/long/ -p no:cov -m "not benchmark"
  fi
  code=$?
  print_error_code $code "LONG INTEGRATION TEST"
}

notebook_test() {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
<<<<<<< HEAD
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
=======
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb" --ignore="tutorials/19-employee-classification-prediction.ipynb"
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
>>>>>>> bf022329 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8a8a90aa (Add stable diffusion integration (#1240))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
>>>>>>> bf022329 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
=======
>>>>>>> eva-source
=======
>>>>>>> 2b924b76 (Add stable diffusion integration (#1240))
<<<<<<< HEAD
>>>>>>> 8a8a90aa (Add stable diffusion integration (#1240))
=======
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb" --ignore="tutorials/18-stable-diffusion.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
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
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
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
=======
>>>>>>> georgia-tech-db-main
=======
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
=======
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
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
  PYTHONPATH=./ python -m pytest --durations=5 --nbmake --overwrite "./tutorials" --capture=sys --tb=short -v --log-level=WARNING --nbmake-timeout=3000 --ignore="tutorials/08-chatgpt.ipynb" --ignore="tutorials/14-food-review-tone-analysis-and-response.ipynb" --ignore="tutorials/15-AI-powered-join.ipynb" --ignore="tutorials/16-homesale-forecasting.ipynb" --ignore="tutorials/17-home-rental-prediction.ipynb"
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
  code=$?
  print_error_code $code "NOTEBOOK TEST"
}

full_test() {
  PYTHONPATH=./ pytest test/ test/third_party_tests/test_native_executor.py::NativeExecutorTest::test_should_run_query_in_sqlite --durations=20 --cov-report term-missing:skip-covered  --cov-config=.coveragerc --cov-context=test --cov=evadb/ --capture=sys --tb=short -v -rsf --log-level=WARNING -m "not benchmark" --ignore=test/third_party_tests/ --ignore=test/app_tests/
  code=$?
  
  print_error_code $code "FULL TEST"
}

no_coverage_full_test() {
  PYTHONPATH=./ python -m pytest -p no:cov test/ test/third_party_tests/test_native_executor.py::NativeExecutorTest::test_should_run_query_in_sqlite -m "not benchmark" --ignore=test/third_party_tests/ --ignore=test/app_tests/
  code=$?
  print_error_code $code "FULL TEST"
}

##################################################
## FUNCTION END 
##################################################

MODE="FULL"

while getopts "m:" options; do            
  case "${options}" in                    # 
    m)                                    # If the option is m,
      MODE=${OPTARG}                      # set $MODE to specified value.
      ;;
    *)                                    # If unknown (any other) option:
      exit_abnormal                       # Exit abnormally.
      ;;
  esac
done

# This script should return a non-zero value if either
# linter fails or the pytest or the benchmark fails. 
# This is important for the CI system.

PYTHON_VERSION=`python -c 'import sys; version=sys.version_info[:3]; print("{0}.{1}".format(*version))'`

echo "OSTYPE: --|${OSTYPE}|--"
echo "PYTHON VERSION: --|${PYTHON_VERSION}|--"
echo "MODE: --|${MODE}|--"

##################################################
## LINTER TESTS
##################################################

if [[ ( "$OSTYPE" != "msys" ) && ( "$MODE" = "LINTER" || "$MODE" = "ALL" ) ]];
then 
  # Run black, isort, linter 
  check_formatter
fi

if [[ ( "$OSTYPE" != "msys" ) && ( "$MODE" = "LINTER" || "$MODE" = "ALL" ) ]];
then 
  # Keeping the duplicate linting for time being
  # Run linter (checks code style)
  check_linter
fi

##################################################
## DOC BUILD TESTS
##################################################

if [[ ( "$OSTYPE" != "msys" ) && ( "$MODE" = "DOC" || "$MODE" = "ALL" ) ]];
then 
  # Run black, isort, linter 
  check_doc_build
  check_doc_link
  check_readme_link
fi

##################################################
## UNIT TESTS
##################################################

if [[ "$MODE" = "UNIT" ]];
then 
  unit_test
fi

##################################################
## SHORT INTEGRATION TESTS
##################################################

if [[ "$MODE" = "SHORT INTEGRATION" ]];
then 
  short_integration_test
fi

##################################################
## SHORT THIRDPARTY TESTS
##################################################

if [[ "$MODE" = "SHORT THIRDPARTY TEST" ]];
then 
  short_third_party_test
fi

##################################################
## LONG INTEGRATION TESTS
##################################################

if [[ "$MODE" = "LONG INTEGRATION" ]];
then
  long_integration_test "WITHOUT_CACHE"
fi

if [[ "$MODE" = "LONG INTEGRATION CACHE" ]];
then
  long_integration_test "WITH_CACHE"
fi

##################################################
## FULL TESTS
## with cov pytest plugin
##################################################

if [[ "$MODE" = "FULL" ]];
then
    # Non-Windows
    if [[ "$OSTYPE" != "msys" ]];
    then
      full_test
    # Windows -- no need for coverage report
    else
      no_coverage_full_test
    fi
fi

##################################################
## JUPYTER NOTEBOOKS TESTS
## with nbmake pytest plugin
##################################################

if [[ "$MODE" = "NOTEBOOK" ]];
then 
  notebook_test
fi

##################################################
## UPLOAD COVERAGE
## based on Python version
##################################################

if [[ ( "$PYTHON_VERSION" = "3.10" ) ]]
then 
    echo "UPLOADING COVERAGE REPORT"
    coveralls
    exit 0 # Success     
fi

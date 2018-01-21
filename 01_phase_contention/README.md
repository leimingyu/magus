### test cases to evaluate NN for contention analysis
to verify the nn performance

* got to test_apps, run 01_compile_natively.sh
* generate metrics : 02_profile.sh
* generate traces : 05_genTrace.sh
* go to test_apps_ContentionTest/, generate contention tests by running ./01_genTests.py
* go to test_cases, run ./01_runAll
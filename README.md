# 🐍 PYTEST PLAYWRIGHT 🎭

## DONE IS BETTER THAN PERFECT FOR THIS CASE ! ##


## WHAT DOES THIS PROJECT DO
Simple, minimal complexity, scalable, and quick-to-develope, Functionsl, UI, E2E test scripts. With reporting, email, and basic (push & daily) CICD to github.


## TO SETUP
1) Install python3.exe x64-bit
2) At root project create new virtual env: python -m venv venv 
3) Start Python's virtual env: venv\Scripts\activate
4) python.exe -m pip install --upgrade pip
5) pip install -r requirements.txt (or manually install everything)
6) playwright install
7) to end venv environment: deactivate


## TO RUN TEST
1) pytest tests/regression/test_mnp_regression.py
2) pytest tests/e2e/test_npl_new.py


## PLAYWRIGHT CODE GENERATOR
1) playwright codegen https://{{url}}


## [PRIORITY 1] Require Immediate Attention:
1) Decide: Playwright test or Pytest format !
2) [CONFIG] A CI/CD in place
3) [FUNCTION] Scroll behavior: click and drag, example: start position 25%:25% end position 75%:75%
4) [FUNCTION] Screenshot, save, and auto-rename.
6) [CONFIG] level: page.wait_for_timeout() default to 2000 (milliseconds)
7) [CONFIG] level: scale browser window size to flexible
8) ✅[FUNCTION] Payment Method: FPX, Mastercard, Visa


## [PRIORITY 2] Non-Blockers, Fun To Explore
1) [CLI] python CLI & Args: python test.py test_name_example.py --data csvfile 
2) map or init all e2e test scripts
3) [FUNCTION] test result template
4) [FUNCTION] email test result
5) ✅[CONFIG] setup .env for: payment detail, personal email, password, URL?? etc


## Questions and Problems Faced
1) how to launch multiple test scripts/windows parrallelly on Python
2) playwright pytest configuration approach? at conftest? Which test framework to use?
3) scale playwright --headless=false to flexi, or 1/4 of window size
4) video evidence quality is SO BAD now.. can improve quality/size?


## TEST SCRIPTS, PRE-REQUISITE
1) Login negative scenairos for all modules. Format, eligibility, with the error message.
2) screenshot every test case result!
3) API are stable


## OFFICIAL DOCUMENTATIONS

- PEP 8 Official Guide https://peps.python.org/pep-0008/
- Python Documentation https://docs.python.org/3/tutorial/classes.html#private-variables 
- Playwright Documentation https://playwright.dev/python/docs/api/class-playwright

| Element	| Convention | Example |
|----------|----------|----------|
Script/Module names | snake_case | customer_api.py
Functions | snake_case | get_customer_data()
Variables | snake_case | customer_id
Classes | PascalCase | CustomerAPI
Constants | SCREAMING_SNAKE_CASE | MAX_RETRIES
Methods | snake_case | calculate_total()
Private variables | _snake_case	| _internal_data
Name-mangled variables | __snake_case | __private_data
Packages | lowercase | mypackage
Type variables | PascalCase	| T, ResponseType

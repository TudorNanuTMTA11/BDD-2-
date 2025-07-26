# Section 1: Packages to be installed

 ## Introduction

 BDD framework is linked with GHERKIN language. In Python, Gherkin is implemented with help of behave library.
 There are some browsers or drivers which are suported such as Firefox, Chrome and Edge .Furthermore, supported Python version is 3.12.

 ## Installation

 To install BDD framework, it has to be created a text file called behave.ini, where it is necessary to install Ini plugin which support .ini files. Package to be installed is behave-html-formatter. After that, it will be opened files which are renamed as .feature. Then it is installed Gherkin plugin which allows the files to become Cucumber files.

 ### Ini plugin

 Provides ".ini" files support. The following features are available:
Syntax highlighting, formatting, code folding, and viewing structure for .ini files
Detection of duplicate properties and sections
The ability to navigate to a property via the Go to Symbol action

### Behave-html-formatter package

It can be installed by using the command pip install behave-html-formatter or by install it from packages. Then, in behave.ini file write  the sequence [behave.formatters]
html=behave_html_formatter:HTMLFormatter

### Gherkin language
Adds support for the Gherkin language, which is used by the Cucumber testing tool.
Provides coding assistance for step definitions

## Selenium
For interaction with web elements it will be necessary installation of selenium library. This can be done by using the command pip install -U selenium.

## Driver
For interacting with the browser , Selenium needs a driver which will be instantiated through Driver class , available in seleniumbase library.

The driver will be specified through sending its name as argument of the Driver class constructor , if it is not specified it will be sent the name of the implicit browser from the system where the code is run. Seleniumbase library from where Driver class is imported can be installed by using the command pip install seleniumbase.

## Project cloning and running
For cloning we can use the command git clone TudorNanuTMTA11/BDD-2-

For executing the tests we can write in console behave -f html -o test-report.html for all tests or for a single test write behave -f html -o test-report.html followed by --tags=@T1 for example

# Section 2: Project structure
The project is composed of the following structure:

root named "BDD-2-

directory named "BDD-2-"

directory named "Features"

directory named "Pages"

directory named "Steps"

magento_home_page.feature.py -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for access website function

magento_create_account.feature.py -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for creating account

magento_checkout_feature.py -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for purchasing a product

magento_sign_in_page.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for sign in into the account

magento_sale.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for accessing the sale option of the website

magento_training.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for accessing the training option of the website

magento_circe_hooded_ice.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for buying a speciffic product

magento_hoodies_and_sweatshirts.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for sorting the products

magento_search.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for searching the products

magento_tops.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for accessing the tops option of the website

magento_what_is_new.feature -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for accessing the what is new option of the website


home_page.py -> contains methods and functions which are used for allowing the tests for accesing the website to work and a class 

which contains the speciffic selectors

create_account.py -> contains methods and functions which are used for allowing the tests for create account to work and a class which 

contains the speciffic selectors

what_is_new.py -> contains methods and functions which are used for allowing the tests for what is new to work and a class which 

contains the speciffic selectors

tops.py -> contains methods and functions which are used for allowing the tests for tops to work and a class which 

contains the speciffic selectors

checkout.py -> contains methods and functions which are used for allowing the tests for purchasing a product to work and a class which 

contains the speciffic selectors

sign_in_page.py -> contains methods and functions which are used for allowing the tests for sign in into account to work and a class which 

contains the speciffic selectors

hoodies_and_sweatshirts.py -> contains methods and functions which are used for allowing the tests for hoodies and sweatshirts to work and a class which 

contains the speciffic selectors

circe_hooded_ice.py -> contains methods and functions which are used for allowing the tests for circe hooded ice to work and a class which 

contains the speciffic selectors

search.py -> contains methods and functions which are used for allowing the tests for search product to work and a class which 

contains the speciffic selectors

training.py -> contains methods and functions which are used for allowing the tests for training to work and a class which 

contains the speciffic selectors

sale.py -> contains methods and functions which are used for allowing the tests for sale to work and a class which 

contains the speciffic selectors

home_page_steps.py -> contains the steps which are defined in features designed for accesing the website and then for generate the 

test report in html format

create_account_steps.py -> contains the steps which are defined in features designed for creating account and then for 

generate the test report in html format

sign_in_page_steps.py -> contains the steps which are defined in features designed for sign in and then for 

generate the test report in html format

sale_steps.py -> contains the steps which are defined in features designed for sale and then for 

generate the test report in html format

training_steps.py -> contains the steps which are defined in features designed for training and then for 

generate the test report in html format

search_steps.py -> contains the steps which are defined in features designed for search product and then for 

generate the test report in html format

circe_hooded_ice_steps.py -> contains the steps which are defined in features designed for circe hooded ice and then for 

generate the test report in html format

checkout_steps.py -> contains the steps which are defined in features designed for purchasing product and then for 

generate the test report in html format

what_is_new_steps.py -> contains the steps which are defined in features designed for what is new and then for 

generate the test report in html format

tops_steps.py -> contains the steps which are defined in features designed for tops and then for 

generate the test report in html format

hoodies_and_sweatshirta_steps.py -> contains the steps which are defined in features designed for hoodies and sweatshirts and then for 

generate the test report in html format

behave.ini -> file for enabling Ini plugin

browser.py -> file for accessing the browser

environment.py -> file for designing the framework

test-report.html -> file for accesing the report in browser

# Section 3 : Automation testing project objectives
Automation testing project has as foundation the site "https://magento.softwaretestingboard.com/", with the logo "Luma".

The objectives are testing the login functionality which is performed with the help of positive testing, negative testing and functional 

testing.

Furthermore, testing of the inventory functionality, was done through positive testing, negative testing and functional testing.

Also, the purpose of the project was creating .py files and generating a html-type execution report, with the scope of presenting and 

interpreting the results.

# Section 4 : Deadlines
The accepted deadline for finalising all the testing for the website in scope was 15.09.2024. Until then, all testing must be performed, 

all reports must be generated. The scope of this project was purely an automation one, and no defect management activities were done. 

For defect identification I created a separate manual testing project which covers this type of testing activities.

# Section 5: Description of the tests that were performed + testing types and techniques used

All the tests that were performed that were created in the unittest framework using positive testing, negative testing and functional 

testing.

Majority of the the tests that were created were passed during the test execution phase, one failed on purpose.

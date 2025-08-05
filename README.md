# Section 1: Packages to be installed

 ## Introduction

 BDD framework is linked with GHERKIN language. In Python, Gherkin is implemented with help of behave library.
 There are some browsers or drivers which are suported such as Firefox, Chrome and Edge .Furthermore, supported Python version is 3.12.

 ## Installation

In order <b>to format the test report file</b>, we need to <b>install behave-html-formatter package</b>. Also, in order <b>to beautify the format option in the run command</b>, we need to <b>install the .ini package</b> and <b>create a file</b> called <b>behave.ini</b>. <b>The content of the file must be the following: </b>
Provides ".ini" files support. The following features are available:
 <ul>
<li>Syntax highlighting, formatting, code folding, and viewing structure for .ini files  </li>
<li>Detection of duplicate properties and sections </li>
<li> The ability to navigate to a property via the Go to Symbol action </li>
</ul>

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

<ul>
<li>root named "BDD-2-</li>
<li>directory named "BDD-2-"</li>
<li>directory named "Features"</li>
<li>directory named "Pages"</li>
<li>directory named "Steps"</li>
<li><b>magento_home_page.feature.py </b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, thenfor access website function</li></i>
<li><b>magento_create_account.feature.py</b> -> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for creating account</li></i>
<li><b>magento_checkout_feature.py </b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for purchasing a product</li></i>
<li><b>magento_sign_in_page.feature </b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for sign in into the account</li></i>
<li><b>magento_sale.feature </b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for accessing the sale option of the website</li></i>
<li><b>magento_training.feature</b> -> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for accessing the training option of the website</li></i>
<li><b>magento_circe_hooded_ice.feature</b> -> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for buying a speciffic product</li></i>
<li><b>magento_hoodies_and_sweatshirts.feature</b> -> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for sorting the products</li></i>
<li><b>magento_search.feature</b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for searching the products</li></i>
<li><b>magento_tops.feature</b> -> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for accessing the tops option of the website</li></i>
<li><b>magento_what_is_new.feature</b>-> <i>test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then for accessing the what is new option of the website</li></i>
<li><b>home_page.py</b> -> <i>contains methods and functions which are used for allowing the tests for accesing the website to work and a class which contains the speciffic selectors</li></i>
<li><b>create_account.py</b> -> <i>contains methods and functions which are used for allowing the tests for create account to work and a class which contains the speciffic selectors</li></i>
<li><b>what_is_new.py</b> -> <i>contains methods and functions which are used for allowing the tests for what is new to work and a class which contains the speciffic selectors</li></i>
<li><b>tops.py</b> -> <i>contains methods and functions which are used for allowing the tests for tops to work and a class which 
contains the speciffic selectors</li></i>
<li><b>checkout.py</b> -> <i>contains methods and functions which are used for allowing the tests for purchasing a product to work and a class which contains the speciffic selectors</li></i>
<li><b>sign_in_page.py</b> -> <i>contains methods and functions which are used for allowing the tests for sign in into account to work and a class which contains the speciffic selectors</li></i>
<li><b>lhoodies_and_sweatshirts.py</b> -> <i>contains methods and functions which are used for allowing the tests for hoodies and sweatshirts to work and a class which contains the speciffic selectors</li></i>
<li><b>circe_hooded_ice.py</b> -> <i>contains methods and functions which are used for allowing the tests for circe hooded ice to work and a class which contains the speciffic selectors</li></i>
<li><b>search.py</b> -> <i>contains methods and functions which are used for allowing the tests for search product to work and a class which contains the speciffic selectors</li></i>
<li><b>training.py</b> -> <i>contains methods and functions which are used for allowing the tests for training to work and a class which 
contains the speciffic selectors</li></i>
<li><b>sale.py </b>-> <i>contains methods and functions which are used for allowing the tests for sale to work and a class which 
contains the speciffic selectorst</li></i>
<li><b>home_page_steps.py</b> -> <i>contains the steps which are defined in features designed for accesing the website and then for generate the test report in html format</li></i>
<li><b>create_account_steps.py </b>-> <i>contains the steps which are defined in features designed for creating account and then for 
generate the test report in html format</li></i>
<li><b>sign_in_page_steps.py</b> -><i> contains the steps which are defined in features designed for sign in and then for 
generate the test report in html format</li></i>
<li><b>sale_steps.py </b>-> <i>contains the steps which are defined in features designed for sale and then for 
generate the test report in html format</li></i>
<li><b>training_steps.py</b> -> <i>contains the steps which are defined in features designed for training and then for 
generate the test report in html format</li></i>
<li><b>search_steps.py </b>-> <i>contains the steps which are defined in features designed for search product and then for 
generate the test report in html format</li></i>
<li><b>circe_hooded_ice_steps.py</b> -> <i>contains the steps which are defined in features designed for circe hooded ice and then for 
generate the test report in html format</li></i>
<li><b>checkout_steps.py</b> -> <i>contains the steps which are defined in features designed for purchasing product and then for 
generate the test report in html format</li></i>
<li><b>what_is_new_steps.py</b> -> <i>contains the steps which are defined in features designed for what is new and then for 
generate the test report in html format</li></i>
<li><b>tops_steps.py</b> -> <i>contains the steps which are defined in features designed for tops and then for 
generate the test report in html format</li></i>
<li><b>hoodies_and_sweatshirta_steps.py</b> -> <i>contains the steps which are defined in features designed for hoodies and sweatshirts and then for generate the test report in html format</li></i>
<li><b>behave.ini </b>-> <i>file for enabling Ini plugin</li></i>
<li><b>browser.py </b>-> <i>file for accessing the browser</li></i>
<li><b>environment.py </b>-> <i>file for designing the framework</li></i>
<li><b>test-report.html </b>-> <i>file for accesing the report in browser</li></i>
</ul>

# Section 3 : Automation testing project objectives
Automation testing project has as foundation the site "https://magento.softwaretestingboard.com/", with the logo "Luma".
The objectives are testing the login functionality which is performed with the help of positive testing, negative testing and functional 
testing.Furthermore, testing of the inventory functionality, was done through positive testing, negative testing and functional testing.
Also, the purpose of the project was creating .py files and generating a html-type execution report, with the scope of presenting and 
interpreting the results.

# Section 4 : Deadlines
The accepted deadline for finalising all the testing for the website in scope was 15.09.2024. Until then, all testing must be performed, 
all reports must be generated. The scope of this project was purely an automation one, and no defect management activities were done. 
For defect identification I created a separate manual testing project which covers this type of testing activities.

# Section 5: Description of the tests that were performed + testing types and techniques used
<img width="1366" height="768" alt="Captură ecran (462)" src="https://github.com/user-attachments/assets/e2024a9a-6e02-4d86-99e3-75adf61e8d53" /><img width="1366" height="768" alt="Captură ecran (467)" src="https://github.com/user-attachments/assets/1f878145-3ef5-454d-82ba-57c7f20b75ef" />


All the tests that were performed that were created in the unittest framework using positive testing, negative testing and functional 
testing.[Uploading test-report.html…]()


Majority of the the tests that were created were passed during the test execution phase, one failed on purpose.

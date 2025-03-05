# Requirements

<!-- markdownlint-disable MD013 --><!-- Tables cannot be split up over lines, hence will break 80 characters per line -->

Requirement ID|Requirement description     |Acceptance criteria   |Test cases
--------------|----------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------
R1            |Read data                   |Passes the test case  |The `.csv` file is parsed correctly by a function called `read_data`
R1.1          |Read file                   |Passes the test case  |The content of the file can be read without errors
R1.2          |Data column names           |Passes the test case  |The column names must match between file and the table that is created by reading the file
R1.3          |Data content                |Passes the test case  |The column names must match between file and the table that is created by reading the file
.             |.                           |Passes the test case  |The content of the first row of the table created by loading the file, matches exactly the content of the first row in the file
R1.4          |Read data fast              |Passes the test case  |The file is read within 1 second
R1.5          |Read absent file            |Passes the test case  |If the file cannot be found, create a helpful error message, that includes the path of the absent file
R1.6          |Documented column names     |Passes the test case  |The documentation contains the names of the columns
.             |.                           |One human agrees      |The documentation describes the content of the columns
R100          |Best practices              |All team members agree|We think we follow the best practices as found in the academic literature
R100.1        |Best practices are discussed|All team members agree|If the team agrees a practice found in the academic literature to be best, it is discussed
R100.2        |Democratic decision making  |All team members agree|If there are candidate better practices, these are voted for/against
R100.2        |Democratic adoption         |All team members agree|If a majority vote favors a practice, we adopt it
    
<!-- markdownlint-enable MD013 -->


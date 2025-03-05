# Requirements

<!-- markdownlint-disable MD013 --><!-- Tables cannot be split up over lines, hence will break 80 characters per line -->

Requirement ID|Requirement description|Acceptance criteria |Test cases
R1            |Read data              |Passes the test case|The file is parsed correctly
R1.1          |Read file              |Passes the test case|The content of the file can be read without errors
R1.2          |Data column names      |Passes the test case|The column names must match between file and the table that is created by reading the file
R1.3          |Data content           |Passes the test case|The column names must match between file and the table that is created by reading the file
.             |.                      |.                   |The content of the first row of the table created by loading the file, matches exactly the content of the first row in the file
R1.4          |Read data fast         |Passes the test case|The file is read within 1 second
R1.5          |Read absent file       |Passes the test case|If the file cannot be found, create a helpful error message, that includes the path of the absent file
R1.6          |Documented column names|Passes the test case|The documentation contains the names of the columns
.             |.                      |One human agrees    |The documentation describes the content of the columns
    
<!-- markdownlint-enable MD013 -->


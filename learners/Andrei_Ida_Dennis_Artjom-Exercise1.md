Task: Do some analysis on data from an Uppsala weather station.


You have a temperature data file (Uppsala)
Build a program that performs and presents some analysis
graph of running means
other statistics
daily maximums/min
yearly maximums/min
meta data extraction
name of station
dates , times and variable from which column
presentation
header of graphs (name)
axis labels
When the program is run, user should be able to decide which analysis to perform, for instance with arguments from the commandline.
Make sure to that it can load other data.

User needs
    User input
        Select data to analyse

    Graphs
        Running means
    Stats
        Daily maximums/min
        Yearly maximums/min
    Meta data extraction
            name of station
            dates , times and variable from which column
    Presentation
        

| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases |
| -------- | ------- | ------- | ------- |
| R1 | User input | User can specify which analysis to run on the command line | Verify that the selected analysis runs |
| R2 | User input | User can select temperature data file on which to work on | Confirm that selected data is loaded correctly |
| R3 | Runnings means graph | An image file is created | Confirm that non-empty image file is created |
| R4 | Daily maximums and minimums | Print daily maximums and minimums | Confirm no extreme or empty values |
| R5 | Yearly maximums and minimums | Print yearly maximums and minimums | Confirm no extreme or empty values |
| R6 | Extract name of station | Print name of station | Confirm 


Risk assessment

Hazards
R1  1 Performed analysis does not match user choice
    2 User mixes up analysis choice due to lack of userfriendliness
    3 User provides wrong input format
R2  
R3  
R4  
R...

Probability
R1.1 | P1 | S3 | 3 |
R1.2 | P4 | S3 | 12 |
R1.3 | P4 | S4 | 16 |

Severity
R1.1    S3
R1.2    S3
R1.3    S4

Risk
R1.1    3
R1.2    12
R1.3    16
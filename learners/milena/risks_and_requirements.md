# Risks and requirements group 1: Milena, Artur and Xiuqi

# Requirements

1. 
    Description: Loading data
    Acceptance criteria: Data is loaded without errors
    Test case: check for expected data type, file size ...

    Risk: Malware
    Probability: low (1/5)
    Severity: medium (3/5)
    P*S = 3

    Risk: corrupted data 
    Probability: medium (2/5)
    Severity: low (1/5)
    P*S = 2

    Risk: Large files, difficulty handling input data
    Probability: medium (3/5)
    Severity: high (3/5)
    P*S = 9

2. 
    Description: Running means, daily/yearly maximum and minimum, metadata extraction
    Acceptance criteria: Correct computation, handle missing data and outliers
    Test case: Make simulated dataset where you know the values

    Risk: Mistakes resulting in wrong output values
    Probability: low (1/5)
    Severity: high (4/5) (this would likely result in problems for requirement 3)
    P*S = 4

3. 
    Description: Computing statistics, is there a difference in the increase in temperature between measurement stations or corrected vs. uncorrected data? Let user choose with argparse
    Acceptance criteria: Correct computation, understandable results presentation
    Test case: make test dataset and test cases on real data.

    Risk: Mistakes in the code
    Probability: low (1/5)
    Severity: medium (2/5)
    P*S = 2

    Risk: User makes bad request
    Probability: medium(2/5)
    Severity: low (1/5)
    P*S = 2

4. 
    Description: Visualization
    Acceptance criteria: readable and useable plot for user with all essential information, dynamic adjustment depending on data content.
    Test case: make test cases on real data

    Risk: Unusable figures if user picks extreme data source
    Probability: medium (2/5)
    Severity: medium (2/5)
    P*S = 4

    Risk: Mistakes, figure contradicts statistics
    Probability: low (1/5)
    Severity: low (1/5)
    P*S = 1
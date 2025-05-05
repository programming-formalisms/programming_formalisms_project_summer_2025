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
    Test case: Make dummy dataset where you know the values

    Risk: Mistakes resulting in wrong output values
    Probability: low (1/5)
    Severity: high (4/5) (this would likely result in problems for requirement 3)
    P*S = 4

3. 
    Description: Computing statistics
    Acceptance criteria:
    Test case:

    Risk:
    Probability:
    Severity:
    P*S = 

4. 
    Description: Visualization
    Acceptance criteria:
    Test case:

    Risk:
    Probability:
    Severity:
    P*S = 
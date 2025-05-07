# Risks and requirements

| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases |
| -------- | ------- | ------- | ------- |
| R1 | Read data | 
| R1.1 | Let user select data | 
| R2 | Running means, daily/yearly maximum and minimum, metadata extraction | Correct computation, handle missing data and outliers | Make dummy dataset where you know the values
| R3 | Computing statistics | 
| R4 | Visualisation | 
| R4.1 | User input | User can specify which analysis to run on the command line | Verify that the selected analysis runs |
| R4.2 | Runnings means graph | An image file is created | Confirm that non-empty image file is created |
| R4.3 | Daily maximums and minimums | Print daily maximums and minimums | Confirm no extreme or empty values |
| R4.4 | Yearly maximums and minimums | Print yearly maximums and minimums | Confirm no extreme or empty values |
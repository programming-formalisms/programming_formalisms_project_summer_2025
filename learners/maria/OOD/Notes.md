# code-along with Lars on Mermaid
classDiagram
direction TB
    class Uppsala_Weather_Station {
	    - TemperatureData
	    + GenerateReport()
    }

    class Temperature_Graph {
    }

    class Thermometer {
	    -Temperature
    }

    Uppsala_Weather_Station --> Temperature_Graph : data
    Uppsala_Weather_Station "1" *-- "1..*" Thermometer : has a number of


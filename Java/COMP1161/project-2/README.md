# COMP1161 Project 2

Project 2 implements a bus planning system with bus types, trips, plans, planners, ministry information, interactive screens, and case-based testing.

## Runtime Shape

~~~text
Driver.java
    |
    +--> EntryScreen and ReportScreen
    +--> Planner, Plan, Trip, and Bus models
    +--> id.txt and SysInfo.txt
    +--> cases/
~~~

The driver reads `id.txt` and uses the configured case and documentation paths through `SystemInfo`. Run it from this folder.

## Build and Run

~~~bash
javac *.java
java Driver
~~~

The `cases/` directory stores input cases and expected outputs. The `doc/` directory stores generated Javadocs. Open `doc/index.html` in a browser to browse the API documentation.

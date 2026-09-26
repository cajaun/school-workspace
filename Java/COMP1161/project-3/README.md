# COMP1161 Project 3

Marked is a desktop student grade management application. It adds students, displays student records, edits grades, recalculates GPA values, and visualizes a student’s course grades.

## Runtime Shape

~~~text
ui/ -> screens and navigation
models/ -> students, grades, and GPA calculations
util/ -> loading, validation, fonts, and UI helpers
data/ -> course codes and student records
assets/ -> logo and application fonts
lib/ -> packaged runtime libraries
~~~

The source uses Swing and the libraries stored under `lib/`. The packaged `comp1161-final-project.jar` is the runnable artifact. Run it from this folder so the relative `assets/` and `data/` paths resolve:

~~~bash
java -jar comp1161-final-project.jar
~~~

The original project guide is [READ ME.txt](<READ ME.txt>). It documents the user flows and the JSON files used by the application.

## Source Areas

| Folder | Responsibility |
| --- | --- |
| `models/` | Student, grade, and GPA data |
| `ui/` | Welcome screen, menus, panels, and Swing components |
| `util/` | Course loading, validation, fonts, and shared helpers |
| `config/` | Application constants |
| `data/` | JSON input and persisted student records |
| `assets/` | Logo and fonts |
| `lib/` | FlatLaf, Gson, JSON, and XChart libraries |

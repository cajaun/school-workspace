# School Workspace

This workspace organizes coursework from Cajaun Campbell’s computer science studies at The University of the West Indies. The source is grouped by language, course, project, lab, and examination material.

## Documentation

The [documentation index](docs/README.md) owns the detailed material. Each major area keeps its build commands, file map, and usage notes in its local README.

| Area | Start here |
| --- | --- |
| C coursework | [C index](C/README.md) |
| HTML coursework | [HTML index](Html/README.md) |
| Java coursework | [Java index](Java/README.md) |
| Python coursework | [Python index](Python/README.md) |
| Documentation rules | [Documentation index](docs/README.md) |

## Workspace Shape

~~~text
Client or terminal
        |
        v
Course folder -> source files -> language toolchain -> local output
        |
        +--> C and COMP3101 Makefiles
        +--> Java and COMP1161 project folders
        +--> Python course scripts
        +--> HTML, CSS, JavaScript, and image assets
~~~

The workspace has no root-level build command. Each course uses its own source layout, compiler, runtime, test data, and generated output.

## Local Development

Build or run work from the folder that owns it:

~~~bash
# c
cd C/COMP3101/assignment-1
make
./myshell

# java
cd Java/COMP1161/project-1
javac *.java
java Driver

# python
python3 Python/COMP1126/week-3/tutorial/test.py

# web
python3 -m http.server 8000 --directory Html/COMP1220
~~~

The local README beside a project takes precedence over these general commands when it defines extra data, libraries, or working-directory requirements.

## Tests and Quality

The C Makefiles compile with C11 and enable `-Wall`, `-Wextra`, and `-Wpedantic`. Java and Python work use folder-level compilation or direct script execution. The static site uses a local HTTP server for browser checks.

There is no shared test runner for the complete workspace. Run the checks documented by the README in the folder under review.

## Repository Layout

~~~text
C/          COMP3101 process and shell work
Html/       COMP1220 static web work
Java/       COMP1161 object-oriented programming work
Python/     COMP1126, COMP1127, COMP2190, and COMP2211 work
docs/       documentation index and repository guidance
~~~

Some coursework folders preserve compiled files, archives, generated documentation, test fixtures, packaged applications, and copied submission files. The local README identifies those artifacts and explains which files belong to the runnable source.

Generated cache directories such as `__pycache__` do not own source workflows. Their parent README documents the source that produced them.

## Documentation Rules

Keep commands in the README that owns the relevant workflow. Link to that page when another README needs the same command or policy. Keep descriptions tied to files that exist in the folder.

## Academic Use

This workspace stores academic coursework and study material. Ask the author before redistributing its source code or submitted work.

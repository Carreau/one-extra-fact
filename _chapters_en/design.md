---
permalink: "/en/design/"
title: "Course Design"
---

This design template is taken from *[Teaching Tech Together][t3]* [[Wils2018](#CITE)].
The first section explains who this course is for,
while the second sketches its scope.
Sections 3 and 4 then lay out what learners will do in what order,
and the final section is the course's public face.
See `misc/course-outline.md` for material that was designed
but *isn't* being included in the course.

<!-- -------------------------------------------------------------------------------- -->

## Step 1: Who is this course for?

### Bhadra

Bhadra received a B.Sc. in biochemistry five years ago, and has worked
since then for a small biotech firm.  She did a biostatistics course
using R as a senior, but has no other training in programming.

Bhadra is developing pattern-matching algorithms for gene expression.
Every morning, Bhadra manually runs any queries her colleagues have
emailed her and emails the results back.  Once a month she manually
re-analyzes the input and output files she has saved to look for new
patterns.

This course will teach Bhadra how to automate her daily and monthly
tasks, how to write regression tests for her software so that
additions and changes don't break existing features, and how to
package her software so that her colleagues can install it and run it
themselves.

### Jorge

Jorge just moved from Costa Rica to Canada to study agricultural
economics.  Other than using Excel, Word, and the Internet, Jorge's
most significant previous experience with computers is helping his
sister build a WordPress site for the family business back home in
Costa Rica.

Jorge needs to find, clean, integrate, and analyze data from land use
registries, labor statistics, commodity prices, and weather records.
He has inherited a handful of spreadsheets and programs written by
previous members of his lab to handle each of these separately, but
does not know whether he has the most up-to-date version of each, or
even precisely what kind of filtering and analysis each does.

This course will teach Jorge how to manage the code and data used in a
small research software project, how to fetch and process text, CSV,
and JSON data, and how to create simple exploratory visualizations.

### Mei

Mei is a graduate student in chemistry. Her only programming
experience is a general first-year introduction to computational
science using Python.

Mei is studying the carcinogenic effects of fullerenes. A typical
experiment involves testing each sample on four hundred slightly
different gels.  Using a machine borrowed from a collaborating lab,
she can prepare all the gels at once, but must manually edit and
upload a parameter file to the machine to do this.  She must then
download the results, add them to the steadily-growing archive, and
re-analyze the data.  The archive is now half a terabyte in size,
and analysis takes roughly 14 hours on a high-end desktop computer.

Over time, Mei has become more interested in the statistics she is
doing than in the underlying chemistry, and has decided that once she
completes her PhD, she would like to become a data scientist.  This
course will introduce her to tools and methods that will help her
finish her degree faster, and prepare her to work with much larger
data using more complicated statistical methods.

<!-- -------------------------------------------------------------------------------- -->

## Step 2: Brainstorming

1.  What questions will this course answer?
    -   How can I manage data, code, and reports?
    -   How can I build software faster?
    -   How can I tell if my software is correct?
    -   How can I make my work reproducible?
    -   How can I share data and software with others?
1.  What concepts and techniques will learners meet?
    -   Organize and manipulate tabular data in a spreadsheet.
    -   Manage and process files with the Unix shell.
    -   Process tabular data in Python.
    -   Program iteratively and defensively.
    -   Embed documentation in code.
    -   Name and organize the files in a project systematically.
    -   Track work with Git using a branching workflow.
    -   Share work with GitHub using pull requests.
    -   Make work reproducible using Make.
    -   Write tests with PyTest.
    -   Install packages with Pip.
    -   Do numerical computing with NumPy.
    -   Do statistics with Pandas.
    -   Process text with regular expressions.
    -   Create and publish a static website using GitHub Pages.
    -   Use ORCIDs and DOIs to identify authors, reports, and data.
1.  What technologies, packages, or functions will learners use?
    -   Spreadsheets: same topics as the [Data Carpentry lesson][dc-sheets] using Google Sheets.
    -   Unix shell: same topics as the [Software Carpentry lesson][swc-shell],
        with some [extra material][swc-shell-extra] on permissions.
    -   Python, NumPy, and Pandas: same topics as the [revised Software Carpentry lesson][swc-python],
        with extra material on writing command-line utilities.
    -   Pytest: new material.
    -   Git and GitHub: same topics as the [Software Carpentry lesson][swc-git] (split into separate lessons on tracking and collaborating).
    -   Publishing: new material on [Markdown][markdown] and [GitHub Pages][github-pages].
1.  What concepts will be introduced?
    -   Tidy data.
    -   Pipe and filter model.
    -   Version control repository.
    -   Embedded documentation for software.
    -   Key/value data.
    -   Program decomposition and iterative development.
    -   Commit.
    -   Merge and merge conflict.
    -   Pull request.
    -   Unit testing.
    -   Publication via text processing (rather than by using WYSIWYG tools).
1.  What misconceptions are expected?
    -   Why would I use the shell instead of Python? (duplication of utility between tools)
    -   How come I can't open my data files? (Path issues when using GUI tools)
    -   What the hell is a "detached HEAD"? (and other Git weirdness)
    -   What are all these curly braces for? (indexing by name in dictionaries, JSON, etc.)
    -   How can two different variables have the same name? (variable scope)
1.  What *won't* be covered?
    -   Package management: out of scope.
    -   Writing queries for relational or non-relational databases:
        feedback is that most data scientists don't do this (they consume data other people have produced).
    -   Connecting to remote computers using SSH:
        no time.
    -   Parallelizing map-reduce problem using GNU Parallel:
        too advanced.
    -   Serving data:
        all we could do in a short lesson is show people how to create security holes.
    -   Higher-order functions and object-oriented programming:
        there isn't time.
    -   LaTeX:
        [Markdown][markdown] plus [Pelican][pelican] are much simpler, and let us teach the same concepts (compiled, reproducible documents).
        -   We use [Pelican][pelican] rather than [Jekyll][jekyll] because it's Python-based (we can build into `./docs` for publication).
        -   And because it parallels the R course using [R Markdown][r-markdown].
    -   Conditionals and functions in the shell:
        learners will use Python for anything that complex.
    -   Docker:
        too advanced for the intended audience.
    -   GIS:
        not universally applicable.
    -   Image processing:
        ditto.
    -   Interactive web pages:
        there isn't time to teach JavaScript (or even something like Altair).
    -   Numerical or statistical methods:
        lots of high-quality courses already cover these topics.
    -   High-performance computing:
        high throughput is more widely useful.
    -   Symbolic debuggers:
        awkward to use through the Jupyter Notebook, but will probably be included in the RStudio version of the course.

<!-- -------------------------------------------------------------------------------- -->

## Step 3: What mental models will learners form?

These concept maps were drawn with the desktop edition of [draw.io][draw-io].
To modify them, edit the XML, then select all and export as SVG
using "selection only" and "transparent background".

<figure>
  <figcaption>Variables and Values</figcaption>
  <img id="f:variables-values" src="../../files/design/variables-values.svg" alt="Variables and Values" />
</figure>

<figure>
  <figcaption>Programs</figcaption>
  <img id="f:programs" src="../../files/design/programs.svg" alt="Programs" />
</figure>

<figure>
  <figcaption>Projects</figcaption>
  <img id="f:projects" src="../../files/design/projects.svg" alt="Projects" />
</figure>

<!-- -------------------------------------------------------------------------------- -->

## Step 4: What will learners do along the way?

*Another dozen exercise ideas will be added to this list before course
development starts, and all of them expanded to full text with
accompanying solutions to show how far learners will get by the end of
each lesson.*

### Reorganize Messy Data

The spreadsheet `scores.ods` contains scores for three cohorts of
undergraduate students who have been taught using different
techniques.  Reorganize this data into a single tidy sheet with:

-   variables in columns
-   observations in rows sorted by subject, property, and date (in that order)
-   a single value per cell
-   column headers that include the variable's name and units
-   empty cells for missing values
-   uniformly-formatted dates
-   a lookup table for categories based on performance

Export the tidy data as a CSV file and compare it to
`scores-solution.csv`.  Where does your interpretation of "tidy"
differ from the sample solution's?  Are any of these differences
important?

### Index a Dataset

The folder `scores` contains several dozen tidy datasets, each
formatted as a CSV file.  Each file has a column titled `person`
containing a randomly-generated ID that identifies a study subject.
Write a Python program that reads these files and produces an index
recording which subjects appear in which datasets:

-   The program should be called `person-file-index.py`.
-   It takes two arguments, both optional:
    -   The path to the folder containing the data files (default `.`).
    -   The name of the output file (if none is given, the program
        writes the index to standard output).
-   If any CSV file in the specified folder does *not* have a single
    column titled `person`, the program prints an error message to
    standard error and exits without creating an output file or
    printing anything to standard output.
-   The output must have exactly two columns titled `person` and `filename`.
    -   Each (`person`, `filename`) pair must be unique.
    -   The `person` value must be a string, even if the ID read from
        the input was all digits.
    -   The `filename` value contain only the filename (not any folder
        names).

### Reorganize a Small Project

The folder `thesis` contains shell scripts, Python programs, data
collected directly from laboratory equipment (as CSV files) and
several plots generated from that data.  Reorganize that material so
that it conforms to [Noble's Rules][noble].

### Clean up a set of inconsistently-formatted text data files using regular expressions.

### Fetch data from a website using a REST API.

### Merge changes from a remote repository when there are conflicts.

### Write a program to pass a set of pre-written tests.

### Publish a single-page website for a project on GitHub.

<!-- -------------------------------------------------------------------------------- -->

## Step 5: How are the concepts connected?

The initial outline in `misc/course-outline.md`
is structured in hour-long blocks with three topics per hour.
That works out to only 15 minutes per topic,
since academic "hours" are only 50 minutes long,
and it always takes a few minutes to get started.
However,
we expect that learners will read the questions and answers before class,
then spend their in-time class working on self-paced exercises
with tutors and peers available to help them when they get stuck.

This outline is inspired by the "minimal manual" approach to instructional design [[Carr2014](#CITE)]:

1.  All learning tasks should be meaningful and self-contained activities.
1.  Learners should be given realistic projects as quickly as possible.
1.  Instruction should permit self-directed reasoning and improvising
    by increasing the number of active learning activities.
1.  Training materials and activities should provide for error recognition and recovery.
1.  There should be a close linkage between the training and actual system.

The chapters now contain roughly 2/3 of what was in the original proposal.

<!-- -------------------------------------------------------------------------------- -->

## Step 6: Course overview

### Course Description

This course is an introduction to research computing and data analysis
for people with little or no previous training in either.
It can be used for self-study by people who are thinking about becoming data scientists
either as the core of a one-semester for graduate or undergraduate course.

### Prerequisites

Learners will need:

-   A personal computer with Internet access.
-   The Unix shell.
-   Python 3 (including the Jupyter Notebook).
-   Google Docs and GitHub accounts.

### Other Resources

-   [Software Carpentry][swc]
-   [Data Carpentry][dc]
-   [Data Carpentry for Biologists][dcb]
-   [Learn the tidyverse][tidyverse]
-   [[Wils2014](#CITE)]
-   [[Wils2017](#CITE)]
-   [[Tasc2017](#CITE)]
-   [Building a Research Software Commons][brsc]

{% include links.md %}

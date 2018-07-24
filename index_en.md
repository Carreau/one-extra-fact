---
layout: default
language: "en"
permalink: "/en/"
root: true
redirect_from: "/"
---
This course is an introduction to research computing and data analysis
for people with little or no previous training in either.
It can be used either as the core of a one-semester course for graduate students or senior undergraduates,
or for self-study by people who plan to enroll in a program like
the [Insight Data Science][insight] Fellows Program.
The course and related software freely available under [an open licence](./license/),
and can be viewed on [the course's website]({{site.website}}).

This course assumes 30 contact hours
(i.e., 3 hours/week for 12 weeks minus time for guest speakers, exam prep, and so on).
The pace is based on what [Software Carpentry][swc] and [Data Carpentry][dc] routinely achieve in their two-day workshops,
and on the University of Florida's experience with [Data Carpentry for Biologists][dcb].

Questions, suggestions, and corrections are very welcome:
please [file an issue]({{site.repo}}/issues)
in the course's [GitHub repository]({{site.repo}})
or [email the author directly](mailto:{{site.email}}).
Please note that all contributors are required to abide by
[our code of conduct](./conduct/).

This course is inspired by:

- [Software Carpentry][swc], [Data Carpentry][dc], and [Library Carpentry][lc]
- [Data Carpentry for Biologists][dcb]
- "[Best Practices for Scientific Computing][best]"
- "[Good Enough Practices in Scientific Computing][good]"
- "[Ten Simple Rules for Making Research Software More Robust][robust]"
- [Managing Research Software Projects][mrsp]

Please see the course design notes below for an overview of current thinking,

----

## Design

This design template is taken from *[Teaching Tech Together][t3]*.
The first section explains who this course is for,
while the second sketches its scope.
Sections 3 and 4 then lay out what learners will do in what order,
and the final section is the course's public face.

This course's primary tools are Google Sheets, Unix, Python, and the Jupyter Notebook.
Parallel material using Excel, Windows, R, and RStudio will be designed separately.

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
and JSON data, how to write basic SQL queries to get data from
databases, and how to create simple exploratory visualizations.

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

1. What questions will this course answer?
   1. How can I manage data, code, and reports?
   1. How can I build software faster?
   1. How can I tell if my software is correct?
   1. How can I make my work reproducible?
   1. How can I share data and software with others?
1. What concepts and techniques will learners meet?
   1. Organize and manipulate tabular data in a spreadsheet.
   1. Manage and process files with the Unix shell.
   1. Process tabular data in Python.
   1. Program iteratively and defensively.
   1. Embed documentation in code.
   1. Name and organize the files in a project systematically.
   1. Track work with Git using a branching workflow.
   1. Share work with GitHub using pull requests.
   1. Make work reproducible using Make.
   1. Write tests with PyTest.
   1. Install packages with Pip.
   1. Do numerical computing with NumPy.
   1. Do statistics with Pandas.
   1. Visualize data with Altair.
   1. Process text with regular expressions.
   1. Write queries in SQL.
   1. Fetch remote data using Requests.
   1. Create and publish a static website using GitHub.
   1. Use ORCIDs and DOIs to identify authors, reports, and data.
1. What technologies, packages, or functions will learners use?
   1. Spreadsheets: same topics as the [Data Carpentry lesson][dc-sheets] using Google Sheets.
   1. Unix shell: same topics as the [Software Carpentry lesson][swc-shell], with some [extra material][swc-shell-extra] on permissions.
   1. Python, NumPy, and Pandas: same topics as the [revised Software Carpentry lesson][swc-python], with extra material on writing command-line utilities.
   1. Pytest: new material.
   1. Jupyter Notebook: introduced *after* learners are comfortable processing tabular data in Python.
   1. Git and GitHub: same topics as the [Software Carpentry lesson][swc-git] (split into separate lessons on tracking and collaborating).
   1. SQL: same topics as the [Software Carpentry lesson][swc-sql].
   1. Project organization: topics taken from [Managing Research Software Projects][mrsp] and [Noble's rules][noble].
   1. Packaging: new material (using Pip rather than Conda for simplicity).
   1. Working with remote data: new material on the Python `requests` library.
   1. Publishing: new material on [Markdown][markdown] and [GitHub Pages][github-pages].
   1. Altair: new material.
1. What concepts will be introduced?
   1. Tidy data.
   1. Pipe and filter model.
   1. Version control repository.
   1. Embedded documentation for software.
   1. Key/value data.
   1. Program decomposition and iterative development.
   1. Vectorized (whole-array) operations.
   1. Commit.
   1. Merge and merge conflict.
   1. Pull request.
   1. Unit testing.
   1. Continuous integration.
   1. Task automation.
   1. Primary and foreign keys.
   1. Publication via text processing (rather than by using WYSIWYG tools).
1. What misconceptions are expected?
   1. Why would I use the shell instead of Python? (duplication of utility between tools)
   1. How come I can't open my data files? (Path issues when using GUI tools)
   1. What the hell is a "detached HEAD"? (and other Git weirdness)
   1. What are all these curly braces for? (indexing by name in dictionaries, JSON, etc.)
   1. How can two different variables have the same name? (variable scope)
   1. Why did parallelizing my work make it slower? (I/O-bound computation)
   1. Why can't I install this software/log in to this computer? (permissions)
1. What *won't* be covered?
   1. Connecting to remote computers using SSH: no time.
   1. Parallelizing map-reduce problem using GNU Parallel: too advanced.
   1. Serving data: it would be cool to show learners how to build data services, but all we can do in a short lesson is show them how to create security holes.
   1. Writing classes: we want to encourage a mostly-functional style of programming, and there isn't time to cover both higher-order functions and writing classes.
   1. LaTeX: [Markdown][markdown] plus [Pelican][pelican] are much simpler, and let us teach the same concepts (compiled, reproducible documents).
      - We use [Pelican][pelican] rather than [Jekyll][jekyll] because it's Python-based (we can build into `./docs` for publication).
      - And because it parallels the R course using [R Markdown][r-markdown].
   1. Conditionals and functions in the shell: learners will use Python for anything that complex.
   1. Docker: too advanced for the intended audience.
   1. GIS: not universally applicable.
   1. Image processing: ditto.
   1. Non-relational databases: there (still) isn't a clear leader, and relational databases allow us to introduce the key concepts.
   1. Interactive web pages (except the interactivity provided by Altair): there isn't time to teach JavaScript.
   1. Numerical or statistical methods: lots of high-quality courses already cover these topics.
   1. High-performance computing: high throughput is more widely useful.
   1. Symbolic debuggers: unless the course uses a Python IDE.

<!-- -------------------------------------------------------------------------------- -->

## Step 3: What mental models will learners form?

These concept maps were drawn with the desktop edition of [draw.io][draw-io].
To modify them, edit the XML, then select all and export as SVG
using "selection only" and "transparent background".

<figure>
  <figcaption>Variables and Values</figcaption>
  <img src="../files/design/variables-values.svg" alt="Variables and Values" />
</figure>

<figure>
  <figcaption>Programs</figcaption>
  <img src="../files/design/programs.svg" alt="Programs" />
</figure>

<figure>
  <figcaption>Projects</figcaption>
  <img src="../files/design/projects.svg" alt="Projects" />
</figure>

<!-- -------------------------------------------------------------------------------- -->

## Step 4: What will learners do along the way?

Another dozen exercise ideas will be added to this list before course development starts,
and all of them expanded to full text with accompanying solutions
to show how far learners will get by the end of each lesson.

1. Reorganize a messy spreadsheet full of field data.
1. Debug a stripped-down version of [`cvscut`][csvcut].
1. Iteratively build a Python tool to identify duplicate datasets.
1. Reorganize a small project to be consistent with [Noble's Rules][noble].
1. Package that project's scripts using Pip.
1. Clean up a set of inconsistently-formatted text data files using regular expressions.
1. Generate a CSV index of a photo archive.
1. Fetch data from a website using a REST API.
1. Create and merge pull requests that have merge conflicts.
1. Extend a Makefile to download data, merge it into existing data, and regenerate reports.
1. Write a program to pass a set of pre-written tests.
1. Publish a single-page website for a project on GitHub.

<!-- -------------------------------------------------------------------------------- -->

## Step 5: How are the concepts connected?

This outline is structured in hour-long blocks with three topics per hour.
That works out to only 15 minutes per topic,
since academic "hours" are only 50 minutes long,
and it always takes a few minutes to get started.
However,
we expect that learners will read the questions and answers before class,
then spend their in-time class working on self-paced exercises
with tutors and peers available to help them when they get stuck.

This outline is inspired in part by
the "[minimal manual](http://www.instructionaldesign.org/theories/minimalism.html)" approach to instructional design,
which suggests that:

1. All learning tasks should be meaningful and self-contained activities.
1. Learners should be given realistic projects as quickly as possible.
1. Instruction should permit self-directed reasoning and improvising by increasing the number of active learning activities.
1. Training materials and activities should provide for error recognition and recovery.
1. There should be a close linkage between the training and actual system.

This is *not* the same as creating cheatsheets
(though [the tldr site](https://tldr.ostera.io/) is really useful),
because cheatsheets assume readers already have a mental model and need to refresh details.

- Getting Started
  - Introduction to this Course
    - What is open science?
      - <http://ivory.idyll.org/blog/2016-what-is-open-science.html>
    - Why is it better than what we're doing now?
    - What is the roadmap for this course?

- Spreadsheets
  - Cleaning Up Spreadsheet Data
    - Why spreadsheets?
    - Why should we think of spreadsheets as having records with fields?
    - What headers should spreadsheet columns have?
    - What is the difference between numbers and text?
    - What is an atomic value?
  - Making Values Explicit
    - How can we use formulas to calculate new values in a spreadsheet?
    - Why should all values in a spreadsheet be explicit?
    - How can we debug dependencies in a spreadsheet?
  - Using Lookup Tables
    - How can we use a lookup table in a spreadsheet?
    - How can we use named ranges to make lookup tables more robust?
  - Exporting Data
    - How can we export data from a spreadsheet?
    - What is lost when we export data from a spreadsheet?
    - What is a record key?
    - Why should records have keys?
  - Common Spreadsheet Errors
    - What mistakes do people commonly make in spreadsheets?
    - How can we fix them?

- The Unix Shell
  - Introduction to the Unix Shell
    - What is the difference between an operating system and a shell?
    - Why the Unix shell?
    - How do we run bash?
    - What is an absolute path?
    - What is a relative path?
    - How do we see what's in a directory?
    - How do we move around in the shell?
  - Manipulating Files in the Shell
    - How do we view the contents of a text file?
    - How do we copy a file?
    - How do we move a file?
    - How do we rename a file?
    - How do we delete a file?
  - Editing Text Files
    - What's the difference between a text file and a binary file?
    - How do we run a text editor?
    - How do we edit text in a text editor?
    - How do we move around in a text editor?
    - How do we find and replace in a text editor?
  - Operating on Text
    - How do we find out how long a file is?
    - How do we select the top or bottom of a file?
    - How do we save the output of a command in a file?
  - Shortcuts
    - How do we see what I've done?
    - How do we use tab completion to fill in filenames?
    - How do we repeat previous commands?
  - Pipes
    - How do we combine two or more commands?
    - How do we select columns of text?
  - Variables
    - What is a variable?
    - How do we create variables?
    - How do we use variables?
    - What variables does the shell automatically create for us?
  - Writing Shell Scripts
    - "Ninety percent of most magic merely consists of knowing one extra fact." – Terry Pratchett
    - How do we execute commands saved in a file?
    - How do we pass filenames into a script?
  - Repeating Things in the Shell
    - What is a loop?
    - How do we write a loop in a shell script?
    - How do we write a loop interactively?

- Version Control
  - Introduction to Version Control
    - What is version control?
    - When and why should we use version control?
  - Setting Up
    - How can we configure version control on a new machine?
    - How can we create a repository?
    - How can we record changes to a set of files?
  - Viewing History
    - How can we view the history of a project?
    - How can we compare files to previous versions of themselves?
    - How can we ignore files we don't want to track?
  - Using Remote Repositories
    - What is a remote repository?
    - How can we create a remote repository?
    - How can we synchronize repositories?
  - Sharing Work
    - How can we work with other people's repositories?
    - How can we share our work with other people?
  - Collaborating
    - What kinds of licenses can we apply to our work?
      - <http://choosealicense.com/>
      - <http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>
    - How can we make our work easier to cite?
    - Where can we host our work?
  - Working with Branches
    - What is a branch?
    - When should we use branches?
    - How do we create branches?
    - How do we merge branches?
  - Handling Conflicts
    - What is a conflict?
    - How can we tell when a conflict has occurred?
    - How can we view a conflict?
    - How can we resolve conflicts?
  - Workflow
    - How are branches used to enable collaboration?

- Programming in Python
  - Introduction to Python
    - What is a programming language?
    - Why Python?
    - How do we create and use variables in Python?
  - Data Types
    - What are data types?
    - What data types does Python have?
    - What are type errors?
    - What are functions?
    - How do we call functions?
    - How can we use functions to convert data from one type to another?
  - Libraries
    - What is a library?
    - How do we use a library?
    - What are some commonly-used Python libraries?
  - Repeating Things in Python
    - How do we write a loop in Python?
  - Line-Oriented File I/O
    - How do we open, read, and close files in Python?
    - How do we read a file a line at a time?
  - Basic String Operations
    - What is a method?
    - What methods do strings have?
    - How can we use string methods to process text files?
  - Lists
    - What is a list?
    - How do we create a list?
    - How do we index a list?
    - How do we modify a list?
    - How do we loop over the elements of a list?
    - How do we loop over a range of numbers?
  - Conditionals
    - What is an `if` statement?
    - What are `else` and `elif` statements?
  - Writing Filters
    - How can we combine loops and conditionals to create filters?
    - How can we pass filenames to a Python script?
  - Errors
    - What is the difference between a syntax error and a runtime error?
    - How can we make sense of Python's error reports?
  - Getting Help
    - Where can we look for help when errors occur?
  - Asking for Help
    - How can we ask questions to elicit helpful responses?
  - Functions
    - When should we create a function?
    - What's the difference between defining a function and calling it?
    - How do we define a function?
    - How do we return a value from a function?
    - How do we call a function we have defined?
  - Passing Values to Functions
    - What is the difference between an argument and a parameter?
    - When are parameters created?
    - When are parameters destroyed?
  - Programming Style
    - What should we call the variables and functions we create?
    - How can we document functions?
  - Sets
    - What is a set?
    - Why are sets useful?
    - How do we create sets?
    - How do we manipulate sets?
    - What kinds of values can we store in sets?
    - What are sets good for?
  - Dictionaries
    - What is a dictionary?
    - How do we create dictionaries?
    - How do we manipulate dictionaries?
  - Using Dictionaries
    - What are dictionaries good for?

- Scientific Programming
  - Introduction to Arrays
    - What is NumPy?
    - What is an array?
    - How can we create arrays?
    - What properties do arrays have?
    - How can we read data into arrays?
    - How can we visualize arrays?
  - Indexing
    - What is a slice?
    - What are some common ways to slice arrays?
    - What are some common reasons to slice arrays?
  - Array Operations
    - What are whole-array operations?
    - Why are whole-array operations more efficient than loops?
    - How can we use NumPy to do linear algebra?
  - Images
    - What is the relationship between an image and an array?
    - How can we load and save images?
    - How can we manipulate pixel values?
  - Array Conditionals
    - What is a mask?
    - How can we use masks to manipulate images?
  - Image Processing
    - What is scikit-image?
    - What tools are in scikit-image?

- Data Analysis
  - Introduction to Pandas
    - What is Pandas?
    - What is a dataframe?
  - Reading, Writing, and Displaying Data
    - How can we read data into a dataframe?
    - How can we save dataframes to files?
  - Working with Dataframes
    - What properties do dataframes have?
    - What methods do dataframes have?
    - How can we select individual rows and columns from dataframes?
    - How can we create simple visualizations of dataframes?
  - Selecting Data from a Dataframe
    - How can we select subsets of data from dataframes?
  - Grouping Data
    - How can we operate on subsets of data from dataframes?
  - Cleaning Up Data
    - What is tidy data?
    - How can we create tidy data?

- Visualization
  - Introduction to Visualization
    - How can we choose the best kind of chart for our data and question?
    - What tools are available for creating charts?
      - <http://lisacharlotterost.github.io/2016/05/17/one-chart-tools/>
  - Faceted Data
    - How can we create faceted histograms?
    - How can we create bubble plots?
    - How can we create whisker plots?
  - Time Series Data
    - How can we create time series plots?

- Databases
  - Introduction to Databases
    - What is a relational database?
    - What is a database manager?
    - What database managers can we use?
    - When should we use a relational database?
  - Selecting Data from a Database
    - How can we select fields from a single table?
    - How can we order results?
    - How can we eliminate duplicate results?
  - Filtering
    - How can we select specific values from a single table?
    - How can we calculate new values during selection?
  - Handling Missing Data
    - What are nulls?
    - When should we use nulls?
    - How can we handle nulls in queries?
  - Aggregation
    - How can we combine multiple values?
    - How can we group values when combining them?
  - Combining Data
    - What is a join?
    - How are joins executed?
    - What is a primary key?
    - What is a foreign key?
  - Modifying Databases
    - How can we create a new table in a database?
    - How can we modify or delete data in a table?
  - Programming with Databases
    - How can we use databases from Python?
  - Comparison with Other Tools
    - How do relational databases compare to spreadsheets?
    - How do SQL queries compare to programming with Pandas?

- Working with Text
  - Introduction to Regular Expressions
    - What are regular expressions?
    - What basic patterns can regular expressions match?
  - Extracting Information
    - How can we get the parts of text that a regular expression matches?
  - Programming with Regular Expressions
    - How can we use regular expressions in Python?
    - How can we use regular expressions in the Unix shell?
    - How can we use regular expressions in SQL?
  - Introduction to OpenRefine
    - What is OpenRefine?
    - How can we facet, cluster, and split data in OpenRefine?
  - Scripting OpenRefine
    - How can we re-do data cleanup in OpenRefine?
  - Validating Data
    - How can we check the integrity of our data?

- Managing Data
  - Normalizing Data
    - What is normalized data?
    - How can we normalize our data?
  - Metadata
    - What is metadata?
    - How should we represent metadata?
    - Where should we store metadata?
  - Storing Data
    - What formats should we use for storing our data?
    - Where should we store data?

- Getting It Right
  - Introduction to Testing
    - What kinds of tests can we write for software?
    - Why can't testing ever prove that software is correct?
    - Why is it worth doing anyway?
    - How much testing is enough?
  - Writing Unit Tests
    - What is a unit test?
    - What outcomes can a unit test have?
    - How can we write unit tests?
    - How can we run unit tests?
  - Testing Floating Point Calculations
    - Why are floating point calculations hard to test?
    - How should we write tests for floating point calculations?
      - <https://peerj.com/articles/cs-58/>
  - Choosing Tests
    - What unit tests should we write?
    - When should we write our unit tests?
  - Introduction to Code Review
    - What is code review?
    - What are the benefits of code review?
    - When is code review not practical?
  - Reading Code
    - What should we look for when reviewing code?
  - Managing Code Reviews
    - Who should review what?
    - How should we respond to code reviews?
  - Continuous Integration
    - What is continuous integration?
    - How can we set up continuous integration with version control?
  - Designing Testable Software
    - What sorts of things make software harder to test?
    - How can we work around common obstacles to testability?
  - Introduction to Debugging
    - How can we use the experimental method to find and fix bugs?
  - Using a Debugger
    - What is a symbolic debugger?
    - How can we single-step through a program?
    - How can we set a breakpoint?
    - How can we set a conditional breakpoint?
  - Coverage Analysis
    - What is coverage analysis?
    - How can we see how much of our program we are testing?
    - How much coverage is enough?

- Making Programs Faster
  - Computer Architecture
    - How are modern computer systems organized?
    - How long do typical operations take?
  - Performance Profiling
    - How can we tell where a program is spending its time?
    - How can we tell if it will be possible to make a program faster?
    - How can we tell whether it will be worth making our programs faster?
  - Performance Tuning
    - How can we make our programs faster?

- Making Work Reproducible
  - Introduction to Make
    - What is a build manager?
    - When and why should we use a build manager?
  - Managing Dependencies
    - How do we express dependencies in Make?
    - How does make decide what commands to execute?
    - How can we generalize rules in Make?
  - Using Functions in Makefiles
    - Why should we use functions in Makefiles?
    - What are some commonly-used Make functions?

- Managing Research Software Projects
  - Organizing Projects
    - What are Noble's Rules?
    - Why should we organize projects this way?
  - Installing Software
    - What happens when software is installed?
    - How can we manage software installation?
  - Making Software Robust
    - What do we mean by "robust software"?
    - What are Taschuk's Rules?
    - How can we tell if software is robust?
  - Introduction to Packaging
    - What is a package manager?
    - Why should we rely on a package manager?
    - How does a package manager work?
  - Making Requirements Explicit
    - How can we make our program's requirements explicit?
  - Making a Package
    - How can we create a package so that other people can install our program?
    - <https://github.com/DamienIrving/teaching/blob/master/imas-pug/conda_tutorial.md>
  - Software Lifecycles
    - What is a software development lifecycle?
    - How do good research teams *actually* develop software?
  - Managing Requirements
    - How do we figure out what software ought to do?
    - How can we tell if it's doing it?
  - Issue Tracking
    - What is an issue tracker?
    - When and why are issue trackers better than simple to-do lists?
    - How can we write a good issue?
  - Managing Meetings
    - How can we make meetings more productive?
  - Making Projects Welcoming
    - What factors discourage individuals from taking part in open projects?
    - What can we do to reduce or eliminate these factors?
  - Making Projects Inclusive
    - What factors discourage groups from taking part in open projects?
    - What can we do to reduce or eliminate these factors?

- Publishing
  - 21st Century Publishing
    - How has the web changed research publishing?
    - What is an ORCID?
    - What is a DOI?
  - Managing Citations
    - What is a bibliography manager?
    - Why should we use a bibliography manager?
    - How should we publish our bibliography?
  - Introduction to HTML
    - What is HTML?
    - What are the basic elements of a web page?
    - How can we create web pages?
    - How can we publish web pages?
  - Markdown
    - What is Markdown?
    - What are some commonly-used features of Markdown?
    - How can we translate Markdown files into other formats?
  - Introduction to WordPress
    - What is WordPress?
    - How can we set up WordPress?
    - How can we create a simple website with WordPress?
  - Introduction to Jekyll
    - What is a templating engine?
    - How can we use the same layout for many pages?
    - How can we preview pages?
    - How can we publish a website on GitHub?
    - How does Jekyll compare to WordPress?
  - Using Variables
    - How can we configure Jekyll?
    - How does variable substitution work?
    - How can we use the same layout for all our pages?
    - How can we modularize our pages?
  - Blogging
    - What is RSS?
    - How does blogging work?
    - How can we create a blog using Jekyll and GitHub Pages?

- Working on the Web
  - Introduction to XML
    - What is XML?
    - How is XML different from HTML?
  - Working with HTML/XML
    - How do we represent HTML/XML in a program?
    - What are XPath and XQuery?
  - HTML in the Real World
    - Why is so much HTML badly formatted?
    - How can we process badly-formatted HTML?
  - HTTP
    - What is HTTP?
    - What is the HTTP request/response cycle?
    - How can we parameterize HTTP requests?
  - Getting Data from the Web
    - How can we get data from the web using Python?
    - How can we get data from the web using the Unix shell?
    - <http://www.meanboyfriend.com/overdue_ideas/2016/06/introduction-to-apis-using-iiif/>
  - Web Scraping
    - How can we get data from web pages?
  - Publishing Data from the Web
    - How should people publish data on the web?
    - How do people actually publish data on the web?

- Conclusion
  - What We Left Out
    - What is object-oriented programming?
    - What is high-performance computing?
  - Big Ideas
    - It's all data.
    - Programming is about creating and composing abstractions.
    - Models are for computers, views are for people.
    - Paranoia makes us productive.
    - Better algorithms are better than better hardware.
    - The tool shapes the hand.
    - Society shapes science for both good and ill.
  - Wrapping Up This Course
    - What does "done" look like?
    - How are we going to get there?

<!-- -------------------------------------------------------------------------------- -->

## Step 6: Course overview

### Course Description

This course is an introduction to research computing and data analysis
for people with little or no previous training in either.
It can be used either as the core of a one-semester for graduate or undergraduate course,
or for self-study by people who are thinking about becoming data scientists
and want a solid base to build on.

### Prerequisites

Learners will need:

- A personal computer with Internet access.
- The Bash shell.
- Python 3 (including the Jupyter Notebook).
- Google and GitHub accounts.

### Other Resources

- [Software Carpentry][swc]
- [Data Carpentry][dc]
- [Data Carpentry for Biologists][dcb]
- [Learn the tidyverse][tidyverse]
- "[Best Practices for Scientific Computing][best]"
- "[Good Enough Practices in Scientific Computing][good]"
- "[Ten Simple Rules for Making Research Software More Robust][robust]"
- [Managing Research Software Projects][mrsp]

{% include links.md %}

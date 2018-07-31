---
permalink: "/en/intro/"
title: "Introduction"
questions:
-   "What are open science, reproducible research, and computational competence?"
-   "Why are they better than what we're doing now?"
-   "What is the roadmap for this course?"
-   "What software is needed for this course?"
-   "What online accounts are needed for this course?"
keypoints:
- FIXME
---

FIXME

-   Real goal is better working practices
-   Teach tools to facilitate, encourage, and accelerate their use

## Good Enough Practices

-   Drawn from [[Wils2017](#CITE)]
-   The list is daunting, so this material introduces it piece by piece

1.  Data Management
    -   Save the raw data
    -   Ensure that raw data is backed up in more than one location
    -   Create the analysis-friendly data you wish to see in the world
    -   Record all the steps used to process data
    -   Anticipate the need to use multiple tables, and use a unique identifier for every record
    -   Submit data to a reputable DOI-issuing repository so that others can access and cite it
1.  Software
    -   Place a brief explanatory comment at the start of every program
    -   Decompose programs into functions
    -   Be ruthless about eliminating duplication
    -   Always search for well-maintained software libraries that do what you need
    -   Test libraries before relying on them
    -   Give functions and variables meaningful names
    -   Make dependencies and requirements explicit
    -   Do not comment and uncomment sections of code to control a program's behavior
    -   Provide a simple example or test data set
    -   Submit code to a reputable DOI-issuing repository
1.  Collaboration
    -   Create an overview of your project
    -   Create a shared to-do list for the project
    -   Decide on communication strategies
    -   Make the license explicit
    -   Make the project citable
1.  Project Organization
    -   Put each project in its own directory, which is named after the project
    -   Put text documents associated with the project in the `doc` directory
    -   Put raw data and metadata in a `data` directory, and files generated during cleanup and analysis in a `results` directory
    -   Put project source code in the `src` directory
    -   Put external scripts, or compiled programs in the `bin` directory
    -   Name all files to reflect their content or function
1.  Keeping Track of Changes
    -   Back up (almost) everything created by a human being as soon as it is created
    -   Keep changes small
    -   Share changes frequently
    -   Create, maintain, and use a checklist for saving and sharing changes to the project
    -   Store each project in a folder that is mirrored off the researcher's working machine
    -   Add a file called `CHANGELOG.txt` to the project's `docs` subfolder
    -   Copy the entire project whenever a significant change has been made
    -   Use a version control system
1.  Manuscripts
    -   Write manuscripts using online tools with rich formatting, change tracking, and reference management
    -   Write the manuscript in a plain text format amenable to version control

## Exercises {#s:intro-exercises}

{% include links.md %}

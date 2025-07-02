# The MUDE Book

This repository contains the source code for the MUDE Online Textbook from the 2024-25 academic year. It is the first version released with a CC BY license.  MUDE stands for Modelling, Uncertainty and Data for Engineers, a required module in the MSc programs from the faculty of Civil Engineering and Geosciences at Delft University of Technology in the Netherlands.

This book is constantly in development, so feel free to contribute! You can do so directly by forking this repository and creating a pull request. If you have access to this repository, create a branch and pull request to contribute directly.

The released book can be found on on https://tudelft-mude.github.io/book/. This page shows the built book of the default branch (it will be the upcoming academic year). All branches will also be visible as seen in the action's summaries: https://github.com/TUDelft-MUDE/book/actions

Development of the book is focused around its use as an online textbook for students in MUDE, which takes place from September through January each year. During this period improvements are generally released on a weekly basis. Major updates (for example, to the structure or layout of a page/chapter) are reserved for the following academic year, in order to avoid confusing students that actively used the book in class during the Fall. Therefore, to view the most recent "complete" version of this textbook, one should view the previous academic year, in this case, 2024 (this book!). 

Some parts of this book are taken directly from other git repositories (either as submodules or external resources). To contribute to those pages, contribute to the source repository directly with a fork and merge/pull request. If you intend to clone this book including its submodules, clone using: `git clone --recurse-submodules git@github.com:TeachBooks/manual.git`

Additional information about the book (especially for MUDE teachers) can be found at the MUDE Teacher site: [tudelft-mude.github.io/teacher/book](https://tudelft-mude.github.io/teacher/book).

Happy book building!

## Contact
If you encounter any issues, report it by clicking the GitHub icon and lightbulb on the top right corner of this page. Or contribute directly by creating a pull request in the [repository](https://github.com/TUDelft-MUDE/book).

If you have questions on the content, contact the MUDE team at MUDE-CEG@tudelft.nl. If you have technical questions regarding this book, contact the IT-coordinator of MUDE (Tom): T.R.vanWoudenberg@tudelft.nl

## Additional Information

There are several directories that were partially used in 2023-24 but are no longer used (they will be removed in a future PR):

- `book/`: primary source files for the book
- `code/`: auxiliary scripts for generating figures, etc. These are executed via eval-rst blocks, but the functionality is disabled for now.
- `unused/`: files that were removed from the book. Might be better to hide these in a branch unused/pd/

# The MUDE Book

This repository contains the source code for the MUDE Textbook. MUDE stands for Modelling, Uncertainty and Data for Engineers, a required module in the MSc programs from the faculty of Civil Engineering and Geosciences at Delft University of Technology in the Netherlands.

This book is constantly in development, so feel free to contribute! You can do so directly by forking this repository and creating a pull request. If you have access to this repository, create a branch and pull request to contribute directly.

The released book can be found on on [mude.citg.tudelft.nl/book/](https://mude.citg.tudelft.nl/book/). This page shows the built book of the default branch, which is the current or upcoming academic year. All branches will also be visible as seen in the action's summaries: [github.com/TUDelft-MUDE/book/actions](https://github.com/TUDelft-MUDE/book/actions). For previous years, the URL should be modified. For example: [mude.citg.tudelft.nl/book/**2024**](https://mude.citg.tudelft.nl/book/2024) is the version from the 2024-25 academic year (it is also the first version released with a CC BY license). An overview of the book and MUDE in general can be found on the MUDE website: [mude.citg.tudelft.nl/](https://mude.citg.tudelft.nl/).

Development of the book is focused around its use as an online textbook for students in MUDE, which takes place from September through January each year. During this period improvements are generally released on a weekly basis. Major updates (for example, to the structure or layout of a page/chapter) are reserved for the following academic year, in order to avoid confusing students that actively used the book in class during the Fall. A new version of the book will be released after MUDE is finished each year. Therefore, to view the most recent "complete" version of this textbook, one should view the previous academic year. See the section below more detailed information about versions and releases.

Some parts of this book are taken directly from other git repositories (either as submodules or external resources). To contribute to those pages, contribute to the source repository directly with a fork and merge/pull request. If you intend to clone this book including its submodules, clone using: `git clone --recurse-submodules git@github.com:TeachBooks/manual.git`

Additional information about the book (especially for MUDE teachers) can be found at the MUDE Teacher site: [tudelft-mude.github.io/teacher/book](https://tudelft-mude.github.io/teacher/book).

Happy book building!

## Contact

If you encounter any issues, report it by clicking the GitHub icon and lightbulb on the top right corner of this page. Or contribute directly by creating a pull request in the [repository](https://github.com/TUDelft-MUDE/book).

If you have questions on the content, contact the MUDE team at MUDE-CEG@tudelft.nl. If you have technical questions regarding this book, contact the IT-coordinator of MUDE (Tom): T.R.vanWoudenberg@tudelft.nl

## Versions and Releases

As the book consists of source code and a rendered website (HTML), versioning, releases and archives are handled in several ways. The README describes technical aspects of the book source code and supplemental publishing websites (e.g., Zenodo, PURE), whereas the [Credits Page](https://mude.citg.tudelft.nl/book/credits) of the book describes copyright and citation information of the book contents (remember to adjust the URL for the appropriate year as needed). In general, the GitHub repository [TUDelft-MUDE/book](https:github.com/TUDelft-MUDE/book) and book URL [mude.citg.tudelft.nl/book](https://github.com/TUDelft-MUDE/book) should be used as primary links for the book and its source code, whereas Zenodo is used as an archive and DOI publisher.

[TeachBooks Versioning](https://teachbooks.io/manual/features/versioning.html) is used (a special type of semantic numbering for educational purposes) with generic format `vA.B.C`, where `A` is the academic year for which the book is made (e.g., `2024` is for the 2024-25 academic year). The first complete version of the book for a give academic year uses `B=1` (e.g., `v2024.1.0` is the first complete version for 2024) and `C` is used to denote errata `C`. As the book is "complete" after the first `B=1` release for a given year, `B` should only be advanced is major changes or additions are made (i.e., to correct a major omission) and communicated clearly in the release notes. 

The HTML files associated with each release are archived to Zenodo in a zip file with DOI [10.5281/zenodo.16223062](https://doi.org/10.5281/zenodo.16223062). The zip file is the artifact downloaded manually from the Actions page and updloaded to Zenodo to (manually) create a new version.

Source code is versioned using Git and stored on GitHub in repository [TUDelft-MUDE/book](https://github.com/TUDelft-MUDE/book). Zenodo is used to automatically archive the source code for every release and associated with DOI [10.5281/zenodo.16227602](https://doi.org/10.5281/zenodo.16227602). The metadata for this Zenodo record comes from the file `CITATION.cff`; besides updating the list of editors, no metadata should be changed in this file (use the README, Credits page and/or other Zenodo record instead).

A PDF of the book will eventually be generated and uploaded to the TU Delft Repository (PURE) _work in progress._ The PDF is intended only for archival purposes in PURE and is not intended to be read.

In the future, additional records may be created to more easily enable citation of individual book chapters (e.g., Zenodo or PURE records for each chapter).

### Instructions for Creating a New Release

To create a new release, follow these steps:

1. If new editors are added, update the `CITATION.cff` file.
2. Ensure the book is built successfully in the Actions tab.
3. Create a new release in the GitHub repository and set the new version number per the description above.
4. Add release notes to summarize the changes: errata should be described concisely when `C` is advanced; more detailed description is required if `B` is advanced.
5. Download the HTML files from the Actions page as a zip file (choose the branch on which the new release was made.
6. Manually update the Zenodo record for the book website ([zenodo.org/records/16223062](https://zenodo.org/records/16223062)) by: uploading the zip file, changing the version number and updating metadata as needed (e.g., add new editors).
7. Confirm that the Zenodo record for the source code ([zenodo.org/records/16227602](https://zenodo.org/records/16227602)) was automatically advanced.

## Additional Information

There are several directories that were partially used in 2023-24 but are no longer used (they will be removed in a future PR):

- `book/`: primary source files for the book
- `code/`: auxiliary scripts for generating figures, etc. These are executed via eval-rst blocks, but the functionality is disabled for now.
- `unused/`: files that were removed from the book. Might be better to hide these in a branch unused/pd/

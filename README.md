# The MUDE Book

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16227601.svg)](https://doi.org/10.5281/zenodo.16227601)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16223061.svg)](https://doi.org/10.5281/zenodo.16223061)
[![call-deploy-book](https://github.com/TUDelft-MUDE/book/actions/workflows/call-deploy-book.yml/badge.svg)](https://github.com/TTUDelft-MUDE/book/actions/workflows/call-deploy-book.yml)

This repository contains the source code for the MUDE Textbook. MUDE stands for Modelling, Uncertainty and Data for Engineers, a required module in the MSc programs from the faculty of Civil Engineering and Geosciences at Delft University of Technology in the Netherlands.

This book is constantly in development, so feel free to contribute! You can do so directly by forking this repository and creating a pull request. If you have access to this repository, create a branch and pull request to contribute directly.

The released book can be found on on [mude.citg.tudelft.nl/book/](https://mude.citg.tudelft.nl/book/). This page shows the built book of the default branch, which is the current or upcoming academic year. All branches will also be visible as seen in the action's summaries: [github.com/TUDelft-MUDE/book/actions](https://github.com/TUDelft-MUDE/book/actions). For previous years, the URL should be modified. For example: [mude.citg.tudelft.nl/book/**2024**](https://mude.citg.tudelft.nl/book/2024) is the version from the 2024-25 academic year (it is also the first version released with a CC BY license). An overview of the book and MUDE in general can be found on the MUDE website: [mude.citg.tudelft.nl/](https://mude.citg.tudelft.nl/).

Development of the book is focused around its use as an online textbook for students in MUDE, which takes place from September through January each year. During this period improvements are generally released on a weekly basis. Major updates (for example, to the structure or layout of a page/chapter) are reserved for the following academic year, in order to avoid confusing students that actively used the book in class during the Fall. A new version of the book will be released after MUDE is finished each year. Therefore, to view the most recent "complete" version of this textbook, one should view the previous academic year. See the section below more detailed information about versions and releases.

Some parts of this book are taken directly from other git repositories (either as submodules or external resources). To contribute to those pages, contribute to the source repository directly with a fork and merge/pull request. If you intend to clone this book including its submodules, clone using: `git clone --recurse-submodules git@github.com:TeachBooks/manual.git`

Additional information about the book (especially for MUDE teachers) can be found at the MUDE Teacher site: [mude.citg.tudelft.nl/teacher/book](https://mude.citg.tudelft.nl/teacher/book).

Happy book building!

## Contact

If you encounter any issues, report it by clicking the GitHub icon and lightbulb on the top right corner of this page. Or contribute directly by creating a pull request in the [repository](https://github.com/TUDelft-MUDE/book).

If you have questions on the content, contact the MUDE team at MUDE-CEG@tudelft.nl. If you have technical questions regarding this book, contact the IT-coordinator of MUDE (Tom): T.R.vanWoudenberg@tudelft.nl

## Versions and Releases

As the book consists of source code and a rendered website (HTML), versioning, releases and archives are handled in several ways. The README describes technical aspects of the book source code and supplemental publishing websites (e.g., Zenodo, PURE), whereas the [Credits Page](https://mude.citg.tudelft.nl/book/credits) of the book describes copyright and citation information of the book contents (remember to adjust the URL for the appropriate year as needed). In general, the GitHub repository [TUDelft-MUDE/book](https:github.com/TUDelft-MUDE/book) and book URL [mude.citg.tudelft.nl/book](https://github.com/TUDelft-MUDE/book) should be used as primary links for the book and its source code, whereas Zenodo is used as an archive and DOI publisher.

[TeachBooks Versioning](https://teachbooks.io/manual/features/versioning.html) is used (a special type of semantic numbering for educational purposes) with generic format `v<academic_year>.<additions>.<errata>`, with an additional `.pre-release` added for incomplete books (e.g., `v2024.1.0` is the first complete version for 2024, while v2025.0.1.pre-release is an incomplete version for 2025). Releases on GitHub and Zenodo are only made for non-`.pre-release` versions.

The HTML files associated with each release are archived to Zenodo in a zip file with DOI [10.5281/zenodo.16223061](https://doi.org/10.5281/zenodo.16223061), which will automatically resolve to the newest DOI (not necessarily the most recent GitHub release). The zip file is the artifact downloaded manually from the Actions page and uploaded to Zenodo to (manually) create a new version.

Source code is versioned using Git and stored on GitHub in repository [TUDelft-MUDE/book](https://github.com/TUDelft-MUDE/book). Zenodo is used to automatically archive the source code for every release and associated with DOI [10.5281/zenodo.16227601](https://doi.org/10.5281/zenodo.16227601), which will automatically resolve to the newest DOI, as well as the most recent GitHub release (this may not be in sequential order in terms of academic years). The metadata for this Zenodo record comes from the file `CITATION.cff`; besides updating the list of editors and the appropaite DOI for the Zenodo book record, no metadata should be changed in this file (use the README, Credits page and/or Zenodo book record instead).

A PDF of the book is generated and uploaded to the TU Delft Repository (PURE). This adds attribution to the TU Delft profile of involved authors. The PDF is intended only for archival purposes in PURE and is not intended to be read.

In the future, additional records may be created to more easily enable citation of individual book chapters (e.g., Zenodo or PURE records for each chapter).

Note that there are effectively two numeric ways of versioning the book: the version number (defined by git tags and GitHub Releases manually, according to the rules above) and the Zenodo-generated DOI. There should be a one-to-one correspondence between the two, but the Zenodo DOI will not necessarily be sequential. Because the Zenodo DOI is both a permanent identifier _and_ a hyperlink, it is used in the recommended citation format for the book and its chapters. If desired, the book version can also be used, but this should only be necessary if it is important to distinguish between two versions of the book that were published for the same academic year (e.g., if a major change was made after the first release of the book for that year).

### Instructions for Creating a New Release

To create a new release, follow these steps:

1. If new editors are added, update the `CITATION.cff` file.
2. Visit [zenodo.org/records/16223061](https://zenodo.org/records/16223061) and create a new (draft!) version of the HTML files record. Manually update the version number and URL's in the description when the academic year (`A`) changes. Generate a new DOI by clicking the button "Get a DOI now," which will be used in the following step.
3. Use the DOI generated in the previous step to update source code of the book. This is best accomplished by doing a text find-and-replace search, and should modify files `README.md`, `credits.md`, `CITATION.cff`, and `references.bib`. The version number (e.g., year) should only be updated when a new academic year is released. Do not replace DOI's `16223061` or `16227601`, as these will automatically resolve to the newest DOI for each Zenodo record and are important for these README instructions.
4. Commit changes and ensure the book is built successfully in the Actions tab on the desired branch. Note that the DOI link on the Credits page will not work until the Zenodo record is published, several steps below.
5. Create a new release in the GitHub repository and set the new version number per the description above (`vA.B.C`) as the tag and Release title (be sure to choose the correct target branch; the default branch is typically not the branch containing the version intended for readers). 
6. Add release notes to summarize the changes: errata should be described concisely when `C` is advanced; more detailed description is required if `B` is advanced. Include the new DOI from the step above.
7. Download the HTML files from the Actions page as a zip file (choose the branch on which the new release was made), then upload the zip file to Zenodo and publish the record.
8. Confirm that the Zenodo record DOI for the book ([zenodo.org/records/16223061](https://doi.org/10.5281/zenodo.16223061)) was updated and matches that in the book on the README, Credits and References pages. 
9. Confirm that the Zenodo record DOI for the source code ([zenodo.org/records/16227601](https://zenodo.org/records/16227601)) was automatically advanced.

## Additional Information

There are several directories that were partially used in 2023-24 but are no longer used (they will be removed in a future PR):

- `book/`: primary source files for the book
- `code/`: auxiliary scripts for generating figures, etc. These are executed via eval-rst blocks, but the functionality is disabled for now.
- `unused/`: files that were removed from the book. Might be better to hide these in a branch unused/pd/

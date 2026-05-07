(credits)=
# Credits and License

You can refer to the most recent version of this book as:

> Ding, J. Lanzafame, R., van der Meer, F. van Woudenberg, T., Verhagen, S. (Eds.) (n.d.), Modelling, Uncertainty and Data for Engineers (MUDE) Textbook, Delft University of Technology. https://mude.citg.tudelft.nl/book, CC BY 4.0.

The introduction, structure of the book and formatting of contents is done under direction of the Editors, in collaboration with a large team of co-authors and student assistants. Some chapters and pages have additional primary authors who are identified within the book either at the bottom of the first page in a chapter, or at the bottom of an individual page, as necessary. If an author is not listed on a particular chapter or page, the editors may be attributed as the authors. Furthermore, as contents of this book may change each academic year, we cannot guarantee that chapter titles and URL's will remain static indefinitely. Therefore, if it is important for you to reference a specific location within the book, we recommend including the complete URL and version in your reference:

> `<Primary Authors>`, `<Title of Chapter or Page>`. In Ding et al. (n.d.), _Modelling, Uncertainty and Data for Engineers (MUDE) Textbook._ Delft University of Technology. https://mude.citg.tudelft.nl/book/`<year>/<...>`, version `<version_number>`, CC BY 4.0.

The book in its entirety is available in the 2025 edition (2026 edition will follow in spring 2027), please note that only for complete versions of the book a DOI is created. Refer to this version as follows:

> Ding, J. Lanzafame, R., van der Meer, F. van Woudenberg, T., Verhagen, S. (Eds.) (2025), Modelling, Uncertainty and Data for Engineers (MUDE) Textbook, Delft University of Technology. https://mude.citg.tudelft.nl/book/2025, version v2025.16.6, CC BY 4.0. [doi:10.5281/zenodo.18241869](https://doi.org/10.5281/zenodo.18241869).

````{admonition} BibTeX Citation
:class: tip, dropdown

If you would like to refer to the MUDE Textbook with BibTeX (e.g., in a TeachBook or Jupyter Book), the following entries can be used in a  `bib` file to get close to the references shown above. Use the GitHub repository for this book as a reference for setting up APA citations (if desired).

```bibtex
@book{mude_most_recent,
  title={Modelling, {U}ncertainty and {D}ata for {E}ngineers ({MUDE}) {T}extbook},
  editor={Ding, Jialei and Lanzafame, Robert and van der Meer, Frans and van Woudenberg, Tom and Verhagen, Sandra},
  year={n.d.},
  publisher={Delft University of Technology},
  note={{s://mude.citg.tudelft.nl/book} CC BY 4.0}
}
```

or including a specific location and version (URL and version number to be adapted):

```bibtex
@book{mude_most_recent,
  title={Modelling, {U}ncertainty and {D}ata for {E}ngineers ({MUDE}) {T}extbook},
  editor={Ding, Jialei and Lanzafame, Robert and van der Meer, Frans and van Woudenberg, Tom and Verhagen, Sandra},
  year={n.d.},
  publisher={Delft University of Technology},
  note={{s://mude.citg.tudelft.nl/book/`<year>/<...>`},version `<version_number>`, CC BY 4.0}
}
```

The text citation is {cite:t}`mude_most_recent` and the parenthetical citation is {cite:p}`mude_most_recent`.

Or for the complete 2025 edition:

```bibtex
@book{mude2025,
  title={Modelling, {U}ncertainty and {D}ata for {E}ngineers ({MUDE}) {T}extbook},
  editor={Ding, Jialei and Lanzafame, Robert and van der Meer, Frans and van Woudenberg, Tom and Verhagen, Sandra},
  year={2025},
  publisher={Delft University of Technology},
  edition={v2025.16.6},
  note={{s://mude.citg.tudelft.nl/book/2025} CC BY 4.0},
  doi={10.5281/zenodo.18241869}
}
```

The text citation is {cite:t}`mude2025` and the parenthetical citation is {cite:p}`mude2025`.

````

## How the book is made

This book is created using open source tools: it is a Jupyter Book that uses a number of features from [TeachBooks](https://teachbooks.io/) and is written using Markdown, Jupyter notebooks and Python files to generate some figures. The source files are stored on a public GitHub repository [github.com/TUDelft-MUDE/book](https://github.com/tudelft-mude/book/). Zenodo is used to archive all open versions of the book (beginning with the 2024-25 academic year) and to provide a DOI ([10.5281/zenodo.16223061](https://doi.org/10.5281/zenodo.16223061)).  View the repository README file or contact the editors for additional and up-to-date information.

## Acknowledgements

This book has many contributors, many of whom are also key members of the MUDE Team, as well as critical feedback from MUDE students. The sections below list the primary authors and contributors for each chapter, buit is unfortunately not possible to list all of the small contributions from various people from within and outside Delft University of Technology, not list all contributions in detail. A special note should go to the MUDE management team, which take a lead in organizing the module and keeping this book up-to-date with the latest course developments.

A better way to see the contributions is to check the [Contributors Page](https://github.com/TUDelft-MUDE/book/graphs/contributors) of the GitHub repository.

A big "thank you" is also due to the Educational Management Team of the Civil Engineering and Geosciences Faculty at Delft University of Technology for giving the MUDE Team financial and organizational support during the early years of MUDE (especially 2022-2024), in particular Hans Welleman, Director of Education of the faculty. Without the freedom and support to experiment with new tools, this book (and [TeachBooks](https://teachbooks.io/) as well!) would not exist!

And in the end, none of this would have happened if it weren't for the quick meeting between Robert Lanzafame, Caspar Jungbacker and Thirza Feenstra in the Fall of 2022 when we considered making our first Jupyter Book and decided to "go for it!" Caspar Jungbacker set up the first book later that year, which is why the book worm in the TeachBooks logo is named "Caspar."

## License

This manual is [CC BY 4.0 licensed](https://creativecommons.org/licenses/by/4.0/) allowing you to share and adapt the material, as long as the source is named. Resources that are _not_ included under the CC BY license and external resources that are reused in this book are listed in the sections below.

If an author is not listed on a particular page, it is by the Editors (for example, the introduction page of some chapters).

Auxiliary files such as figures, code, videos, etc, are included under the license of this book and should be attributed to the authors of the chapter or page where they are used, unless otherwise stated below or in the file itself. Text-based files (i.e., non-binary) are typically stored in the repository, within the subdirectory where the source file of the chapter or page is located. Binary files are stored in a separate GitHub repo using LFS (`https://github.com/TUDelft-MUDE/source-files/raw/main/file/<binary_file_name>`). Videos and quiz questions are stored in and served from YouTube and H5p; contact the MUDE Team directly if you are interested in source materials for these resources.

(external_resources)=
### External Resources

Parts of this book are taken from other external resources and reused in various ways (some of which are _not_ shared with a permissive license). Entire chapters or pages are listed individually in the {ref}`external_resources` section below. Resources that are used _within_ a page and/or are modified by MUDE authors are listed individually in the {ref}`internal_resources` section below.

(credits_not_cc_by)=
### Resources _not_ under CC BY

CC BY conditions are _not_ applicable to some resources included in this book which resources cannot be reused without explicit permission from the original copyright holder. In some cases, external resources are provided under their own permissive license (e.g., CC BY), in which case permission and instructions for use are already explicitly provided by the copyright holder; however this is not always the case. All resources that are _not_ included in the CC BY license of this book are listed individually in the sections below, either: within the summary of each chapter or page, or as entire chapters or pages in {ref}`external_resources`.

(internal_resources)=
## Individual Chapters and Pages

Credits are provided here for chapters and pages that are released under the license of this book (internal resources). Please note that this is a living document and will be updated as new contributions are made. Whenever a complete version of the book is published, the state of contributions is finalized for that version. Use the guidance provided above to properly share, reuse and cite relevant chapters, pages or any other resources from this book.

(modelling_concepts_credit)=
### Chapter: Modelling Concepts

> {ref}`Modeling concepts <modelling_concepts>` is written by Alessandro Cabboi, Patricia Mares Nasarre and Robert Lanzafame.
>
> Special thanks goes to João Moura Pereira de Lucas Teixeira, who created first draft of pages from powerpoint slides.

(numerical_modelling_credit)=
### Chapter: Numerical Modelling

> {ref}`Numerical modelling <numerical_modelling>` is written by Jaime Arriaga Garcia, Anna Störiko, Justin Pittman and Robert Lanzafame.
>
> Special thanks goes to:
> - Isabel Slingerland and Mona Devos for critical feedback and development of exercises, figures and related content.
> - Ronald Brinkgreve, Dhruv Mehta and Ajay Jagadeesh for feedback on structure, content.
>
> {ref}`The animated figure on the Jamuna river <NumericalMethodsRiver>` included on page {ref}`Numerical modelling <numerical_modelling>` but is _not_ included under the CC BY license of this book. Original content is used here with explicit permission of Amgad Omer on behalf of Deltares.
>
> {ref}`The figure on the left Riemann sum <openstax_fig_01>` is reproduced from {cite:t}`openstax_calculus` without modification and is _not_ included under the CC BY license of this book. The source content is provided with a CC BY NC SA license and can be accessed for free at [https://openstax.org/books/calculus-volume-2/pages/1-introduction](https://openstax.org/books/calculus-volume-2/pages/1-introduction).

(distributions_credit)=
### Chapter: Univariate Continuous Distributions

> [Univariate Continuous Distributions](./univariate_distributions/appendix_overview.md) is written by Patricia Mares Nasarre, Robert Lanzafame and Max Ramgraber.
>
> Special thanks goes to Oswaldo Morales Napoles and Elisa Ragno for suggestions on the theoretical and didactic framework, as well as critical feedback and review.
>
> The interactive figures in these pages are created by Max Ramgraber ([maxramgraber.com/interactive](https://www.maxramgraber.com/interactive)), which are published with a CC BY license and included in this book without modification.

(multivariate_credit)=
### Chapter: Multivariate Distributions

> {ref}`Multivariate Distributions <mult_dist>` is written by Patricia Mares Nasarre and Robert Lanzafame.
>
> Special thanks goes to Oswaldo Morales Napoles and Elisa Ragno for suggestions on the theoretical and didactic framework, as well as critical feedback and review.
>
> {ref}`This <element_correlation_correlation>` and {ref}`this <2D_Gaussian>` interactive figures are created by Max Ramgraber ([maxramgraber.com/interactive](https://www.maxramgraber.com/interactive)), published with a CC BY license and included in this book without modification. 

(uncertainty_propagation_credit)=
### Chapter: Uncertainty Propagation

> {ref}`Uncertainty Propagation <01_errorprop>` is written by Sandra Verhagen and Lotfi Massarweh.
>
> This chapter builds on the lecture notes _Probability and Observation Theory_ by P.J.G. Teunissen, D.G. Simons, C.C.J.M. Tiberius (2009).
>

(observation_theory_credit)=
### Chapter: Observation Theory

> {ref}`Observation theory <OT>` is written by Sandra Verhagen.
>
> Special thanks goes to:
> - Peter Teunissen and Christiaan Tiberius who co-shaped the material, indirectly, through collaboration with the author as TU Delft colleagues.
> - The books _Adjustment theory: an introduction_ {cite:p}`adjustment_theory` and _Testing theory: an introduction_ {cite:p}`testing_theory` which provided the framework for this chapter.
> - Sophie Keemink, Caspar Jungbacker and Thirza Feenstra, who provided feedback and helped develop exercises.

(numerical_methods_for_pdes_credit)=
### Chapter: Numerical Methods for PDEs

> {ref}`Numerical Methods for PDEs <NumMethPDE>` is written by Marcel Zijlema.
>
> _This chapter reuses material from Lecture Notes "Course CIE4340 - Computational Modelling of Flow and Transport" by Marcel Zijlema (TU Delft, 2023)._
> This reader can be downloaded [here](https://www.tudelft.nl/en/student/my-study-me/education/study-start/book-reader-sales/downloading-and-ordering-readers).


(finite_element_method_credit)=
### Chapter: Finite Element Method

> {ref}`Finite Element Method <finite_element_method>` is written by Frans van der Meer. 
>
> _The material in this chapter is also incorporated in an in-depth book "Finite Elements in Civil Engineering and Geosciences" by Oriol Colomés, Iuri Rocha, Frans van der Meer and Martin Lesueur which can be found [here](https://interactivetextbooks.citg.tudelft.nl/computational-modelling)._
>
> Special thanks goes to Lex Niessen who greatly assisted in developing material on the finite element method for the first edition of MUDE, which was the starting point for this chapter. 

(signal_processing_credit)=
### Chapter: Signal Processing

> {ref}`Signal processing <signal_processing>` is written by Christiaan Tiberius.
>
> _The material in this chapter is related to an in-depth book "Engineering signal analysis - from Fourier to filtering" by Christiaan Tiberius and Max Mulder (TU Delft Open Publishing, 2025)._
>
> Special thanks goes to:
> - Max Mulder for being a signal processing soul-mate, sparring-partner and TU Delft colleague of the author who co-shaped the material, indirectly, through collaboration since early 2000's.
> - Jelle Knibbe, who reviewed, commented and/or modified content of original powerpoint slides.
> - João Moura Pereira de Lucas Teixeira, created first draft of pages from powerpoint slides.
> - Antonio Magherini, who reviewed, commented and/or modified content.
>
> {ref}`The animated unity circle figure <unitycircle>` is included on page {ref}`Fourier series <fourier_real>` but is _not_ included under the CC BY license of this book. Original content licensed under CC BY-SA 4.0 by {cite:t}`BFG` and can be found [here](https://commons.wikimedia.org/wiki/File:Unitycircle-complex.gif); used here without modification.

(time_series_analysis_credit)=
### Chapter: Time Series Analysis

> {ref}`Time Series Analysis <tsa>` is written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen.
>
> _The initial framework and contents of this chapter were created by Alireza Amiri-Simkooei, which was then revised and updated by Sandra and Christian._
>
> Special thanks goes to:
> - Berend Bouvy, who created a number ofinteractive figures and exercises, as well as provided critical feedback.
> - Serge Kaplev and Lucas Alvarez Navarro, who provided critical feedback and suggestions for the theoretical content.
> - Antonio Magherini, who created the first draft material from powerpoint slides and prepared notebooks as exercises.
> 
> The following resources are used in this chapter but are _not_ included under the CC BY license of this book:
> - {ref}`The IPCC prediction figure <cover>` is used on page {ref}`Time Series Analysis <tsa>` (not modified) and is from {cite:t}`ipcc2018`.
> - {ref}`The global mean sea level figure <trend>` is used on page {ref}`Components of time series <components>` (not modified) and is from {cite:t}`csiro`.

(optimization_credit)=
### Chapter: Optimization

> {ref}`Optimization <optimization>` is written by Nadia Pourmohammadzia, Gonçalo Homem de Almeida Correia, Maria Nogal Macho, Jie Gao and Bahman Ahmadi.
>
> _Gonçalo Homem de Almeida Correia created most of the material. Maria Nogal Macho and Bahman Ahmadi made contributions to various parts. Bahman Ahmadi developed the exercises in Python and Jupyter notebooks. Jie Gao created the genetic algorithm material._
>
> Special thanks goes to:
> - Jialei Ding, who reviewed material and made improvements to the traffic exercise.
> - Tom van Woudenberg, who edited text and improved content and structure for online interactive textbook format.
> - João Moura Pereira de Lucas Teixeira, who created first draft of pages from powerpoint slides.
>
> The {ref}`Road Network Design Problem <optimization_project>` pages are included in this chapter but are _not_ included under the CC BY license of this book; they are in-class exercises that will be shared by the authors of this book as part of a future publication (also under a CC BY license; citation will be provided here after publication).
>
> Several figures are included in this chapter but are _not_ included under the CC BY license of this book:
> - {ref}`The figure on convex / nonconvex figures <convex_non_convex>` is used on page {ref}`Taxonomy of optimization models <optimization_taxonomy>`; the convex 3D figure is from {cite:t}`Agrawal2021` and the non-convex 3D figures is from {cite:t}`Nogal2021`. Both are included as part of the figure shown in this book modification.
> - {ref}`The figure on linear vs convex programming <recap_simple_branch_bound>` is used on page {ref}`Genetic algorithm <optimization_genetic_algorithm>` and is from {cite:t}`Danshian2025` (left) and the figure on the right is from an unknown source. Both are included as part of the figure shown in this book without modification.
> - {ref}`This <computation_complexity>`, {ref}`this <metaheuristic_approach>`, {ref}`this <metaheuristic_approach2>`, {ref}`this <evolutionary_algorithm>`, {ref}`this <termination>`, {ref}`this <genetic_algorithm_diagram>`, {ref}`this <single_point_crossover_diagram>`, {ref}`this <single_point_crossover_diagram2>` and {ref}`this figure <genetic_new_population>` on page {ref}`Genetic algorithm <optimization_genetic_algorithm>`  are not included under the CC BY license of this book, as they are from unknown sources and will be replaced.

(machine_learning_credit)=
### Chapter: Introduction to Machine Learning

> {ref}`Machine learning <machine_learning>` is written by Iuri Rocha, Anne Poot, Joep Storm and Leon Riccius.

(extreme_value_analysis_credit)=
### Chapter: Extreme Value Analysis

> {ref}`Extreme Value Analysis <eva>` is written by Patricia Mares Nasarre.
>
> Special thanks goes to Oswaldo Morales Napoles, Elisa Ragno and Robert Lanzafame for suggestions on the theoretical and didactic framework, as well as critical feedback and review.

(risk_reliability_credit)=
### Chapter: Risk and Reliability

> {ref}`risk_reliability` is written by Patricia Mares Nasarre, Max Ramgraber and Oswaldo Morales Napoles. 

(programming_credit)=

### Programming chapters

> The programming chapters are written by Tom van Woudenberg, Robert Lanzafame and Frans van der Meer.
>
> Special thanks goes to Stanislaw Ostyk-Narbutt for his contribution with the Large language models chapter

Part of the chapters in the Programming part of this book are reused from two sources: _Learn Programming for Engineers_ {cite:p}`learn-programming` and _Python for Engineers_ {cite:p}`learn-python`. Both books are published with a CC BY license and are available online at [teachbooks.io/learn-programming](https://teachbooks.io/learn-programming) and [teachbooks.io/learn-python](https://teachbooks.io/learn-python).


## Contact

If you have questions on the content, contact the MUDE team at MUDE-CEG@tudelft.nl. If you have technical questions regarding this book, contact the IT-coordinator of MUDE (Tom): T.R.vanWoudenberg@tudelft.nl.


DRAFT TEXT of email from Robert to MUDE authors:

Dear MUDE Textbook author,

We are currently working hard to make the MUDE Textbook completely open: no longer password protected, and with a clear open source license (CC BY). There are many reasons for doing this, most important of which are to make sure students can use it after they graduate; we can share the amazing resource we have created; and that everyone can be recognized for their contributions.

This email is to inform you how the attribution and referencing will be done, since you are a primary author. As there is a lot of information in this email, note that the most important thing is to let us know if you think the way we are describing your chapter is appropriate, and to make any corrections to the information provided below that you think are necessary.

While we think that the general structure and editor-author arrangement is nearly final, any other feedback you have is still very much welcome!

Kind regards,
Robert, Tom and Sandra

Before diving into the MUDE details, we want to be sure you understand what a CC BY license means. First, note that CC BY is the "attribution" license (BY) created by the Creative Commons organization (CC). It basically means yes, someone can take your work and use it in various ways; however, they also need to clearly state that it came from you. Read more here: https://creativecommons.org/licenses/by/4.0/deed.en

As to why CC BY is a good thing, here is a concise and informative blog post that lays things out nicely; especially the table of licenses will hopefully clarify this for you: https://agilescientific.com/blog/2021/2/17/which-open-licence-should-i-choose

The book, in its current form, was first used in the 2023-24 academic year. Although there were several authors that made great contributions, it was Tom, Sandra and I that were looking more at the overall structure and flow of the book. As such, we propose to be listed as Editors, but acknowledge the contributions of other authors and collaborators in the specific chapters where their effort was concentrated. The following text illustrates how the entire book will be described on the Credits page:

=====================

You can refer to this book in its entirety as:

> Lanzafame, R., van Woudenberg, T., Verhagen, S. (2024), Modelling, Uncertainty and Data for Engineers (MUDE) Textbook, Delft University of Technology. https://mude.citg.tudelft.nl/book. Retreived [Month, Year]. CC BY 4.0.

The introduction, structure of the book and formatting of contents is done under direction of the Editors (Robert Lanzafame, Tom van Woudenberg and Sandra Verhagen), in collaboration with a large team of co-authors and student assistants. Some chapters and pages have additional primary authors who are identified within the book either at the bottom of the first page in a chapter, or at the bottom of an individual page, as necessary. If an author is not listed on a particular chapter or page, the editors may be attributed as the authors.

You can refer to individual chapters or pages within this book as:

> `<Primary Authors>` (2024) `<Title of Chapter or Page>`. In Lanzafame et al. (Eds.), _Modelling, Uncertainty and Data for Engineers (MUDE) Textbook._ Delft University of Technology. https://mude.citg.tudelft.nl/book.

_Individual chapters/pages will be listed on this page as well, as described at the beginning of this email for each particular case._


=====================

The following sets of text will be included to describe how **your chapter** is presented in the book (make sure you agree with this way of presenting it!):

At the bottom of the Credits page:

Chapter <title> is written by <authors>. Special thanks goes to <name> for <contribution>.

On the first page of a chapter, the following text will be included:

> This Chapter is written by `<Primary Authors>`. Find out more here.

The "Find out more here" link will point to the Credits page of the book, which will include a list of all authors and their contributions, including the text shown above.

At the bottom of each page in a chapter (except the first page), a piece of text like this may be included (still working this part out):

> This page is part of Chapter `<Title of Chapter>` written by `<Primary Authors>`. Find out more here.

=====================

Within the git repository of the book we will also include a file that includes additional information for each chapter, some of which can also be included in the text of the book on an as-needed basis. For example, if the chapter also (re)uses material from other sources like images, special licenses, a few notes about where it came from, etc. At the moment, the (draft) record for your chapter is shown here:

```yaml
  uncertainty_propagation:
    author:
      - Sandra Verhagen
    title: Propagation of Uncertainty
    license: CC BY 4.0
    acknowledgement:
      - who: Robert Lanzafame, Patricia Mares Nasarre, Max Ramgraber
        what: reviewed, commented and/or modified content
      - who: Antonio Magherini
        what: converted the slides to book format
```
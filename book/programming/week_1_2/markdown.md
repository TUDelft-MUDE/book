# Markdown

Programming yourself is one thing, communicating it with others equally as important. imagine you will be sending some code to a classmate or a teacher and you really want them to be able to see the final answer easily, while also being able to understand how you arrived at it. Sending them python file (e.g. `.py` or `.ipynb`) might confuse them, even if you add a lot of comments. Therefore, you could accompany it with a nice report, with your code only as an appendix and way to generate result you present in the report.

Markdown is a _markup language_ that makes it possible to write richly-formatted text in markdown files (`.md`) or Jupyter notebooks (`.ipynb`). It's a very basic formatting language, which is very useful with version-control systems like git. We will use Markdown on a weekly basis in our MUDE project reports, so this is a good chance to use it for the first time, if you never have.

## Basic markdown formatting

Here are a few formatting tips:

- Write out lists by beginning the line with a hyphen `- my item`, or a number and dot `1. first item`
- You make text **bold** by using `**double asterisk**` and *italics* with `*one asterisk*`.
- `Highlight` code-related words using `` `back-ticks` `` ,
- Create multi-line code block with three back-ticks. Provide a language after the first backticks to get syntax highlighting:
````md
```python
YOUR CODE HERE
```
````
For example:
```python
a = 1 + 2
print('hello world')
```
- Create [hyperlinks](https://mude.citg.tudelft.nl) with `[text to display](link)`
- Create titles using hashtags `#`. You can use more hashtags `##`, `###` for subtitles.

Many more tips are available here: https://www.markdownguide.org/basic-syntax/

If you are viewing this file inside the book, all the markup has been converted properly. If you download the file and open it in a text-editor, you'll see the raw source code. To make your life easier, there are many tools available to render the markdown live. In VS code, this can be done by clicking 'Open preview to the side' in the toolbar (shortcut `CTRL` + `K` --> `V` ):

![Markdown preview VS code](https://github.com/TUDelft-MUDE/source-files/raw/main/file/markdown_preview.png)

Later on, you'll upload your assignments to GitHub, which by default renders all your markdown files. Please note that there are many different flavours of markdown, so it's best to stick to the main markdown syntax to make sure it's properly formatted wherever the file is opened.

## Formatting Tables in Markdown

This is relatively straightforward, once you learn the proper syntax. Note, however, that the most challenging thing about Markdown tables (and Markdown in general) is that every platform interprets the source code (i.e., the text) differently---in other words, what works in VS Code may not work the same in other IDE's, or even on GitHub. Fortunately this is usually fixed with a little trial-and-error, usually with white space (spaces, new lines, etc) or a quick Google search for some example code.

The following are key notes for constructing a table:
- The essential element is the pipe symbol `|` (the vertical bar), which denotes the column boundaries.
- Each line of code is a new row in the table, which will generate automatically in a Markdown cell as long as you have the same number of pipes in each row.
- The second row is essential, and must contain at least one colon `:` and one hyphen (dash) `-` that tells the Markdown interpreter that you are defining a table (see next comment, and examples).
- You can specify left, center or right justification of text in each column using `:-`, `:-:` or `-:`, respectively. You can also use extra hyphens or whitespace to format the raw text in a readable way.

Below are two example tables to illustrate how it works.

_Table 1: Example table, empty; formatted as source code._

```md
|     |     |     |
| :-: | :-: | :-: |
|     |     |     |
```

_Table 2: Example with left, center, right justification in columns._

| Column 1 | Column 2 | Column 3 |
| :- | :-: | -: |
| Left Justified | Center | Right |
| a | b | c |
| 1 | 2 | 3 |

## Figures

You can also add figures in Markdown, using the following syntax:  `![My image](./imagename.ext)` (where `ext` is any image extension). Here are some examples:
- an image located in the working directory `![My image](./imagename.ext)` (where `ext` is any image extension).
- an image located in a sub-directory called "images": `![My image](./images/imagename.ext)`
- an image with a space in the file name: `![My image](./images/my%20image.png)`
- instead of a local image, you can also reference an image online: `![MUDE logo](https://github.com/TUDelft-MUDE/source-files/raw/main/file/MUDE_Logo-small.png)` gives you the MUDE logo!

When using Markdown to include an image, the square brackets is a text tag that is displayed in case the image does not load. Do not include a dot in the square brackets; i.e., do _not_ do this: `![my image.](./image.svg)`.

As you can create a wider variety of figures in code, we should be able to include them in our accompanying reports for communicating the results of our analyses.

```md
![bar chart of dummy data](./my_bar_chart.svg)
```


## Markdown in Jupyter notebooks

Jupyter notebooks generally consist of code cells and text cells. And the most common formatting for these text cells is again Markdown! All of the above can also be applied in a Jupyter Notebook!

% START-CREDIT
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Robert Lanzafame and Tom van Woudenberg. {ref}`Find out more here <programming_credit>`.
```
% END-CREDIT
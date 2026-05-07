# Version Control

<!-- This git tutorial was originally modified from Kiril and Riccardo's version from 2022-23. It was converted from LaTeX to md with Pandoc. Original PDF is included for reference. -->

In a nutshell, **version control** is a process that is concerned with the management and recording of files on your computer. These tools are primarily focused on text-based files, although for convenience we will also apply them to binary files such as PDF or raster images. While you may be used to backup software such as OneDrive, Dropbox, etc, version control software works a bit differently because of the focus on the text-based content. The chapters in this textbook will give you the information you need to take advantage of a version control software, git, for the programming projects you will work on during your MSc program.

<!-- authors: Kiril Vasilev, Riccardo Taormina, Robert Lanzafame, Tom van Woudenberg. -->

## What is Version Control?


While working on personal or university projects, without a doubt you have come across the following situation: You have finished drafting a report and believe you are done with it and save the file as `report.doc`. However, later you decide to experiment and make some changes, but you still want to keep your old working version, so you make a new file called `report-final.doc`. Now imagine that you send the file to a friend of yours to proofread and make some comments on it and they send it back. Next, you incorporate their feedback and end up naming the new one `report-final-2.doc`.


### Linear version control

What you have been doing is called version control in a linear fashion. Version control systems start with a base version of the document and then record changes you make each step of the way. You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your most recent version, as shown in figure {numref}`intro1`:

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/intro1.png
---
height: 200px
name: intro1
---
Consecutive file changes
```

### Branching version control

Once you think of changes as separate from the document itself, you can then think about branching different sets of changes on the base document, resulting in different versions of that document. For example, two users can make independent sets of changes on the same document, resulting in 2 independent versions ({numref}`intro2`).

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/intro2.png
---
height: 300px
name: intro2
---
Parallel file changes
```

Unless multiple users make changes to the same section of the document - a conflict - you can incorporate two sets of branched changes into the same base document ({numref}`intro3`).

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/intro3.png
---
height: 300px
name: intro3
---
Merge of changes
```

### Comparison

Git as a version control system allows for separate sets of changes to be branched and merged together, as well as providing tools to resolve conflicts when they arise. This is a very different appearance than what you are used to with traditional linear backup software, for example, Microsoft Word auto-save, or cloud-based services like OneDrive and Google Drive. All of these platforms are set up in a user-friendly way that is focused on a single version of a file in every moment in term. This works fine when we are writing a report like a thesis. However, it does **not** work well when it comes to computer programs, because in addition to the files themselves, the contents of the file become critical. As we will see, git is a version control software that allows us to compare and track changes in every character of text within a file, and doing that independent of changes made by others. This is very useful when writing code, as well as working with a distributed team of collaborators.

## File types: text versus binary

Version control systems oriented towards software development and programming are typically focused on **text-based files**: files where the contents are viewable on your computer as human-readable text. **Binary files,** on the other hand, are organized and saved with bits (`0`'s and `1`'s) and are not human-readable. Although this may be a simplified description in terms of the way computers store information (you can read more [here](https://en.wikipedia.org/wiki/Binary_file)), it is enough for our purposes to recognize that text-based files are best suited for use with version control system; in other words, your Python code!

* Examples of common text-based file extensions are: `txt`, `md`, `csv`, `ipynb`, `py`, `html`, etc.
* Examples of common binary files are: `pdf`, `ppt`, `xlsx`, `docx`, etc.

```{exercise}
:nonumber: true

Try exploring a few files on your computer to confirm wether they are text-based or binary by opening them up in a text editor. You will easily be able to distinguish the difference because one is readable, the other not.

Note that in Windows if you are using Notepad (the default), you will want to select  "Word Wrap" under the "Format" menu to fit the contents of very long lines within the visible width of the window.
```

## Git and Github

[Git](https://git-scm.com/) is a version control system , used by a wide variety of engineers and software developers to work on projects in parallel together. It provides multiple benefits such as tracking changes to files, working side by side with other people, and the ability to rollback to previous versions of files without losing track of newer changes. It is a free and open sources software.

Note that while git is free and can be used on a variety of operating systems, there are many 3rd party softwares that _use_ git directly, or are heavily dependent on git. For example, GitHub is a company that provide cloud-based servers for hosting git repositories, as well as additional features like user groups, discussion channels, and even hosting of websites. Furthermore, GitHub provides a free software that is very useful: **GitHub Desktop**! This software allows you to interact in a nice graphical interface with the version control of your files.

## Main concepts and terminology

Here we present a list of the terminology we may use when referring to version control systems. Bear in mind that the list below is not exhaustive, and more terms may show up.

- **Repository:** storage, where the version control system stores their history of changes and information about who made them.
- **Remote repository:** a version control repository stored somewhere else and the changes between the two are usually synchronized. We will refer to the GitHub repository as the *origin*, which could be one of multiple *remotes*.
- **Commit:** Snapshot of the current state of the project. If a commit contains changes to multiple files, all the changes are recorded together.
- **Cloning:** copying (downloading) an existing project on your laptop including the full history and link with the remote repository. Usually, it is done only during the first time of getting the remote repository.
- **Pushing:** uploading new commits (changes) to the remote repository.
- **Fetching:** checking for new changes on the remote repository with respect to your cloned repository.
- **Pulling:** retrieving new commits from the remote repository. To prevent issues, always fetch and pull from the remote repository before starting a work session on your computer.
- **Conflict:** when changes made by multiple users to the same file are incompatible, you can get into a conflict. Helping users resolve those conflicts is one of the key advantages of version control systems.
- **Branch:** development (time) line. The main development line is often called `main`.
- **Merge:** combining the commits of two branches, for example, changes on a development branch are merged into the `main` branch.
- **Fork:** a separate version of someone else's repository on your own GitHub account. You could see this as a branch you own yourself instead of the original owner of the repository. The original repository is generally called *upstream*, which could be added as an additional *remote* to a local repository.
- **Pull request:** proposal on github to merge a branch or fork into another one. This proposal provides a space for feedback.

These terms are best understood by seeing them in action.

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Kiril Vasilev, Riccardo Taormina, Robert Lanzafame, Tom van Woudenberg. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

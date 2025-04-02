# Files and Folders

MUDE has a repetetive weekly workflow and a _lot_ of different technical topics. Because of this, it is important to keep our files well organized. This page gives you the background information to do this efficiently. Your weekly assignments will also guide you through the process of setting this up in a gradual way.

```{tip}
This may be the first time you have ever had to consciously interact with the file system on your computer. If you are used to using software applications like OneDrive on your laptop, the setup required for MUDE may have been done automatically for you in the past. If you work primarily on a tablet or mobile phone, you probably _never_ have to interact with the file system on your device.

If you struggle with file system organization, or would like additional information, do not hesitate to come to weekly question hours and reach out to your MUDE instructors!
```

The _file system_ on a computer is simply a way to organize digital documents. Because it is easily customizable, it can be confirgured in many ways, enabling the computer user to optimize it for their own purposes. For MUDE, it is useful to define a few key concepts:

- **files**: the digital documents on our computers.
- **folders**: the way we organize the **files** on our computer. It is possible to have **folders** inside other **folders**. 
- **directory**: a hierarchical structure for organizing data on a computer. For our purposes, it is synonymous with **folder**.
- **sub-directory**: for our purposes, this is a folder within another folder.
- **top level directory** or **root directory**: the highest level in the directory structure. Note that this is a relative term; if we are considering only the scope of MUDE documents, perhaps the `MUDE` directory is the top level, even though it is also a sub-directory itself.
- **lower level directories**: this term refers to travelling "downward" through the hierarchical tree of the directory system
- **working directory**: the place where we will edit files when working on a particular project.


The concept of a **working directory** is especially important, as it is the primary place where we "do work." This includes everything from writing reports, writing and running code and programs, processing data, creating visualizations, etc. Ideally this directory is set up to include all relevant files for a particular project, such that when you are "doing work" you can ignore the rest of the file system on your computer. This has important practical implications, for example:
- you can open your IDE in the working directory and have access to all the files you need
- it is easy to back up (save) your work and share it with others

The goal of this page is thus to give you _just enough_ information to be able to confidently set up and understand working directories on your computer.

```{tip}
Some of the content on this page describes the software Git and a related concept of _repository._ If you are unfamiliar with these concepts, you can ignore them for now and consider a _repository_ to be equivalent to a _directory_ of _sub-directory._
```

## Your Local File System

You will be working with a _lot_ of different files and file types in MUDE: `csv`, `pdf`, `ipynb`, `txt`, `md` just to name a few. Remember, there are 16 weeks of class in MUDE---it is good practice to get in the habit of storing files in an organized way, not to mention make it easier to study for the exams. We recommended creating a folder `MUDE` to collect all files associated with the module, then set up a new folder for each week and each project as your **working directory** for each of those activities. This is where you will download files and edit them when working on them. 

```{admonition} File Types and Extensions
:class: tip, dropdown
File types are typically defined by their "extension," which is the set of letters that appears after the name of a file, separated by a dot. If you can't see these in the file explorer on your OS, you need to change your view settings to be able to see them. We often use the convention of a `*` to denote the arbitrary file name, for example `*.csv` is a generic `csv` file. If this is a foreign concept to you, just note for now that extensions make it easier for computer software to find files and decide what to do with them. 
```

```none
├── MUDE                           <-- a root directory for MUDE projects
    ├── Project_1                  <-- project files in sub-directories
        ├── Assignment_File.ipynb  <-- stay organized with more sub-directories
        ├── auxiliary_files
            ├── data.csv
            ├── figure.png
            ├── ...
    ├── Project_2                  <-- another working directory
        ├── ...
    ├── Project_3                  <-- each of these should be it's own repository
        ├── ...
    ├── Project_4
        ├── ...
```

As you can see, we have included a directory `auxiliary_files` in the directory for Week 1. This is a generic setup to help keep the weekly folders from getting too cluttered: as our MUDE projects become more complex, we may want to use a variety of sub-folders to organize our files (e.g., data, code, figures, etc).

```{tip}
If you have not yet learned about the software Git, or its command line invocation `git`, it is enough to know that it is a _version control system_ that focuses on tracking changes to files and collaborating with others. It is software that can run on many OS's and is integrated into other tools provided by 3rd party companies that add additional features, for example, a way to backup and collaborate in the cloud. Widely used examples of these companies are GitHub and GitLab.
```

The organization of your `MUDE` and working directories can vary widely due to the types of projects and your personal preferences. Your _version control_ system may also dictate the structure. For example, in a course where you will have multiple repositories per week (e.g., CEGM1000 MUDE), you might consider organizing these `git` repositories in sub-directories, like this:

```none
├── MUDE
    ├── Week_A
        ├── git_repo_for_project_1
            ├── Assignment_File.ipynb
            ├── auxiliary_files
                ├── data.csv
                ├── figure.png
                ├── ...
        ├── git_repo_for_project_2
            ├── ...
    ├── Week_B
        ├── git_repo_for_project_3
            ├── ...
        ├── git_repo_for_project_4
            ├── ...
    ├── Week_C
        ├── ...
    ├── Week_D
        ├── ...
```

```{tip}
If you are not yet working with Git or another version control system, it is OK to back up your work using a cloud-based software like OneDrive. However, note that this can sometimes lead to issues when running code and programs, so you may occasionally need to move the files elsewhere when working. As soon as you are comfortable with a tool like Git, we encourage you to **stop** using cloud-based software to back up your working directories; instead you can use a tool like GitLab (we will show you how in MUDE).

This is additionally explained in a section below.
```

## A Typical MUDE Working Directory

Within each **working directory** you will collect a wide variety of files. It is important to keep these well organized so that when you return to work on a project in the future, it is easy to pick up where you left off. As a preview of the types of analyses we will do, a typical MUDE working directory is illustrated in the figure below. Note in particular that it contains several file types, along with a few sub-directories for organizing content. The files that are edited directly (e.g., the Analysis or Report files) are included in the top level directory. In addition, a README file is included to provide general information about the working directory and its contents.

```{figure} https://files.mude.citg.tudelft.nl/working_dir.svg
---
width: 40%
name: working_dir
---
Contents and organization of a typical working directory in MUDE. Note the various file types, and how the files that are actively edited are located in the top level directory, whereas files that remain mostly static, or are produced as a result of running a program (i.e., figures) are in the sub-directories.
```

```{tip}
Markdown is a text-based file format that is used to easily make nicely formatted documents. We will use it to write Reports summarizing our analysis and findings. You can think of it like a (very!) simple alternative to LaTeX.
```

## Saving Your Work

It is important to keep a backup of your work, and to save these files in a consistent way. Your typical cloud-based backup software is OK for many types of files, but you should note that sometimes there can be issues when running code on your compter in these special sync folders. Imagine: your Python code is running and loading or saving data into files in the same folders that the cloud backup software is using: there are bound to be conflicts!

Over the course of the semester we will gradually increase our reliance on `git` and GitLab, a widely used set of tools meant to store, track and archive files. As you become more comfortable with this tool, you will learn to `git push` more and rely on your cloud storage system less! In summary:
* for now, we recommend you store everything in a location that is backed-up regularly, but keep code and data files in a separate folder. If your backup software causes issues with notebooks or other Python code, move the working directory temporarily to another location on your computer.
* once you are comfortable with `git`, we recommend that you permanently move your code folder somewhere that is not backed up by cloud software and use your GitLab repository instead.

In case the text above was not clear: to avoid syncing problems, use a system like `git` to backup code, _not_ a cloud service like OneDrive!

(cli)=
# Command line interface

A _command line interface_ (CLI) is a method of interacting with a computer that involves individual lines of text. These so-called _command lines_ can be entered manually by the user, as well as written in a text-based file and passed on to a computer or application for automatic entry and execution. The alternative to a CLI is a _graphical user interface_ (GUI).

A few of the main reasons for using a CLI in engineering work are:

- rudimentary tasks are easily automated and repeated (e.g., copying, moving, renaming files and folders)
- some software does not have a GUI
- a CLI can easily be opened on any modern laptop and can be much faster than using a GUI

For example, once you can use the CLI you will probably find it much easier than using a GUI to navigate to a working directory on your computer, create and activate a computing environment for your project and open and begin working in your chosen IDE.

There is a long history of CLI's and many different types; a brief overview and set of examples are provided on this page.

## Definitions and terms

There are various terms to be aware of, but we will only give a brief explanation here (see [this tutorial](https://www.tutorialspoint.com/difference-between-terminal-console-shell-and-command-line#:~:text=To%20summarize%2C%20a%20terminal%20is,textual%20commands%20into%20the%20shell.) for a more detailed explanation):

- **Terminal**: a piece of hardware for entering data into a computer. How we did it in the "old days" (the [Wikipedia page](https://en.wikipedia.org/wiki/Computer_terminal) has a few examples).
- **Console**: similar to a terminal, but adds hardware, interaction and a few other things (if you want to understand the difference, [try reading this](https://en.wikipedia.org/wiki/Computer_terminal#System_console))
- **Shell**: an application that allows a user to write commands and enter data that can be translated into commands and data that can be executed by the operating system and hardware on a given computer; in short, this is how your instructions can be interpreted by any computer, regardless of hardware or operating system. A shell generally has two methods for interaction, a _graphical user interface_ (GUI) or a _command line interface_ (CLI).
- **Command line interface**: a method of interacting with a computer that involves typing lines of text into an interface; modern CLI's are implemented in shell applications. Visit the [CLI Wikipedia page](https://en.wikipedia.org/wiki/Command-line_interface) for an exhaustive overview of CLI's.

Now that these have been defined, you might realize that most of your life you have probably used a GUI to interact with your computer (remember, your mobile phone is also a computer!). This page is about using the alternative shell interface: a CLI!

You will hear many people and see software that use the terms above interchangeably (for example, VS Code uses the term "terminal" for all CLI's), but in reality usage of the term _terminal_ or _console_ today generally refers to a _shell_ with a _CLI._ We recommend sticking to the term **command line interface (CLI)**, or simple the **command line** as this is platform independent and captures what we are physically doing with regards to the content in this book: entering and executing commands via a CLI.

## Examples of CLI

There are many types of modern CLI's that you may come across, here is a short list to give you an idea of their names and a few observations about each one:

- **Terminal**: the standard CLI on a Mac OS
- **Command Prompt**: one of several CLI's commonly used on Windows OS
- **PowerShell**: one of several CLI's commonly used on Windows OS. Notorious for having a syntax and set of commands that is different from most other CLI's (we recommend you avoid this one, if possible)
- **Anaconda Prompt**/**Conda Prompt**: a custom CLI that builds on other CLI's. For example, on Windows OS you can find a Command Prompt and PowerShell versions, depending on your preference
- **Bash**: widely used on Linux systems
- **Git Bash**: a CLI that comes with the Git software distribution that is the easiest way to get Unix style commands on a Windows OS

### Unix

Many CLI's use _UNIX style syntax and commands._ UNIX is a family of operating systems that were developed in the 1970's and influenced many other computer OS's.

Mac and Linux OS's use UNIX style commands, but unfortunately the CLI's'that are available by default on Windows OS do not. This can make it more difficult to use the CLI for Windows users, especially because the vast majority of online documentation and open source CLI tools available today use UNIX-like syntax and commands.

It is easy to work around this issue, however, for example:

- it is easy to find the equivalent commands between UNIX and Windows CLI's (once you are aware that there is a difference)
- it is possible to get UNIX style CLI's on Windows OS (e.g., Git Bash)

## Basic CLI commands

The table below will give you commonly used commands on Mac and Windows OS's

% Isabel has tested all the Mac commands on MacBook Pro M1 - 3 September

||UNIX-style shell (Linux / Git Bash / macOS Terminal)|Windows (Command prompt / conda prompt)|
|---|---|---|
|Present working directory|`pwd`|`cd`|
|List content of the present working directory|`ls`|`dir`|
|Change directory|`cd /path/to/directory`|`cd C:\path\to\directory`|
|Clear terminal|`clear`|`cls`|
|Quit paged output |`q`|`q`|
|Stop a running command|`Ctrl`+`C`|`Ctrl`+`C`|

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Robert Lanzafame and Tom van Woudenberg. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

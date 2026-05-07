(cli)=
# Command Line Interface

A _Command Line Interface_ (CLI) is a method of interacting with a computer that involves individual lines of text. These so-called _command lines_ can be entered manually by the user, as well as written in a text-based file and passed on to a computer or application for automatic entry and execution. The alternative to a CLI is a _Graphical User Interface_ (GUI).

```{admonition} Why use a CLI?
:class: tip

A few of the main reasons for using a CLI in engineering work are:
- rudimentary tasks are easily automated and repeated (e.g., copying, moving, renaming files and folders)
- some software does not have a GUI
- a CLI can easily be opened on any modern laptop and can be much faster than using a GUI

For example, once you can use the CLI you will probably find it much easier than using a GUI to navigate to a working directory on your computer, create and activate a computing environment for your project and open and begin working in your chosen IDE.
```

There is a long history of CLI's and many different types; a brief overview and set of examples are provided on this page.

## Definitions and Terms

There are various terms to be aware of, but we will only give a brief explanation here (see [this tutorial](https://www.tutorialspoint.com/difference-between-terminal-console-shell-and-command-line#:~:text=To%20summarize%2C%20a%20terminal%20is,textual%20commands%20into%20the%20shell.) for a more detailed explanation):

- **Terminal**: a piece of hardware for entering data into a computer. How we did it in the "old days" (the [Wikipedia page](https://en.wikipedia.org/wiki/Computer_terminal) has a few examples).
- **Console**: similar to a terminal, but adds hardware, interaction and a few other things (if you want to understand the difference, [try reading this](https://en.wikipedia.org/wiki/Computer_terminal#System_console))
- **Shell**: an application that allows a user to write commands and enter data that can be translated into commands and data that can be executed by the operating system and hardware on a given computer; in short, this is how your instructions can be interpreted by any computer, regardless of hardware or operating system. A shell generally has two methods for interaction, a _graphical user interface_ (GUI) or a _command line interface_ (CLI).
- **Command Line Interface**: a method of interacting with a computer that involves typing lines of text into an interface; modern CLI's are implemented in shell applications. Visit the [CLI Wikipedia page](https://en.wikipedia.org/wiki/Command-line_interface) for an exhaustive overview of CLI's.

Now that these have been defined, you might realize that most of your life you have probably used a GUI to interact with your computer (remember, your mobile phone is also a computer!). This page is about using the alternative shell interface: a CLI!

You will hear many people and see software that use the terms above interchangeably (for example, VS Code uses the term "terminal" for all CLI's), but in reality usage of the term _terminal_ or _console_ today generally refers to a _shell_ with a _CLI._ We recommend sticking to the term **command line interface (CLI)**, or simple the **command line** as this is platform independent and captures what we are physically doing with regards to the content in this book: entering and executing commands via a CLI.

## Examples of CLI

There are many types of modern CLI's that you may come across, here is a short list to give you an idea of their names and a few observations about each one:

- **Terminal**: the standard CLI on a Mac OS
- **Command Prompt**: one of several CLI's commonly used on Windows OS
- **PowerShell**: one of several CLI's commonly used on Windows OS. Notorious for having a syntax and set of commands that is different from most other CLI's (we recommend you avoid this one, if possible)
- **Anaconda Prompt**: a custom CLI that builds on other CLI's. For example, on Windows OS you can find a Command Prompt and PowerShell versions, depending on your preference
- **Bash**: widely used on Linux systems
- **Git Bash**: a CLI that comes with the Git software distribution that is the easiest way to get Unix style commands on a Windows OS



```{tip}
Many CLI's use _UNIX style syntax and commands._ UNIX is a family of operating systems that were developed in the 1970's and influenced many other computer OS's.

Mac and Linux OS's use UNIX style commands, but unfortunately the CLI's'that are available by default on Windows OS do not. This can make it more difficult to use the CLI for Windows users, especially because the vast majority of online documentation and open source CLI tools available today use UNIX-like syntax and commands.

It is easy to work around this issue, however, for example:
- it is easy to find the equivalent commands between UNIX and Windows CLI's _once you are aware that there is a difference) (see examples below)
- it is possible to get UNIX style CLI's on Windows OS (e.g., Git Bash)
```

## Basic CLI Skills: Cheat Sheets

The tables below will give you commonly used commands on Mac and Windows OS's

```{note}
We've only included the Powershell commands here. However, the Windows Command Prompt (cmd) is also very easy to use. You can use the descriptors in the tables below to help with a web search or AI prompt, for example: _list directory contents windows command prompt._
```

% Isabel has tested all the Mac commands on MacBook Pro M1 - 3 September

|  | Mac (UNIX Style commands)  | Windows (Powershell)   |
|--|----------|-------------|
|    Present Working Directory  | `pwd`      | `pwd` |
| List content of the present working directory | `ls`        |  `ls`   |
| Change: Change Directory | `cd /path/to/directory` | `cd /path/to/directory`  |
|   Touch: Creates a new file or updates the timestamp  | touch {filename} (`touch my_file.txt`) | touch {filename} (`touch my_file.txt`)|
| Create new directory  | mkdir {directory_name} (`mkdir my_folder`)  | mkdir {directory_name} (`mkdir my_folder`)   |
| Copy: Copies file or directory | cp {source} {target} (`cp my_file.txt my_folder`)| cp {source}  { target} (`cp my_file.txt my_folder`)|
| Moves a file or directory| mv {source} {target} (`mv my_file.txt my_folder`)| mv {source} {target} (`mv my_file.txt my_folder`)|
| Removes: Removes file |  rm {filename} (`rm my_file.txt`) |  rm {filename} (`rm my_file.txt`)|
| Removes: Removes directory|  rmdir {directory_name} (`rmdir my_folder`) |  rmdir {directory_name}  (`rmdir my_folder`) |
| Clear up terminal | `clear` | `clear` |

%below some simple CL to run python from terminal. Perhaps this can go to the python section
**Python**
|  | Mac (UNIX Style commands)  | Windows (Powershell)     |
|--|----------|-------------|
|  Verifying and version  | `python3 --version` | `py -3 --version` |
| Opening Python shell | `python3`    |  `py3`   |
| run python files | python3 {py_file_name} `python3 filename.py` | py3 {py_file_name} `py3 filename.py`|
|Open python file in VS Code| code {py_file_name} `code filename.py` | code {py_file_name} `code filename.py` |

```{tip}
Depending on your computer settings, you may need to use `python` or `python3` to call the interpreter. Usually one or the other words by default on Mac, as it comes pre-installed with Python. For Windows OS, we recommend you use the Anaconda Command Prompt, as it was installed along with Python, which should be findable as long as you added `conda.exe` to your `PATH` environment variable.
```

<!-- Add the code command for opening Python file in VS Code. Open palette `Cmd +Shift + p`  (`<Shell Command: Install 'code' command in PATH> `) -->

<!-- `exit` leaves the CLI -->

## Links to other Cheat Sheets

Here are links for more detailed command line cheat sheets:

- [Windows command line cheat sheet](https://gist.github.com/hofmannsven/8392477) 
- [Mac Terminal command line cheat sheet](https://github.com/0nn0/terminal-mac-cheatsheet)

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Robert Lanzafame. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

# Files and folders

How to work with files and folders is a fundamental skill which many of you have probably been doing for years without even thinking about it. However, when dealing with coding, this may be the first time you have ever had to consciously interact with the file system on your computer. If you are used to opening single file using software applications like OneDrive on your laptop, you don't have to interact with the file system directly. However, when working with code, you will often need to navigate and manipulate files and folders programmatically. If you work primarily on a tablet or mobile phone, you probably _never_ have to interact with the file system on your device.

The _file system_ on a computer is simply a way to organize digital documents. Because it is easily customizable, it can be configured in many ways, enabling the computer user to optimize it for their own purposes. It is useful to define a few key concepts:

- **files**: the digital documents on our computers.
- **folders**: the way we organize the **files** on our computer. It is possible to have **folders** inside other **folders**. 
- **directory**: a hierarchical structure for organizing data on a computer. For our purposes, it is synonymous with **folder**.
- **sub-directory**: for our purposes, this is a folder within another folder.
- **top level directory** or **root directory**: the highest level in the directory structure. Note that this is a relative term; if we are considering only the scope of MUDE documents, perhaps a `MUDE` directory is the top level, even though it is also a sub-directory itself.
- **lower level directories**: this term refers to travelling "downward" through the hierarchical tree of the directory system
- **working directory**: the place where we will edit files when working on a particular project.

The concept of a **working directory** is especially important, as it is the primary place where we "do work." This includes everything from writing reports, writing and running code and programs, processing data, creating visualizations, etc. Ideally this directory is set up to include all relevant files for a particular project, such that when you are "doing work" you can ignore the rest of the file system on your computer. This has important practical implications, for example:

- you can open your editor in the working directory and have access to all the files you need
- it is easy to back up (save) your work and share it with others

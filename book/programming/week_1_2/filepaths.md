# File Paths

A _file path_ is like an address to a file. There are generally two types, _absolute_ and _relative._ Most of our activities focus on working in a  _working directory,_ so we will focus almost entirely on relative paths. The general format is like this:

```
./subdirectory_1/subdir_2/filename.ext
```

where:
- the dot `.` indicates one should use the current directory of the file (or the CLI) as the current location (the `.` is like saying " start _here_")
- forward slashes `/` separate subdirectories
- the last two words are the file name and extension. For example, common image extensions are `.jpg`, `.png` or `.svg`
- in this example, the image file is stored inside a folder called `subdir_2` which is inside a folder called `subdirectory_1` which is in our working directory.
- Do not include spaces in your file path or file names; if it is unavoidable replace the space with `%20`, for example: `![My image](./my%20image.png)`

As a general rule, **always use forward slashes whenever possible.** Although backward slashes are the default and must be used at times on Windows, they don't work on Mac or Linux systems. This causes problems when sharing code with others running these systems. Remember that we try to do things in a way that allows easy collaboration: using approaches that are agnostic of the operating system (i.e., works on all platforms). This is hard to guarantee in practice, but consistently using forward slashes will get us close!

% START-CREDIT
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Robert Lanzafame and Tom van Woudenberg. {ref}`Find out more here <programming_credit>`.
```
% END-CREDIT
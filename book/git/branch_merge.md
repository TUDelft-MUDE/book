# Branching and Merging

A key feature of git is the ability to create and manage multiple version called branches, allowing you to work on different versions of your code simultaneously. Usually, the primary version is called main. In practice when collaborating with Git, everyone will work on a separate branch, whose progress you will later merge with main.

Commits (the 'states' or 'saves' of your files) in git have a graph structure, where every node is a commit and edges represent the transition (flow) between commits. "HEAD" points to the current commit that you're looking at. When you switch between branches, you can think of HEAD as the most recent commit on that branch.

The graph below shows the commit history of a repo with two commits. Head is shown with the rectangular commit node, while the other commit is shown with a circular node.:

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/simple_git_history.png
---
source: https://github.com/TUDelft-MUDE/source-files/raw/main/file/simple_git_history.mmd
---
Commit graph of a simple repository
```

The main advantage of version control is that it allows developers to work together in parallel. During projects, you will be working on "feature" branches and separating the work to review and merge it later. A common graphical structure of commits is shown below, where we have developers working on 3 separate branches and merging their work when necessary. This separation offers flexibility, parallelization of work, and offers more control over the development process.

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/complex-mermaid-diagram.png
---
source: https://github.com/TUDelft-MUDE/source-files/raw/main/file/complex-mermaid-diagram.mmd
---
Commit graph of a complex repository
```

In the commit graph above you see three branches (`main`, `dev` and `dev2`). The `HEAD` is at the commit `Restructure content`, so if you're looking at the files in repository, you see the stated of all the files after that commit. E.g. the changes from `Updated README`, `Added new feature` and `Merge dev into dev2` are not visible. So it's not only possible to change branch, but also to go back in time with `head`!

The `dev branch` was created from the state of the `main` branch at `initial commit` and after two commits `Added new feature` and `Fixed new features`, the changes from `Restructure content` and `Update README` have been merged into that branch in commit `Merge main into dev`.

The `dev2` branch was created from the state of `main` at `Updated README`, while after one commit `Added another new feature`, the changes from `dev` brnach were included into the `dev2` branch with commit `merge dev into dev 2`. After that, it is merged into `main` at `merge dev2 into main`, effectively merging the `dev` into `main`.

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Kiril Vasilev, Riccardo Taormina, Robert Lanzafame, Tom van Woudenberg. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

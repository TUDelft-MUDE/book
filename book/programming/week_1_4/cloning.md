## Cloning

Cloning is much more than just downloading! It is the process of duplicating not only the files, but also the record of all changes that have been made to those files in the past (that's what the git software is doing!). Because the history of these files is preserved, even if we make changes to these files in one of the repositories, the git software will provide a way to update the other software some time in the future. This allows multiple people to work on the same files at the same time; or, you as an individual to work on the same files using several different computers (e.g., a work and home laptop).

Creating several a clone of a repository allows us to also provide a backup of our files (and their history) in case we lose access to the originals (perhaps your computer breaks, or is stolen). It is a great idea to have a copy of the repository in the cloud, which automatically provides a very reliable file storage location. This is one of the key services that companies like GitHub provide. 

In practice we refer to the repository stored on our computer as the **local repository.** This is where we typically spend most of our time working on our code, debugging it and running analysis. It is where you will be spending most of your time working on your MUDE assignments.

The repository on GitHub is our **remote repository.** This can be considered the backup of the files in our repository. When working with multiple people, it can also be considered the most current version of the project. For example, you may be working on improving the plots in your assignment, whereas a colleague is updating the Python script running your model. You will use the _local repository_ to develop your particular task, and the _remote repository_ to collect everyone elses work and deploy it to your local computer (if you need to use it there).

% START-CREDIT
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Robert Lanzafame and Tom van Woudenberg and uses content from  _Learn Programming for Engineers_ {cite:p}`learn-programming` is used. {ref}`Find out more here <programming_credit>`.
```
% END-CREDIT
# Merge conflicts

Merge conflicts arise when people on separate branches modify the same parts of one (or multiple) files. Since Git does not know how to handle that and whose changes to consider, it prompts the user to decide instead.

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/mconflict1.png
---
height: 300px
---
Visualization of a merge conflict
```

Git and GitHub assist you in solving these conflicts, as seen in the figure below:

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/mconflict3.png
---
height: 400px
---
Merge conflict
```

In this situatie, it is attempted to merge main in a conflicting branch. The conflicting lines on the main branches are preceded by `<<<<<<< main`, while the changes from the conflicted `main` branch are preceded by `=======` and followed by `>>>>>>> conflicting-instructions`. To fix this conflict, we need to open the file in an editor and resolve the conflict by keeping the desired changes and removing the unnecessary parts. Once done, we can commit the resolved changes. Note that the current branch is now in a "MERGING" state. We have decided to take the best out of the two branches and merge their changes.

## Why merge into the conflicting branch first?

Merging the main branch into the conflicting branch first allows you to resolve conflicts in a controlled environment. After that you can thoroughly test the merged changes in the conflicting branch before integrating them into the main branch, reducing the risk of introducing bugs.

## Collaborating with branches

When working together on a single branch (so in the same version), it is important to coordinate with your team to avoid conflicts and ensure smooth collaboration. Here are some best practices:

- Keep in touch with your team about who is working on what.
- Frequently pull the latest changes to keep your local branch up to date. This helps in minimizing conflicts.
- Make small, frequent commits with clear messages. This makes it easier to track changes and resolve conflicts.
- If conflicts arise, communicate with your team directly to resolve them before proceeding.

## Why notebooks causes conflicts all the time

Yeah, this is really annoying. The JSON structure of a notebook causes the issue, as explained [here](./notebooks.ipynb).

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Kiril Vasilev, Riccardo Taormina, Robert Lanzafame, Tom van Woudenberg. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

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
copyright: © 2018-2024 The Carpentries
license: CC BY 4.0
placement: margin
show: license, copyright
---
Merge conflict
```

In this situatie, it is attempted to merge main in a conflicting branch. The conflicting lines on the main branches are preceded by `<<<<<<< main`, while the changes from the conflicted `main` branch are preceded by `=======` and followed by `>>>>>>> conflicting-instructions`. To fix this conflict, we need to open the file in an editor and resolve the conflict by keeping the desired changes and removing the unnecessary parts. Once done, we can commit the resolved changes. Note that the current branch is now in a "MERGING" state. We have decided to take the best out of the two branches and merge their changes.

## Why merge into the conflicting branch first?

Merging the main branch into the conflicting branch first allows you to resolve conflicts in a controlled environment. After that you can thoroughly test the merged changes in the conflicting branch before integrating them into the main branch, reducing the risk of introducing bugs.

``````{exercise}
:nonumber: true

Given is the following file `poem.md` which is stored in the 'main' branch of your repository:

```md
Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.
```

You and your friend want to improve this poem.

:::::{grid} 1 2 2 2

::::{grid-item}
:columns: 12 12 6 6

You edit the file in your new branch 'Q2':

```md
Roses are red,
Violets are blue,
Sugar is sweet,
Glad I made Q1 through.
```

::::

::::{grid-item}
:columns: 12 12 6 6

Your friend edits the file in his branch 'love':

```md
Roses are red,
Violets are blue,
Sugar is sweet,
And my love for MUDE is true.
```

::::

:::::

:::{question}
:type: no-input
:nocaption:
:showanswer:

What would happen when you merge the branch 'love' from your friend?
---
= The fourth line in the 'main' branch of your repository will be replaced with the new line from your friend
---
:::

:::{question}
:type: no-input
:nocaption:
:showanswer:

What would happen when you merge your branch 'Q2' into 'main' after merging the branch 'love' from your friend? Why does that happen? How do you solve that?
---
= A merge conflict arises because now there are two conflicting changes for the fourth line of the poem. Git will not know which change to keep and will mark the conflict in the file.

To fix this conflict, you will have to open the file and manually edit the fourth line to keep the change you want.
---
:::

:::{question}
:type: no-input
:nocaption:
:showanswer:

As instead of merging 'Q2' into 'main', after merging the branch 'love' from your friend, you first merge 'main' into 'Q2', what would happen when you merge 'Q2' into main? How would that be different from the previous question?
---
= You will still have a merge conflict, but now you will have already resolved the conflict in 'Q2'. If this would have been code, you could have tested the resolved conflict. Therefore, when you merge 'Q2' into 'main', you can be confident that the changes are correct and won't introduce bugs.
---
:::

``````

## Collaborating with branches

When working together on a single branch (so in the same version), it is important to coordinate with your team to avoid conflicts and ensure smooth collaboration. Here are some best practices:

- Keep in touch with your team about who is working on what.
- Frequently pull the latest changes to keep your local branch up to date. This helps in minimizing conflicts.
- Make small, frequent commits with clear messages. This makes it easier to track changes and resolve conflicts.
- If conflicts arise, communicate with your team directly to resolve them before proceeding.

```{admonition} Why notebooks causes conflicts all the time
:class: danger

Yeah, this is really annoying. The JSON structure of a notebook causes the issue, as explained [here](./notebooks.ipynb).
```

% START-CREDIT
% source: finite_element_method
```{attributiongrey} Attribution
:class: attribution
This chapter reuses material from _Learn Programming for Engineers_ and was written by Kiril Vasilev, Riccardo Taormina, Robert Lanzafame, Tom van Woudenberg. {ref}`Find out more here <programming_credit>`
```
% END-CREDIT

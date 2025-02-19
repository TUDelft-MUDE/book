(oop)=
# Week 1.7: OOP

This chapter contains a lot of information that is useful for improving your programming skills, however you are not required to learn all of it, and not required to memorize everything for the exam.

You should be able to understand the fundamental concepts of classes and object-oriented programming (OOP) in Python as well as the key principles of encapsulation, inheritance, and polymorphism in OOP, which will enable you to better understand and use the classes that are everywhere in Python packages. For example, the class `rv_continuous` in `scipy.stats`, which is used for defining probability distributions, are used heavily in MUDE!

One way to check if you understand this material sufficiently: by the end of Week 1.7 you should realize why OOP is so useful for the continuous parametric distributions we use. For example, recognizing that all distributions can be defined and used in the same way. For example:
- methods like `.pdf()` and `.cdf()` can be used predictably
- you can easily define distributions in terms of parameters or moments
- fitting distributions is also straightforward

For non-probability topics, this will help you recognize why objects in Python packages like Numpy have syntax like `object.mean()` or `object.shape`.

We hope you enjoy this eye-opening experience!

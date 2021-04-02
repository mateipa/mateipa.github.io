---
layout: post
title: UQ course at HM
date: 2021-04-01
---

During this summer, I am teaching [_Fundamentals of Uncertainty Quantification (UQ)_](https://zpa.cs.hm.edu/public/module/374/) in a course for Bachelor students at the [Department of Computer Science and Mathematics](https://www.cs.hm.edu/) (FK07) of the [University of Applied Sciences Munich](https://www.hm.edu/) (HM).

At most schools, classes on UQ are only part of Master's programs since they require decent knowledge of and education in various mathematical (linear algebra, calculus, probability theory, statistics, ...) and computer science (programming, algorithms, data structures, ...) subdisciplines.

However, we decided to offer a Bachelor's course that introduces fundamental (as opposed to advanced) aspects of the field.
The introductory classes discuss motivating examples of why UQ actually matters and tries to give a reasonable overview of the field and a fair description of the notion _uncertainty_.
In a second chapter, we lay the basis for forthcoming contents, i.e., we repeat fundamental and necessary definitions and results of probability theory and statistics.
Basic random number sampling, Monte Carlo-type methods along with more advanced _Latin Hypercube Sampling_ (LHS) is explained in chapter 3.
The final and main part of the course is chapter 4 in which we introduce techniques for _global sensitivity analysis_ of mathematical models.
A table of contents and the models used for demonstration are placed below this text.

Besides discussing the contents in a formal way, students can get their hands on some assignments as part of their practical training.
They implement methods from chapter 4 and test them on the SEIR model, a compartmental model from epidemiology for the spread of infectious diseases.

Other more advanced but common UQ approaches as _Forward UQ_ or _Inverse UQ_ are not discussed in this course.
They could be part of courses UQ II or UQ III which then, however, would be better suited as part of a Master's program.

I am very happy to get the opportunity from FK07 and HM to teach this course which is actually quite related to topics of my dissertation.
Having influence on young people and educating them to critically think about underlying assumptions and their consequences from a formal, informal, and intuitive perspective gives me great pleasure and fulfills me.

**Table of contents**:
1. **Introduction**  
  1.1. Motivation  
  1.2. Types and sources of uncertainties
2. **Fundamentals in probability theory and statistics**  
  2.1. Random variables  
  2.2. Expectation value and (co)variance  
  2.3. Quantiles  
  2.4. Important distributions  
  2.5. Statistical estimators
3. **Sampling strategies**  
  3.1. Pseudo-random number sampling  
  3.2. Monte Carlo simulations  
  3.3. Latin Hypercube Sampling (LHS)  
4. **Global sensitivity analysis**  
  4.1. Primitive approach  
  4.2. Partial rank correlation coefficients  
  4.3. Sobol indices

**Models**:
* Predator-prey model
* Compartment model from epidemiology


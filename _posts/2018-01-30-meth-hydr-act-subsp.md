---
layout: article
title: "Preprint: Efficient parameter estimation for a methane hydrate model with active subspaces"
article_link: "https://arxiv.org/abs/1801.09499"
thumbnail: /assets/images/thumbnail-meth-hydr-act-subsp.png
abstract: "Methane gas hydrates have increasingly become a topic of interest because of their potential as a future energy resource. There are significant economical and environmental risks associated with extraction from hydrate reservoirs, so a variety of multiphysics models have been developed to analyze prospective risks and benefits. These models generally have a large number of empirical parameters which are not known a priori. Traditional optimization-based parameter estimation frameworks may be ill-posed or computationally prohibitive. Bayesian inference methods have increasingly been found effective for estimating parameters in complex geophysical systems. These methods often are not viable in cases of computationally expensive models and high-dimensional parameter spaces. Recently, methods have been developed to effectively reduce the dimension of Bayesian inverse problems by identifying low-dimensional structures that are most informed by data. Active subspaces is one of the most generally applicable methods of performing this dimension reduction. In this paper, Bayesian inference of the parameters of a state-of-the-art mathematical model for methane hydrates based on experimental data from a triaxial compression test with gas hydrate-bearing sand is performed in an efficient way by utilizing active subspaces. Active subspaces are used to identify low-dimensional structure in the parameter space which is exploited by generating a cheap regression-based surrogate model and implementing a modified Markov chain Monte Carlo algorithm. Posterior densities that are consistent with the experimental data are approximated in a computationally efficient way."
---

Yeah, my first preprint is available [here](https://arxiv.org/abs/1801.09499)!

[Steven Mattis](https://www-m2.ma.tum.de/bin/view/Allgemeines/StevenMattis), [Shubhangi Gupta](https://www.geomar.de/en/mitarbeiter/fb2/mg/sgupta/), [Christian Deusner](https://www.geomar.de/mitarbeiter/fb2/mg/cdeusner/), my supervisor [Barbara Wohlmuth](https://www-m2.ma.tum.de/bin/view/M2/Allgemeines/ProfessorWohlmuth), and me wrote an article on how to efficiently estimate parameters of a [methane hydrate](https://en.wikipedia.org/wiki/Methane_clathrate) model with [active subspaces](http://activesubspaces.org).

_Active subspaces_ is a recent technique for dimension reduction I am interested in. In the article, we test the capabilities of this method on a "real world problem" from marine biochemistry.


---
layout: article
title: "Preprint: Log-Gaussian processes for AI-assisted TAS experiments"
article_link: "https://arxiv.org/abs/2209.00980"
thumbnail: /assets/images/thumbnail-ariane-prepr.png
abstract: "To understand the origins of materials properties, neutron scattering
experiments at three-axes spectrometers (TAS) investigate magnetic and lattice
excitations in a sample by measuring intensity distributions in its momentum
(Q) and energy (E) space. The high demand and limited availability of beam time
for TAS experiments however raise the natural question whether we can improve
their efficiency or make better use of the experimenter's time. In fact, using
TAS, there are a number of scientific questions that require searching for
signals of interest in a particular region of Q-E space, but when done
manually, it is time consuming and inefficient since the measurement points may
be placed in uninformative regions such as the background. Active learning is a
promising general machine learning approach that allows to iteratively detect
informative regions of signal autonomously, i.e., without human interference,
thus avoiding unnecessary measurements and speeding up the experiment. In
addition, the autonomous mode allows experimenters to focus on other relevant
tasks in the meantime. The approach that we describe in this article exploits
log-Gaussian processes which, due to the log transformation, have the largest
approximation uncertainties in regions of signal. Maximizing uncertainty as an
acquisition function hence directly yields locations for informative
measurements. We demonstrate the benefits of our approach on outcomes of a real
neutron experiment at the thermal TAS EIGER (PSI) as well as on results of a
benchmark in a synthetic setting including numerous different excitations."
date: 2022-09-05
---

I am pleased to announce a new preprint containing results of our work on AI-assisted TAS experiments.
Together with the [PANDA](https://mlz-garching.de/panda/en) team around Astrid Schneidewind and Christian Franz, Georg Brandl from the [MLZ](https://mlz-garching.de/englisch.html) Instrument Control Group, Uwe Stuhr ([EIGER](https://www.psi.ch/en/sinq/eiger) instrument responsible at [PSI](https://www.psi.ch/en)), and Marina Ganeva, leader of the MLZ Data Driven Discovery Group that I am part of, I spent a lot of energy in providing evidence on the benefits and good performance of our approach [ARIANE](https://jugit.fz-juelich.de/ainx/ariane) (**AR**tificial **I**ntelligence-**A**ssisted **N**eutron **E**xperiments).

The manuscript is an outcome of the project AINX (**A**rtificial **I**ntelligence for **N**eutron and **X**-ray scattering) funded by the [Helmholtz AI](https://helmholtz.ai) cooperation unit of the German Helmholtz Association.

I would like to thank all the co-authors of this manuscript very much for their help making the good results possible.
I am looking forward to and curious about our next steps in the project and how we will approach them.


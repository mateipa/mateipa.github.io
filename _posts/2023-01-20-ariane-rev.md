---
layout: article
title: "Revised preprint: AI-assisted neutron spectroscopy using active learning with log-Gaussian processes"
article_link: "https://arxiv.org/abs/2209.00980"
thumbnail: /assets/images/thumbnail-ariane-rev.png
abstract: "To understand the origins of materials properties, neutron scattering experiments at three-axes spectrometers (TAS) investigate magnetic and lattice excitations in a sample by measuring intensity distributions in its momentum (Q) and energy (E) space.
The high demand and limited availability of beam time for TAS experiments however raise the natural question whether we can improve their efficiency or make better use of the experimenter's time.
In fact, using TAS, there are a number of scientific questions that require searching for
signals of interest in a particular region of Q-E space, but when done
manually, it is time consuming and inefficient since the measurement points may
be placed in uninformative regions such as the background.
Active learning is a promising general machine learning approach that allows to iteratively detect informative regions of signal autonomously, i.e., without human interference, thus avoiding unnecessary measurements and speeding up the experiment.
In addition, the autonomous mode allows experimenters to focus on other relevant
tasks in the meantime.
The approach that we describe in this article exploits log-Gaussian processes which, due to the logarithmic transformation, have the largest approximation uncertainties in regions of signal.
Maximizing uncertainty as an acquisition function hence directly yields locations for informative measurements.
We demonstrate the benefits of our approach on outcomes of a real neutron experiment at the thermal TAS EIGER (PSI) as well as on results of a benchmark in a synthetic setting including numerous different excitations."
date: 2023-01-20
---

We uploaded a revised version of the manuscript on our approach [ARIANE](https://jugit.fz-juelich.de/ainx/ariane) for AI-assisted experiments at three-axes spectrometers (see a [previous post]({% link _posts/2022-09-05-ariane-prepr.md %})).
Apart from a few changes to the text, especially in the introduction, we included a comparison with [_gpCAM_](https://gpcam.lbl.gov) in the appendix.
_gpCAM_ is a competing approach that is also based on Gaussian Process Regression but substantially differs from ARIANE in how measurement locations are suggested.
Although _gpCAM_ does not fully specify how to choose values for its parameters, the comparison is based on all the information available to us.
We are looking forward to comments from the community and further discussions.


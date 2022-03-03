---
layout: page
title: Bayes' theorem and medical screening tests
date: 2021-04-03
---
The Coronavirus pandemic was an ever-present topic during the last 12 months and still is.
The virus _SARS-CoV-2_ is tried to be detected by conducting medical screening tests like the PCR or antigen tests.
A lot of these tests have been made and still continue to be done on a daily basis, regardless of whether the tested persons show symtpoms or not.
Since many of the so-called nonpharmaceutical interventions are based on the number of positive tests during the last week, it is of great importance to ensure that the test results are not only reliable on the level of a single test but also meaningful as a collection.

The following mathematical elaboration aims for an interpretation of one of the main statistical measures that are used when it comes to assessing the performance of so-called _binary classification tests_ in medicine: the _positive predictive value_ (PPV).
The PPV specifies the chance that a person with a positive test is indeed infected.

We approach this investigation by first explaining _Bayes' theorem_, a well-known and famous result from Bayesian statistics.
With this, we will derive an expression for an upper bound of the PPV that gives insight in its nature with respect to two other important values, the _false positive rate_ and the _prevalence_.

# Bayes' theorem
The famous theorem of Bayes, or just _Bayes' theorem_, is specifying how to "update" the chance (also called _degree of belief_ in the Bayesian view on the concept of probability) of a random event \\(A\\) after observing another random event \\(B\\) with \\(\mathbf{P}(B)>0\\), where \\(\mathbf{P}(B)\\) denotes the probability or chance of the event \\(B\\) occurring.

The theorem states that
\\begin{equation}
	\mathbf{P}(A\,\vert\,B) = \frac{\mathbf{P}(B\,\vert\,A) \cdot \mathbf{P}(A)}{\mathbf{P}(B)}
\\end{equation}
and can be informally interpreted by saying that the _prior probability_ \\(\mathbf{P}(A)\\) is updated by the term \\(\mathbf{P}(B\,\vert\,A)/\\mathbf{P}(B)\\) to the _posterior probability_ \\(\mathbf{P}(A\,\vert\,B)\\) after observing that \\(B\\) occurred.
A proof of this form of Bayes' theorem is trivial by applying the definition of conditional probability and using symmetry of the \\(\cap\\)-operation (intersection).

We can further concretize the above expression by regarding \\(\mathbf{P}(B)\\) as a so-called _marginal probability_ and using well-known equalities.
That is, we can write
\\begin{align}
	\mathbf{P}(B) &= \mathbf{P}(B \cap A) + \mathbf{P}(B \cap \overline{A}) \\newline
	&= \mathbf{P}(B\,\vert\,A) \cdot \mathbf{P}(A) + \mathbf{P}(B\,\vert\,\overline{A}) \cdot \mathbf{P}(\overline{A}) \\newline
	&= \mathbf{P}(B\,\vert\,A) \cdot \mathbf{P}(A) + \mathbf{P}(B\,\vert\,\overline{A}) \cdot (1-\mathbf{P}(A)) \\newline
	&= [\mathbf{P}(B\,\vert\,A) - \mathbf{P}(B\,\vert\,\overline{A})] \cdot \mathbf{P}(A) + \mathbf{P}(B\,\vert\,\overline{A}),
\\end{align}
where \\(\overline{A}\\) denotes the event of \\(A\\) _not_ occurring.

If additionally \\(\mathbf{P}(A)>0\\), we get that
\\begin{align}
	\mathbf{P}(A\,\vert\,B) &= \frac{\mathbf{P}(B\,\vert\,A) \cdot \mathbf{P}(A)}{[\mathbf{P}(B\,\vert\,A) - \mathbf{P}(B\,\vert\,\overline{A})] \cdot \mathbf{P}(A) + \mathbf{P}(B\,\vert\,\overline{A})} \\newline
	&= \frac{\mathbf{P}(B\,\vert\,A)}{\mathbf{P}(B\,\vert\,A) - \mathbf{P}(B\,\vert\,\overline{A}) + \frac{\mathbf{P}(B\,\vert\,\overline{A})}{\mathbf{P}(A)}}.
\\end{align}

Furthermore, since \\(\frac{\alpha}{\alpha+\beta} \leq \frac{1}{1+\beta}\\) for nonnegative values \\(\alpha,\beta\\) with \\(\alpha\leq1\\), it holds that
\\begin{equation}
	\mathbf{P}(A\,\vert\,B) \leq \frac{1}{1 - \mathbf{P}(B\,\vert\,\overline{A}) + \frac{\mathbf{P}(B\,\vert\,\overline{A})}{\mathbf{P}(A)}}.
\\end{equation}

# Positive predictive value of medical screening tests
Let us now apply the above result for medical screening tests to get some insight into the _positive predictive value_.

For this, we denote the event of a person being infected as
\\begin{equation}
	I := \lbrace \text{Person is infected} \rbrace.
\\end{equation}
The event \\(I\\) replaces what was denoted by the event \\(A\\) above.

The event, that a test of this person is positive, is denoted as
\\begin{equation}
	T_+ := \lbrace \text{Test of person is positive} \rbrace.
\\end{equation}
The event \\(T_+\\) replaces what was denoted by the event \\(B\\) above.

Hence, the expression \\(\mathbf{P}(I\,\vert\,T_+)\\) denotes the probability that a person is indeed infected after getting a positive test result. 

Applying the upper bound from above, we get that
\\begin{equation}
	\mathbf{P}(I\,\vert\,T_+) \leq \frac{1}{1 - \mathbf{P}(T_+\,\vert\,\overline{I}) + \frac{\mathbf{P}(T_+\,\vert\,\overline{I})}{\mathbf{P}(I)}},
\\end{equation}
where \\(\overline{I}\\) denotes the event that the person is _not_ infected.
The term \\(\mathbf{P}(T_+\,\vert\,\overline{I})\\) is also called the _false positive rate_ (FPR) of the test and represents the ratio between the number of falsely positive tests and the number of noninfected persons.
The _prevalence_ is denoted by \\(\mathbf{P}(I)\\) and specifies the proportion of infected persons in the whole population.

Finally, repeating the above inequality with the mentioned terms, we get that
\\begin{equation}
	\mathbf{P}(I\,\vert\,T_+) \leq \frac{1}{1 - \text{FPR} + \frac{\text{FPR}}{\text{Prevalence}}}.
\\end{equation}

The upper bound, viewed as a function of the FPR and the prevalence, is displayed in the following figure.
<center><img src="/assets/images/fpr-preval-ppv.svg" /></center>
Note that the \\(y\\)-axis has a _log_ scale.

# Interpretation
The main observation with the above figure is that the PPV can get quite low if the FPR and the prevalence are unfavorably related.
More concretely, if the prevalence is low, say \\(\text{prevalence}\approx1\%\\),
then the test needs to be really accurate in the sense that it should have a FPR close to zero; otherwise the test risks becoming unreliable and invalid which can lead to false assessments of the public health situation and thus can provide incorrect information to policy makers.


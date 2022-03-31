---
layout: post
title: "Scientific Computing: attempting a definition"
date: 2021-04-02
pinned: true
---

First of all, "Scientific Computing" (SC) is an accepted term for a certain area of research among mathematicians and computer scientists particularly, but also for the scientific community in general.
However, scientists seem to have varying notions of the term, even if they come from similar disciplines.
This text attempts to show why a clear definition of the term is not straightforward, but finally dares to do exactly that, a fairly clear (objective) definition.

Let us start with an obvious observation.
The term "Scientific Computing" consists of two words: "scientific" and "computing".
We do not try to explain both words separately.
For the first, we would have to find a definition for "science" which is a question that already exists for centuries and is tried to be answered by philosophy, more exactly [_philosophy of science_](https://en.wikipedia.org/wiki/Philosophy_of_science).

What we are rather looking for is a definition of the term "Scientific Computing" (as an interplay of both words) in which the word "scientific" is related to "computing".
Hence, following langugage, SC is a _particular kind of computing_ that is _scientifically sound_, accepts the _scientific method_, and is thus open for the scientific community to get criticized and discussed.

As opposed to these rather trivial observations, the more difficult question to answer is what SC _really does_, in the sense of questions like
- which areas of mathematics and computer science are used in SC and how they interact,
- which problems are solved by SC and how.

SC has often been tried to be defined by following questions of this type.
However, doing so increases the risk of the definition getting subjective too quickly.
For example, a statistician has answers to the above questions that can substantially differ from answers given by a numerical analyst or a computer scientist, but still everyone is convinced that the own description is more precise.
This does not get us very far.

To find a more objective definition of SC, we need to circumvent classifications of the mentioned type.
We base our attempt of a definition on what we want to call the _three pillars of SC_:
1. Theory,
2. Methodology,
3. Implementation.

For this attempt, we need to agree on the following: "SC tries to solve problems that can be solved by computing, i.e., by using a computer."
Such problems are called _computational problems_ in the remainder and often involve _mathematical models_.

Now, the main point of our definition is that neither finding a method or an algorithm alone (methodology), nor proving a numerical result for its own sake (theory), nor an efficient implementation of an algorithm in a suitable programming language (implementation) without a connection to the former two tasks is what SC does.
Much more, it is the (often complex) interplay of all of the three parts.

<br><center><img src="/assets/images/sc-pillars.svg" /></center><br>

The main purpose of SC certainly is finding a method or algorithm that solves a computational problem.
However, following our definition, only the consideration and connection of all three aspects makes the approach a scientific computing approach.

# 1. Theory
Theory, as we use the term in this context, leads to a _formal verification_ of the developed algorithm.
For this, it utilizes a reasonable (mathematical and logical) formalism and useful notation to show that the algorithm is indeed solving the given computational problem.
The quality of the solution can be demonstrated as well.
As an example, numerical analysts can provide promising convergence results or insightful upper bounds on approximation errors.
Additionally, formal formulations can also lead to useful abstractions which potentially broadens the applicability of the method.

Most of theory is done by mathematicians, or at least in a mathematical way.
Mathematical areas that are often applied are, e.g., linear algebra, calculus, numerical mathematics, probability theory, and statistics.
However, also theoretical areas from computer science, as e.g., computability theory or complexity theory, can play a role here depending on the concrete case.

# 2. Methodology
As mentioned, this is certainly the core of the scientific computing approach.
The main job of this part is the development of methods, algorithms, or techniques to solve the computational problem at hand.
Preferably, the approaches need to be described algorithmically such that others can understand them.
It is then the theorist's task to provide a proof of the quality of the approach to the community.
The implementation in software can get started as soon as there is a reasonable description of the method and a sufficiently large chance of success.

In our view, it is indeterminate whether the methodological part is dominated by mathematics or computer science.
We find that both disciplines can equally contribute here.

# 3. Implementation
Implementing a proposed method or algorithm is software development, more or less.
Of course, if the problem is highly computationally expensive, techniques of _high performance computing_, which we also see as part of implementation, should be applied.
It is the job of the software developer (or computer scientist) to produce code that efficiently executes the idea of the algorithm.
In this respect, software validation by suitable tests showing the correctness of the implementation is also necessary at this point.

Since this part is mostly about software development, it is certainly dominated by computer science.
Of course, programming can also be done by mathematicians who however act as software developers then.

Theoretically, all of the above three parts can be done by one and the same person.
Though, there is more than one scientist involved in most cases since approaches can consist of multiple sufficiently complex subtasks that need to be handled by specialists.

# Distinction from _Computational Science_
In contrast to a definition from [Wikipedia](https://en.wikipedia.org/wiki/Computational_science), which does _not_ differ between SC and _Computational Science_ (ClS; to distinguish from CS which is often used for computer science), we would like to promote such a distinction.

The focus with SC lies on the computing or computation aspect, in our opinion.
In other words, we have a computational problem that is tried to be solved scientifically and that orientates on the three pillars mentioned above.

On the other hand, ClS, as the term says, is doing _science_, science in a _computational_ manner.
This means that ClS tries to answer questions from a certain scientific area and hence always has the application in mind.
For example, problems from astrophysics are nowadays often solved computationally by simulations involving mathematical models that aim to reflect reality.
We can thus say that "SC is applied to do ClS" in this case.
Of course, computational problems in SC can be motivated by questions from ClS or from a certain scientific discipline directly, but do not necessarily need to.
Problems in SC can also emerge from other problems in SC.

# Summary
This text tried to formulate a new definition of _Scientific Computing_.
Existing approaches are often based on questions like which mathematical or computer science areas contribute to SC, which is rather subjective.
We aimed for establishing objectivity in the new definition by following another approach called _the three pillars of SC_: theory, methodology, implementation.
Finally, an explicit distinction to _Computational Science_ was made which however conflicts with other attempts; see, e.g., [Wikipedia](https://en.wikipedia.org/wiki/Computational_science).


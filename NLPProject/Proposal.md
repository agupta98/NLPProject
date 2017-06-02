## Overview

We are trying a build a poetry and a poetry title generator based on the topic supplied by the user. In the past these two have been done individually. What makes our project interesting the the ability to do both the work simultaneously.

## Data

We plan to scrap poems from different open source website were general public submit their work. Example: https://www.poetryfoundation.org/poems-and-poets/poems

## Method

We plan to use recurrent neural network as our algorithm. We will use Tensor Flow to implement the algorithm. We will not be modifying the code of the library but might use hyper parameter optimization using hyperOpt.

## Related Work

https://homes.cs.washington.edu/~yejin/Papers/emnlp16_sonnet.pdf

http://nlp.stanford.edu/courses/cs224n/2015/reports/1.pdf

https://www.aclweb.org/anthology/D/D15/D15-1044.pdf

http://publications.lib.chalmers.se/records/fulltext/245146/245146.pdf

http://karpathy.github.io/2015/05/21/rnn-effectiveness/

## Evaluation

The baseline model will be to building a language model. For example: the trump bot that you build in the class.  Key plots will the weight that is assignment to each word. The decrease in the loss function with the training time for neural Network. The increase of the effectiveness of the model versus training point.


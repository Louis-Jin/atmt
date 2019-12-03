# atmt assignment 4

## to run the code
Run part04.sh for all predictions. Then plot with part01_plot.ipynb, plot03.py and plot04.py

## Implementation

### Part 03
Inside ‘get_best’ function in beam.py. 

For all the potential predictions, recalculate their probabilities by adding length normalization.

### Part 04
Inside translate_beam.py, annotated with ‘Part 04’

Since there is no need to add diversity at the first layer of the search tree, I recalculated the probability only for nodes at deeper layers, as long as that node is not a final node. And since the penalty is only used for selecting nodes across same layer, it should not be stored as the log probability. Otherwise the longer a prediction is, more severely it will be penalized. 


# atmt assignment 3

## to run the code
We used pytorch 1.3 and cuda 10.1, runnable on Windows or Ubuntu machine with the two mentioned packages installed, or it can be run online on Google Colab.

We trained three models. 

1. Run train1.py for model 1 & 2
2. Run train.py for model 3

The results for three models are inside results folder.

The plots we added in the report are generated from plot.ipynb

## implementation

### the loss term we added
We adapted train.py to train bidirectionally and then added an additional loss with function get_diff. 

We want to let representations produced by encoders be the same for different languages.

Given one sentence in language en and de. And when we train from de-en, let's take the first word in en, \(v1=attention*src-out\) should represent this word, v2. We defined cos(v1, v2) as loss for our desired property. And to not constrain the representation power, we use cos(v1, v) for all other words in this sentence as normalization.

Notice that our normalization here is division. Whereas in lecture 9, the Unsupervised Sentence Similarity use addition, which should have better numerical stability.

### small small changes
For bidirectional training, there are some small changes for that in utils.py. and We also made it runnable on gpu.

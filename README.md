# atmt assignment 3

## to run the code
We used pytorch 1.3 and cuda 10.1, runnable on Windows or Ubuntu machine with the two mentioned packages installed, or it can be run online on Google Colab.
We trained three models. 

1. Run train1.py is for model 1 & 2
2. Run train.py is for model 3

The results for three models are inside results folder.

The plots we added in the report are generated from plot.ipynb

## implementation
We adapted train.py to train bidirectionally and then added an additional loss with function get_diff. 
We want to let representations produced by encoders be the same for different languages.
Given one sentence in language en and de. And when we train from de-en, let's take the first word in en, \(v1=attention*src-out\) should represent this word, v2. We defined cos(v1, v2) as loss for our desired property. And to not constrain the representation power, we use cos(v1, v) for all other words in this sentence as normalization. 
Our normalization here is division. Whereas in lecture 9, the Unsupervised Sentence Similarity use addition. It should have better numerical stability.

For bidirectional training, there are some small changes for that in utils.py. and We also made it runnable on gpu.

import sacrebleu
import numpy as np

ks = [3,5,7,8,9,10,11]
alpha_max = 10

alphas = [i/10 for i in range(0, 11)]
gamma = 0
Xs, Ys = np.meshgrid(ks, alphas)
Zs = np.zeros((alpha_max+1, len(ks)))

for (itr_k, k) in enumerate(ks):
#    for alpha in range(0, alpha_max + 1):
    for alpha in range(0, alpha_max + 1):
        with open('data_asg4/raw_data/test.en', 'r') as f:
            refs = f.readlines()
        refs = [refs]
        with open('./output_asg4_part4/k{}/postprocessed/model_translations_alpha{}-gamma{}.out'.format(k, alpha, gamma), 'r') as f:
            sys = f.readlines()
        bleu = sacrebleu.corpus_bleu(sys, refs)
        Zs[alpha, itr_k] = bleu.score

print(Zs)
print(np.max(Zs))
max_index = np.argmax(Zs)
print(max_index)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(Xs, Ys, Zs)
plt.xlabel('ks')
plt.ylabel('alphas')
plt.title('Length Normalization Experiment')
plt.show()

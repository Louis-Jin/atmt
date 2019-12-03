import sacrebleu
import numpy as np

k = 11
print('beam size is {}'.format(k))
alpha_max = 10
gamma_max = 10
alphas = [i/10 for i in range(0, 11)]
gammas = [i/10 for i in range(0, 11)]
Xs, Ys = np.meshgrid(gammas, alphas)
Zs = np.zeros((len(alphas), len(gammas)))

for gamma in range(0, gamma_max + 1):
    for alpha in range(0, alpha_max + 1):
        with open('data_asg4/raw_data/test.en', 'r') as f:
            refs = f.readlines()
        refs = [refs]
        with open('./output_asg4_part4/k{}/postprocessed/model_translations_alpha{}-gamma{}.out'.format(k, alpha, gamma), 'r') as f:
            sys = f.readlines()
        bleu = sacrebleu.corpus_bleu(sys, refs)
        Zs[alpha, gamma] = bleu.score
print(np.max(Zs))
print(Zs)
max_index = np.argmax(Zs)
print(max_index)
print('max at gamma %0.2f, alpha %0.2f' % ((max_index%11)/10, np.floor(max_index/11)/10))


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(Xs, Ys, Zs)
plt.xlabel('gammas')
plt.ylabel('alphas')
plt.title('Diversity Experiment')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.5)


fpr = np.linspace(0, 0.1, num=100)
preval = np.logspace(-4, 0, num=100)
fpr_v, preval_v = np.meshgrid(fpr, preval)

ppv_v = 1 / (1 - fpr_v + fpr_v/preval_v)

plt.figure(figsize=(6, 4))
ax = plt.gca()
plt.imshow(ppv_v, extent=[np.min(fpr), np.max(fpr),
                          np.min(preval), np.max(preval)],
           aspect='auto', origin='lower', vmin=0, vmax=1)
plt.yticks(np.linspace(0, 1, num=5))
ax.set_yticklabels([f'$10^{{{exp}}}$' for exp in range(-4, 1)])
plt.xlabel('FPR')
plt.ylabel('Prevalence')
plt.grid(False)
plt.colorbar()
plt.tight_layout()

plt.show()


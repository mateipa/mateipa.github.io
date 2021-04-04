import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('whitegrid')
sns.set_context('talk')


fpr_v, preval_v = np.meshgrid(np.linspace(0, 0.1, num=100), np.logspace(-4, 0, num=100))

ppv_v = 1 / (1 - fpr_v + fpr_v/preval_v)

plt.figure(figsize=(6, 4))
plt.contourf(fpr_v, preval_v, ppv_v, levels=np.linspace(0, 1, num=6))
plt.yscale('log')
plt.xlabel('FPR')
plt.ylabel('Prevalence')
plt.colorbar()
plt.tight_layout()

plt.show()


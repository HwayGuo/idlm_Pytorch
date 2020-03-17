"""
This function is for generating a bunch of random numbers as the answer to the inverse problems and see how well do
those algorithm perform compared to random answers
"""
import numpy as np
from utils.helper_functions import simulator

x_dim = 8
num_of_files = 1
num_of_points = 1000

data_dir = ''
Xpred_file_prefix = 'test_Xpred_random_guess_answers_inference'
data_set = 'meta_material'
# data_set = 'robotic_arm'
# data_set = 'sine_wave'
# data_set = 'gaussian_mixture'

if __name__ == '__main__':
    for i in range(num_of_files):
        print("Generating random uniform distribution fake Xpred data_set for ",
              data_set, "file", i)
        Xpred = np.random.uniform(-1, 1, size=(num_of_points, x_dim))
        Xpred_file = data_dir + data_set + Xpred_file_prefix + str(i) + '.csv'
        Ypred_file = Xpred_file.replace('Xpred', 'Ypred')
        np.savetxt(Xpred_file, Xpred, fmt='%.3f')
        if data_set == 'meta_material':             # meta_material does not have a simulator, it needs forward model
            continue
        Ypred = simulator(data_set, Xpred)
        np.savetxt(Ypred_file, Ypred, fmt='%.3f')



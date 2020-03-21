"""
Params for Back propagation model
"""
# Define which data set you are using
# DATA_SET = 'meta_material'
# DATA_SET = 'gaussian_mixture'
DATA_SET = 'sine_wave'
# DATA_SET = 'naval_propulsion'
# DATA_SET = 'robotic_arm'

# Model Architectural Params for meta_material data Set
USE_LORENTZ = False
#LINEAR = [8,  1000, 1000, 1000, 1000, 150]
#CONV_OUT_CHANNEL = [4, 4, 4]
#CONV_KERNEL_SIZE = [8, 5, 5]
#CONV_STRIDE = [2, 1, 1]

# Model Architectural Params for gaussian mixture DataSet
LINEAR = [2, 60, 60, 60, 60, 60, 60, 4]                 # Dimension of data set cross check with data generator
CONV_OUT_CHANNEL = []
CONV_KERNEL_SIZE = []
CONV_STRIDE = []


# Optimizer Params
OPTIM = "Adam"
REG_SCALE = 1e-3
BATCH_SIZE = 1024
EVAL_BATCH_SIZE = 1000
EVAL_STEP = 20
TRAIN_STEP = 300
BACKPROP_STEP = 300
LEARN_RATE = 1e-2
# DECAY_STEP = 25000 # This is for step decay, however we are using dynamic decaying
LR_DECAY_RATE = 0.8
STOP_THRESHOLD = 1e-5

# Data specific Params
X_RANGE = [i for i in range(2, 10 )]
Y_RANGE = [i for i in range(10 , 2011 )]
FORCE_RUN = True
MODEL_NAME = None 
DATA_DIR = '../'
#DATA_DIR = '/work/sr365/'
# DATA_DIR = '/home/omar/PycharmProjects/github/idlm_Pytorch-master/forward/'
GEOBOUNDARY =[30, 52, 42, 52]
NORMALIZE_INPUT = True

# Running specific
USE_CPU_ONLY = False
EVAL_MODEL = "sine_wavereg0.0005trail_2_backward_complexity_swipe_layer150_num7"

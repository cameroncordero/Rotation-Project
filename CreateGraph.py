import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
gdata = pd.read_csv(OutputFile, header = None, names= ['Mutation' , 'Frequency'])
sns.barplot(x = 'Mutation', y = 'Frequency', data = gdata,))
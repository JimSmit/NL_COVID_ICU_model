import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from classes import *


# Set parameters

beds = 930                          # Max number of ICU beds available for COVID patients
ic_death_rat = 0.40                 # fraction of patients that eventually pass away after enetering ICU
days_to_better = 21                 # length of stay (in days) for patients that recover
days_to_dead = 7                    # length of stay (in days) for patients that die
plot_days = 14                      # day into the future to predict

scenario = 'worst'                  # worst, medium or best case scenario       

saturations = [30, 40 , 50]         # Choose days till saturation
gf = 1.3



## option 1: real and predicted data
y_round, days = list_of_real_predicted_new_cases(saturations, scenario, gf, plot_days, smooth=True)




hospitals = Hospitals(beds=beds, ic_death_rat=ic_death_rat, days_to_better=days_to_better, days_to_dead=days_to_dead)
for new_cases in y_round:        
    hospitals.leave_hospital()
    hospitals.new_patients(new_cases)
    hospitals.log_day()
    hospitals.add_day()



hospitals.plot_log(log=True, map_days=True, start_day='21-02-2020', day_zero=dt.date.today())

# hospitals.summarise()


print('break')

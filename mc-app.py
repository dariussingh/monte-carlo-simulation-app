import utils
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Monte Carlo Simulation on Ad Impressions')
st.write('App to run monte carlo simulation on facebook ad impressions dataset.')

st.header('Simulation')

# data
data = utils.create_random_ads(10)

# prerequsites for MC sim
data['probability'] = utils.calculate_prob(data['impressions'])
data['cumulative_prob'] = utils.calculate_cumulative_probablity(data['probability'])
data['rand_interval'] = utils.create_random_interval(data['cumulative_prob'])

number_ads = st.slider('Run Simulation for N ads', 1, 10000, 10)
# run sim
# if st.button('Run Simulation'):
    # for i in range(1,number_ads):
rand_nums = utils.generate_random_num(number_ads)
sim = utils.run_simulation(rand_nums, data)
utils.plot_sim(sim)
# import dependnecies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# define necessary functions
def create_random_ads(num_ads):
    runtime = np.random.randint(low=15, high=90, size=num_ads)
    impressions = np.random.randint(low=50000, high=70000, size=num_ads)
    ad_id = [f'ad_{i}' for i in range(num_ads)]
    
    data = pd.DataFrame({'ids':ad_id, 'length(in secs)':runtime, 'impressions':impressions})
    return data

def calculate_prob(feature_data):
    total = sum(feature_data)
    probablity = [round(imp/total,2) for imp in feature_data]
    return probablity

def calculate_cumulative_probablity(prob_data):
    cumulative_prob = [sum(prob_data[:i]) for i in range(1,len(prob_data)+1)]
    return cumulative_prob

def create_random_interval(cumulative_prob):
    rand_intervals = []
    for i in range(len(cumulative_prob)):
        if i==0:
            interval = f'00-{int((round((cumulative_prob[i]*100)-1)))}'
        elif i==len(cumulative_prob)-1:
            interval = f'{int(round(cumulative_prob[i-1]*100, 0))}-{99}'
        else:
            interval = f'{int(round(cumulative_prob[i-1]*100))}-{int(round((cumulative_prob[i]*100)-1))}'
        rand_intervals.append(interval)
    return rand_intervals

def generate_random_num(num):
    rand_num = np.random.randint(0,100,size=num)
    return rand_num

def run_simulation(rand_nums, data):
    ad_ids = []
    ad_lengths = []
    for number in rand_nums:
        for row in data.iterrows():
            ad_id = row[1]['ids']
            length = row[1]['length(in secs)']
            interval = row[1]['rand_interval']
            interval = interval.split('-')
            if int(interval[0])<=number<=int(interval[1]):
                ad_ids.append(ad_id)
                ad_lengths.append(length)
    sim = pd.DataFrame({'ids':ad_ids, 'length(in secs)':ad_lengths})
    return sim


def plot_sim(sim_data):
    """
    Take ordered simulation data as input and calculates the sum and plots the simulation 
    """
    ad_num_list = [0]
    ad_impression_count = dict()
    for ad in list(sim_data['ids'].unique()):
        ad_impression_count[ad] = [0]
    
    # calculation of counts
    for row in sim_data.iterrows():
        ad_num = row[0]+1
        ad_num_list.append(ad_num)
        ad = row[1]['ids']
        for key in ad_impression_count.keys():
            if key==ad:
                count = ad_impression_count[key][-1]
                ad_impression_count[key].append(count + 1)
            else:
                count = ad_impression_count[key][-1]
                ad_impression_count[key].append(count)    
                
    # plotting 
    fig = plt.figure(figsize=(10,7))
    plt.ylim(0,4000)
    plt.xlim(0,10000)
    for ad in ad_impression_count.keys():
        plt.plot(ad_num_list, ad_impression_count[ad], label=ad)
    plt.legend()
    st.pyplot(fig)
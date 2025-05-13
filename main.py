import csv
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

def calculate_total_runs(deliveries_reader):
    team_runs={}
    for delivery in deliveries_reader:
        team=delivery['batting_team']
        runs=int(delivery['total_runs'])
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team]=runs
    return team_runs

def plot(team_runs):
    plt.figure(figsize=(12,12))
    plt.pie(team_runs.values(),labels=team_runs.keys(),autopct="%.2f%%")
    plt.title("Total Runs Scored by Team")
    plt.show()

def execute():
    with open('deliveries.csv','r') as file:
        deliveries_reader=csv.DictReader(file)
        team_runs=calculate_total_runs(deliveries_reader)
        plot(team_runs)

execute()
import csv
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

user_inp= int(input("Enter a number which you want to execute:\n1.Total runs scored by team.\n2.Top 10 batsman in Royal Challengers Bangalore\n"))

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

def plot1(team_runs):
    plt.figure(figsize=(12,12))
    plt.pie(team_runs.values(),labels=team_runs.keys(),autopct="%.2f%%")
    plt.title("Total Runs Scored by Team")
    plt.show()

def calculate_players_total_score(deliveries_reader):
    batsman_runs={}
    for delivery in deliveries_reader:
        if delivery['batting_team']=="Royal Challengers Bangalore":
            if delivery['batsman'] in batsman_runs:
                batsman_runs[delivery['batsman']] += int(delivery['total_runs'])
            else:
                batsman_runs[delivery['batsman']] = int(delivery['total_runs'])
    top_10_batsman=sorted(batsman_runs.items(),key=lambda item:item[1],reverse=True)[:10]
    return(top_10_batsman)

def plot2(top_10_batsman_runs):
    names=[name for name,_ in top_10_batsman_runs]
    scores=[score for _,score in top_10_batsman_runs]
    plt.figure(figsize=(12,12))
    plt.bar(names,scores,align='center',edgecolor='green')
    plt.title('TOP 10 BATSMAN IN RCB')
    plt.xlabel('Batsman_name')
    plt.ylabel('Total_Runs')
    plt.show()

def execute():
    with open('deliveries.csv','r') as file:
        deliveries_reader=csv.DictReader(file)
        if user_inp==1:
            team_runs=calculate_total_runs(deliveries_reader)
            plot1(team_runs)
        elif user_inp==2:
            top_10_batsman_runs=calculate_players_total_score(deliveries_reader)
            plot2(top_10_batsman_runs)

execute()
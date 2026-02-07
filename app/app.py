from src.metrics_activity import analyze_activity_and_sleep

data_path = "../data/rawSleep_health_and_lifestyle_dataset.csv"

report = analyze_activity_and_sleep(data_path)

print("Activity Impact Report")
print (report)

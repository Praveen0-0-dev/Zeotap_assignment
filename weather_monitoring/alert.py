#alert.py
def check_alerts(temp,threshold=35):
  if temp>threshold:
    print("Alert: High temperature")

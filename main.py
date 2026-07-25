import numpy as np
def anlyze_engine_data (temp_array , voltage_array):
    print("starting engine data analysis")


    avg_temp = np.mean(temp_array)
    max_temp = np.max(temp_array)
    avg_volt = np.mean(voltage_array)
    print(f"Average temp:.1{avg_temp}°C | peak temp:{max_temp}°C")
    print(f"Average voltage:.2{avg_volt}V")
    critical_temps = temp_array[ temp_array > 40.0 ]
    if max_temp > 45.0 or avg_volt < 3.5:
       system_status = "CRITICAL:engine needs immediate inspection!"
    elif len(critical_temps) > 0:
       system_status = "WARNING: elevated temperature detected."
    else:
         system_status = "OPTIMAL: all parameters are normal."
    return system_status, critical_temps
engine_tempratures = np.array([36.5,37.0,38.2,42.5,39.0,46.1,37.8])
engine_voltage = np.array([4.1,4.0,4.2,3.9,4.1,3.8,4.0])
status,anomalies = anlyze_engine_data(engine_tempratures,engine_voltage)
print("final system report")
print(f"system status:{status}")
print(f"detected anomalies:{anomalies}")

from anylogiccloudclient.client.cloud_client import CloudClient

client = CloudClient("e05a6efa-ea5f-4adf-b090-ae0ca7d16c20")
print(client)

version = client.get_latest_model_version("Service System Demo")
print(version)

inputs = client.create_inputs_from_experiment(version, "Baseline")
inputs.set_input("Server capacity", 8)

simulation = client.create_simulation(inputs)
print(simulation)

outputs = simulation.get_outputs_and_run_if_absent()

print("Raw outputs = " + str(outputs.get_raw_outputs()))
print("For Server Capacity = " + str(inputs.get_input("Server capacity")))
print("Mean queue size = " + str(outputs.value("Mean queue size|Mean queue size")))
print("Server utilization = " + str(outputs.value("Utilization|Server utilization")))

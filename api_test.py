from anylogiccloudclient.client.cloud_client import CloudClient

client = CloudClient("e05a6efa-ea5f-4adf-b090-ae0ca7d16c20")

# version = client.get_latest_model_version("Bass Diffusion Demo 8.5.0")

version = client.get_latest_model_version("Transporters Moving in Free Space")

print(version)

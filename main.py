from fastapi import FastAPI

app = FastAPI(title="API Dashboard")

# Sample API data. This is intentionally in-memory for this learning project.
services = [
    {"name": "Weather API", "protocol": "REST", "status": "online"},
    {"name": "Payment API", "protocol": "REST", "status": "online"},
    {"name": "Maps API", "protocol": "GraphQL", "status": "offline"},
]


@app.get("/")
def home():
    return {"message": "Welcome to API Dashboard"}


@app.get("/api/summary")
def get_summary():
    online = sum(1 for service in services if service["status"] == "online")
    offline = sum(1 for service in services if service["status"] == "offline")

    protocol_counts = {}
    for service in services:
        protocol = service["protocol"]
        protocol_counts[protocol] = protocol_counts.get(protocol, 0) + 1

    return {
        "total_services": len(services),
        "online": online,
        "offline": offline,
        "protocols": protocol_counts,
    }

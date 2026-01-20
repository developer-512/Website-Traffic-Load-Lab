import matplotlib.pyplot as plt

def generate_latency_chart(results):
    times = [r["time"] for r in results]

    plt.figure()
    plt.plot(times)
    plt.title("Latency Over Time")
    plt.xlabel("Request #")
    plt.ylabel("Seconds")
    plt.savefig("artifacts/charts/latency.png")

import matplotlib.pyplot as pylot

def generate():
    labels = ["a", "b", "c"]
    values = [100, 50, 90]

    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig("pylot.png")
    pylot.close()
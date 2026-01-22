import psutil



def get_system_metrics():

    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_threshold = 10

    status = "Hight CPU" if cpu_percent > cpu_threshold else "Healthy"

    return {
        cpu_percent :cpu_percent,
        status:status

    }

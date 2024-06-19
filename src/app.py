from service.service import Service, run_simple


if __name__ == "__main__":
    service = Service()
    run_simple("0.0.0.0", 5000, service.application)
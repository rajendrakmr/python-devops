def extract_errors(log_file):
    errors = []
    with open(log_file, "r") as f:
        for line in f:
            if "ALERT" in line or "Exception" in line:
                # print("___________________________",line.casefold())
                errors.append(line.strip())
    return errors

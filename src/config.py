class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_raw = open(config_path, "r").read()
        self.config = {}

    def get(self, key, default_value = None):
        if key in self.config:
            return self.config[key]
        else:
            return default_value

    def load(self):
        self.config = {}
        
        for line in self.config_raw.splitlines():
            if line.startswith("#") or line.strip() == "":
                continue

            key = line.split("=")[0].strip()
            value = line.split("=")[1].strip()

            if value.startswith("\"") and value.endswith("\""):
                value = value.replace("\"", "")
            elif value == "true" or value == "false":
                value = value == "true"
            else:
                value = int(value)

            self.config[key] = value

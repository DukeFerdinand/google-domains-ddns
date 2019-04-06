class Settings:
    USERNAME=""
    PASSWORD=""
    DOMAIN=""
    def configure(self, config):
        self.USERNAME = config["USERNAME"]
        self.PASSWORD = config["PASSWORD"]
        self.DOMAIN = config["DOMAIN"]

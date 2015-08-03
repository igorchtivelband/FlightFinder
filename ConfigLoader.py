__author__ = 'igorchtivelband'
import yaml

class ConfigLoader:

    def __init__(self):
        with open ("./config/config.yaml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            self.price_threshold = cfg['price_threshold']
            self.api_key =  cfg['qpx__express_api_key']
            self.target_email = cfg['target_email']
            self.SMTP_SERVER = cfg['SMTP_SERVER']
            self.SMTP_PORT = cfg['SMTP_PORT']
            self.SMTP_USERNAME = cfg['SMTP_USERNAME']
            self.SMTP_PASSWORD = cfg['SMTP_PASSWORD']




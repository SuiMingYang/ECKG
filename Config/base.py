import configparser

def setConf():
    config_url="./config/config.conf"
    conf = configparser.RawConfigParser()
    conf.read(config_url,encoding='utf-8')
    return conf

def setVariable():
    config_url="./config/variable.ini"
    conf = configparser.RawConfigParser()
    conf.read(config_url,encoding='utf-8')
    return conf

conf = setConf()
variable = setVariable()
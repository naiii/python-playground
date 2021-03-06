import configparser


Config = configparser.ConfigParser()
Config.read('config.ini')
Config.sections()


def config_section_map(section):
    config_dict = {}
    options = Config.options(section)
    for option in options:
        try:
            config_dict[option] = Config.get(section, option)
            if config_dict[option] == -1:
                print('Skip: %s' % option)
        except:
            print('Exception on %s.' % option)
            config_dict[option] = None

    return config_dict


#
# Bot setup
#
bot_token = config_section_map('Discord')['token']

#
# Discord Auth
#
client_id = config_section_map('Discord')['client_id']
client_secret = config_section_map('Discord')['client_secret']


#
# GitHub
#
github_token = config_section_map('GitHub')['token']
github_owner = config_section_map('GitHub')['owner']
github_repo = config_section_map('GitHub')['repo']

#
# Postgres
#
pg_host = config_section_map('Postgres')['host']
pg_user = config_section_map('Postgres')['user']
pg_password = config_section_map('Postgres')['password']
pg_database = config_section_map('Postgres')['database']

#
# RabbitMQ
#
mq_user = config_section_map('RabbitMQ')['mq_user']
mq_password = config_section_map('RabbitMQ')['mq_password']
mq_host = config_section_map('RabbitMQ')['mq_host']
mq_port = config_section_map('RabbitMQ')['mq_port']

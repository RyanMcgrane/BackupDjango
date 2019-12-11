"""
This file contains settings parameters which shouldn't be committed to a public repository such as GitHub.
Unlike other code files, this file is not managed by git.
It will be read into settings at runtime.

Use this as an example to make a 'secrets.py' file in your project directory (beside settings.py).
"""


def get_secrets():
    SECRETS = {
        'MY_DOMAIN_NAME': 'ryanmcshop.com',
        'DOCKER_IMAGE': 'c16419862/ryanmcshop',
        'DOCKER_COMPOSE_FILE': 'docker-compose.yml',
        'NGINX_CONF': 'nginx_conf_template',
        # 'SECRET_KEY': '<<whatever django generated is appropriate>>',
        'DATABASES': {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'gis',
                'HOST': '134.209.28.101',
                'PORT': '5433',
                'USER': 'docker',
                'PASSWORD': 'docker',
            }
        },
        'ALLOWED_HOSTNAMES': [
            'ryanmcgrane',
        ],

    }

    return SECRETS


def insert_domainname_in_conf(conf_file, my_domain_name):
    try:
        with open("nginx_conf_template", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("ryanmcshop.com", my_domain_name)
        with open(conf_file, "w") as fh:
            fh.write(conf_text)

    except Exception as e:
        print(f"{e}")


def insert_imagename_in_compose(compose_file, image_name):
    try:
        with open("docker-compose-template", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("--your-image-name-goes-here--", image_name)
        with open(compose_file, "w") as fh:
            fh.write(conf_text)

    except Exception as e:
        print(f"{e}")


def insert_projectname_in_uwsgi_ini(project_name, uwsgi_file):
    """
    Sets up a uwsgi ini file modified with your project (directory) name

    :param project_name: usually figured out from the settings.py directory
    :param uwsgi_file: the outgoing uwsgi file usually uwsgi.ini
    :return:
    """
    try:
        with open("uwsgi.ini.sample", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("--your-project-name-goes-here--", project_name)
        with open(uwsgi_file, "w") as fh:
            fh.write(conf_text)
    except Exception as e:
        print(f"{e}")

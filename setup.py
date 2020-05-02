from setuptools import setup, find_packages

setup(
    name='adjutant',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/acorbat/adjutant/tree/master/',
    license='MIT',
    author='Agustin Corbat',
    author_email='acorbat@df.uba.ar',
    description='Slack adjutant manages different tasks using slack direct '
                'messages.',
    install_requires=['flask', 'slackclient', 'slackeventsapi', 'wakeonlan']
)
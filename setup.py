from setuptools import setup

setup(
    name='adjutant',
    version='0.1.0',
    packages=['adjutant', 'abilities'],
    url='https://github.com/acorbat/adjutant/tree/master/',
    license='MIT',
    author='Agustin Corbat',
    author_email='acorbat@df.uba.ar',
    description='Slack adjutant manages different tasks using slack direct '
                'messages.',
    install_requires=[
        'flask',
        'slackclient',
        'slackeventsapi',
        'wakeonlan',
        ],
    extras_require={
        'test': [
            'pytest>=3.6',
            'pytest-cov',
            'flake8',
        ], }
)

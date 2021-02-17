from distutils.core import setup

setup(
    name='proxyMama',  # How you named your package folder (proxyMama)
    packages=['proxyMama'],  # Chose the same as "name"
    version='1.2',  # Start with a small number and increase it with every change you make
    license='GNU GPLv3',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='A simple proxy manager for your web scraping journey',  # Give a short description about your library
    author='Jake Strouse',  # Type in your name
    author_email='jakestrouse00@gmail.com',  # Type in your E-Mail
    url='https://github.com/jakestrouse00/proxyMama',  # Provide either the link to your github or to your website
    keywords=['proxy manager', 'proxy', 'manager', 'requests'],  # Keywords that define your package best
    # install_requires=[  # I get to this in a second
    #     'validators',
    #     'beautifulsoup4',
    # ],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

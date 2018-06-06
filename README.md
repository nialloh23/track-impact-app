# TrackImpact.com
An app that enables volunteer teams to track their volunteering and fundraising activities bringing their collective impact to life.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Python ~2.7
* Vagrant
* Udacity Vagrant file
* VirtualBox

### Packages & Modules
Install the following packages and modules:

1. Install Flask, PostgreSQL with its PL/Python extension, SQL Alchemy and participated
```Python
sudo apt-get -qqy update
sudo apt-get -qqy upgrade
sudo apt-get -qqy install postgresql python-psycopg2 postgresql-plpython
sudo apt-get -qqy install python-flask python-sqlalchemy
sudo apt-get -qqy install python-pip
```

1. Required pip packages
``` Python
sudo pip install bleach
sudo pip install oauth2client
sudo pip install requests
sudo pip install httplib2
sudo pip install redis
sudo pip install passlib
sudo pip install itsdangerous
sudo pip install flask-httpauth
```
2.



### Installing

A step by step series of examples that tell you have to get a development env running

1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile (linked above)
3. Go to Vagrant directory and either clone this repo or download and place zip here
4. Launch the Vagrant VM (vagrant up)
5. Log into Vagrant VM (vagrant ssh)
6. Navigate to cd/vagrant as instructed in terminal
7. The app imports requests which is not on this vm. Run sudo pip install request.
8. Setup application database python/item-catalog/database_setup.py
9. Insert fake data python /item-catalog/database_init.py
10. Run application using python /item-catalog/app.py
11. Access the application locally using http://localhost:5000


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Niall O'Hara** - (https://github.com/nialloh23)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Privacy Policy
This website requires the following information from the user: name, email address and profile picture. This information is used only for registration and authentication, and will never be aggregated and given to any third party (unless required by law).

It also will not be used to contact users by the website owner without asking for explicit consent.

## Acknowledgments

* Material Design Alphabet
* Icon pack by Jurre Houtkamp
* Material design icons

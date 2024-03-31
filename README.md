# cs458-p2
### Running Application 
To run this code first we need to have `node js` with `LTS` version. For this project we have used `20.12.0` version. Having the correct version, clone the project and run
`npm ci` or `npm i` (`ci` is more secure way of doing it). Either one of these commands will automatically install necessary dependencies. also in order to use appium there is need for apk. since we have used expo it is really easy to to. however there is need of expo application services. to do that first comand we need to install eas to our computer. the command is `npm install -g eas-cli`. also user needs to create account on expo application services in order to create apk. after creating account, `eas build:configure` command will create eas.json however in our project it is already created. lastly to create apk following command:
`eas build -p android --profile preview` will create apk on the eas web cite. once the apk build is finish user can download it. here is a video for understanding the process better: https://www.youtube.com/watch?v=fUS_BjOHi-c&t=313s 
### Running Tests
To run tests please first install `python 3.10` then run following commands:

`cd test`

`pip install -r requirements.txt`

`python form_test_suit.py`

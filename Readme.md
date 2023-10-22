# ISS Tracker and Notifier

This Python script allows you to track the International Space Station (ISS) and receive email notifications when it is passing over your location during nighttime.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed
- Required packages: `requests`, `datetime`, `smtplib`, and `time`
```
pip install requests
```
```
pip install datetime
```
```
pip install secure-smtplib
```
## Setup

1. Clone or download this repository to your local machine.
2. Open the script file `iss_tracker.py` in a text editor or an integrated development environment (IDE).
3. Update the following variables with your own information:

   - `my_email`: Your Gmail email address.
   - `my_password`: Your Gmail app password. (Note: It's recommended to use an app password for security purposes.)
   - `my_latitude`: The latitude of your location.
   - `my_longitude`: The longitude of your location.


## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script `iss_tracker.py` is located.
3. Run the script by executing the following command:

   ```
   python iss_tracker.py
   ```

## License

This project is licensed under the MIT License

Feel free to paste this into your README file and make any additional changes you find necessary.

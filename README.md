# spBot_Dev

###### Built by [Jon Jones](https://me-ai.github.io/).

## Description

Package of spBot core automation scripts to supplement admin and deployment functionality in Sprocket CMMS.
The utilities created are still in development so use with caution. :thumbsup:

#### Core Packages

Reference requirements.txt

To get started...

```
pip install requirements.txt
```

And configure your bot credentials and Chrome binaries PATH. Example secrets.py included in spBot_Core

```
bot1 = # LoginID
bot2 = # LoginID
bot3 = # LoginID
bot4 = # LoginID
bot5 = # LoginID
bot6 = # LoginID
password = # Bot PW
binaries = # Path to Chrome Binaries
```

..and you are ready to go. :thumbsup:

#### Setting Bot Targets with CSV File
You can set targets with almost any data format.
The most common use case I have had is primarily with CSV or Excel. See example below.
All columns are converted to a list via pandas. At this point you can iterate through the data.

```
target_file = 'targets_to_sch.csv'
        col_names = ['unit', 'start', 'target_site', 'target_request', 'frequency']
        data = pandas.read_csv(target_file, names=col_names)

        # Store entries in list for variables
            x = 1
            unit = data.unit.tolist()
            start = data.start.tolist()
            target_site = data.target_site.tolist()
            target_request = data.target_request.tolist()
            frequency = data.frequency.tolist()
            sch_name = '{}-{}'.format(unit[x], target_request[x])
```

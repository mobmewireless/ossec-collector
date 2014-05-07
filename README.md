# OSSEC (logs) Collector

This little application collects logs from a local [OSSEC](http://www.ossec.net/) installation, and outputs them as
timestamped JSON entries. It is used by the [Union project](https://github.com/mobmewireless/union) to collect and store
OSSEC logs originating from known servers.

## Installation

Just `collector.py` with Python:

        $ python collector.py

Assuming you're using this tool with *Union*: fork this repository, add a deploy directory with *Union* deploy
instructions, and then deploy it to the target server. With the application in place, enable OSSEC logs collection for
that server.

## Testing

Testing is performed using [Behave](http://pythonhosted.org/behave/). Install Behave, and run the features with:

        $ behave

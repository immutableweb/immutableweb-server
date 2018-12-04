# immutableweb-server
The HTTP semantics based Immutable Web server

[![Build Status](https://travis-ci.org/immutableweb/immutableweb-server.svg?branch=master)](https://travis-ci.org/immutableweb/immutableweb-server)

For more details about the Immutable Web, check out: https://immutableweb.org

# Run the server

```
virtualenv -p `which python3` .ve
source .ve/bin/activate
pip install -r requirements.txt
python server.py /path/to/iw-streams
```

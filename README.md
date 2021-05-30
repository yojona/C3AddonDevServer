# C3AddonDevServer
Construct 3 addon development server

If you are on Windows 10 I recommend you to install WSL  https://docs.microsoft.com/en-us/windows/wsl/install-win10

### Create certificate needed for HTTPS

`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365`

### How to run
`python3 server.py`

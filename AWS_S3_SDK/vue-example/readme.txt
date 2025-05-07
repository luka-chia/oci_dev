step 1: 安装npm 10.9.1 and node v20.17.0:  https://nodejs.org/en/download
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 20

# Verify the Node.js version:
node -v # Should print "v20.18.3".
nvm current # Should print "v20.18.3".

# Verify npm version:
npm -v # Should print "10.8.2".


step 2:  执行npm install

step 3:  执行npm run serve

# Dockerfile for the Recipe App Frontend

# A Dockerfile must begin with a FROM clause. The Docker Hub registry has pre-built images.
# We are pulling a nodejs image, specifying the node version as well as the Debian version
FROM node:20-bookworm

# The ARG instruction defines a variable that users can pass at build-time
ARG PORT=3000

# ENV sets the environment variables inside the container
ENV PORT $PORT

# Defaults to development, npm will install developer packages
ARG NODE_ENV=dev

# Sets the node environment as an env variable
ENV NODE_ENV $NODE_ENV

# WORKDIR creates the directory and changes it to the current working directory
WORKDIR /recipe-app

# RUN is an image build step
# First we update the package manager
RUN apt-get update && apt-get install

# Installs the latest version of npm to get the latest security fixes
RUN npm i npm@latest -g

WORKDIR /recipe-app/frontend/recipe-web

# Copies over the npm package files
COPY recipe-web/package.json recipe-web/package-lock.json ./

RUN npm install

# Installing dependencies in a separate location can be beneficial for local development and production, as it allows for easier bind mounting of the application.
# Additionally, we add the .bin folder under node_modules to the path so that it can find nodemon or react scripts
ENV PATH /app/node_modules/.bin:$PATH

# Copy the source code from the host to the image
# We do this at the end as it frequently changes
COPY . .

# Exposes the given port
EXPOSE $PORT


# Runs a command after the image is built
# Runs our server
CMD npm run dev
# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in package.json
RUN npm install

# Make port 5000 available to the world outside this container
EXPOSE 5173

# Run the application
CMD ["npm", "run", "dev"]


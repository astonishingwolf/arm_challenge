FROM ghcr.io/teamroboconiitr/arm_teamrobocon:latest

# Install additional packages
RUN apt-get update && apt-get -y upgrade && apt-get -y install \
  tmux \
  && rm -rf /var/lib/apt/lists/*

# Copy packages and build the workspace
WORKDIR /catkin_ws
COPY src ./src
RUN apt-get update \
  && rosdep update \
  && rosdep install --from-paths src --ignore-src -r -y \
  && rm -rf /var/lib/apt/lists/*
RUN catkin config --extend /opt/ros/melodic && catkin build --no-status

# Automatically source the workspace when starting a bash session
RUN echo "source /catkin_ws/devel/setup.bash" >> /etc/bash.bashrc

# Install start script
COPY ./start.sh /

CMD ["/start.sh"]

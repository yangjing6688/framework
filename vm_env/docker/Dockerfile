FROM dorowu/ubuntu-desktop-lxde-vnc
USER root

RUN echo "root:extreme" | chpasswd

RUN apt-get update && apt-get install -y \
      python3 \
      python3-venv \
      python3-pip \
      python3-pycurl \
      python3-opencv \
      wget \
      curl \
      libcurl4-openssl-dev \
      libssl-dev \
      default-jdk \
      unzip \
      dos2unix \
      net-tools \
      iputils-ping \
      telnet \
      openssh-server \
      git

# Install apps directory
RUN useradd apps \
    && mkdir -p /home/apps \
    && chown -v -R apps:apps /home/apps

RUN cd /home/apps/ && curl -o allure-2.13.8.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz
RUN cd /home/apps/ && tar -zxvf allure-2.13.8.tgz -C /opt/
RUN cd /home/apps/ && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Install Pycharm
RUN mkdir /software
COPY files/pycharm-community.tar.gz /software
RUN tar xfz /software/pycharm-community.tar.gz -C /opt/
RUN chmod 777 /opt/pycharm*
RUN mv /opt/pycharm-community* /opt/pycharm-community


#Install other editors
RUN apt install -y vim
RUN apt-get install -y emacs

COPY all-requirements.txt /software
RUN pip install -r /software/all-requirements.txt

RUN mkdir automation
RUN chmod 777 automation
ENV PYTHONPATH "/automation/econ-automation-framework:/automation/econ-automation-tests:/automation/extauto:/automation/cw_automation:/automation/extreme_automation_tests"

# Install ssh
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN ln -s /usr/bin/python3 /usr/bin/python

# Install browser support
RUN mkdir tempFiles

#============================================
# Google Chrome
#============================================
# can specify versions by CHROME_VERSION;
#  e.g. google-chrome-stable=53.0.2785.101-1
#       google-chrome-beta=53.0.2785.92-1
#       google-chrome-unstable=54.0.2840.14-1
#       latest (equivalent to google-chrome-stable)
#       google-chrome-beta  (pull latest beta)
#============================================
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#============================================
# Chrome webdriver
#============================================
# can specify versions by CHROME_DRIVER_VERSION
# Latest released version will be used by default
#============================================
ARG CHROME_DRIVER_VERSION
RUN if [ -z "$CHROME_DRIVER_VERSION" ]; \
  then CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}"); \
  fi \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 777 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && sudo ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

# SSH fix for VOSS devices
RUN echo "KexAlgorithms diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1,curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256" >>/etc/ssh/ssh_config.d/weak.conf

# stand alone selenumn server
COPY files/selenium-server-standalone-3.141.59.jar /tempFiles/selenium-server-standalone-3.141.59.jar
COPY /files/pycharm.desktop /usr/share/applications
RUN rm -rf /software

# Update chrome to be able to run as root
RUN sed -i 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --no-sandbox/g' /opt/google/chrome/google-chrome






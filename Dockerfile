FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install python2.7 python-pip wget -y
RUN pip install selenium
ADD RemoteTest.py /root
RUN chmod +x /root/RemoteTest.py
CMD sleep 130s && python /root/RemoteTest.py
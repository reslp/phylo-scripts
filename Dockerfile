#created by Philipp Resl, Aug 2017
#uses mafft version 7.310

FROM phusion/baseimage:0.9.21

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y build-essential
RUN apt-get install -y python2.7
RUN ln -s /usr/bin/python2.7 /usr/bin/python

RUN wget http://mafft.cbrc.jp/alignment/software/mafft-7.310-with-extensions-src.tgz
RUN gunzip -cd mafft-7.310-with-extensions-src.tgz | tar xfv -
RUN cd mafft-7.310-with-extensions/core/ && make && make install && cp ../binaries/* /bin/

RUN git clone https://github.com/reslp/phylo-scripts
RUN cp phylo-scripts/get_analysis_docker.sh /

# Run app.py when the container launches
CMD ["./get_analysis_docker.sh"]
FROM tinkerpop/gremlin-server:3.4.8

LABEL maintainer="tkosht <takehito.oshita.business@gmail.com>"

WORKDIR /opt/gremlin-server/

ARG gremln_version=3.4.8
RUN /bin/bash -c "bin/gremlin-server.sh install org.apache.tinkerpop gremlin-python ${gremlin_version}"
RUN /bin/bash -c "bin/gremlin-server.sh install org.apache.tinkerpop neo4j-gremlin ${gremlin_version}"


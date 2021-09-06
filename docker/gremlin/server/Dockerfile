FROM tinkerpop/gremlin-server:3.4.8

LABEL maintainer="tkosht <takehito.oshita.business@gmail.com>"

WORKDIR /opt/gremlin-server/

ARG gremlin_version=3.4.8
RUN /bin/bash bin/gremlin-server.sh install org.apache.tinkerpop gremlin-python ${gremlin_version}
RUN /bin/bash bin/gremlin-server.sh install org.apache.tinkerpop neo4j-gremlin ${gremlin_version}


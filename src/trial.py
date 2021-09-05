from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

if __name__ == "__main__":
    g = traversal().withRemote(
        DriverRemoteConnection("ws://gremlin-server:8182/gremlin", "g")
    )
    g.addV("mathematician1").property("name", "euiler")  # .next()
    g.addV("mathematician2").property("name", "erdos")  # .next()
    print("names:", g.V().values("name").toList())
    print("dict:", g.V().valueMap().toList())
    print("count:", g.V().count().next())

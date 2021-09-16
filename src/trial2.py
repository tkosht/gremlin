from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class GremlinProvider(object):
    def __init__(self):
        self.g = traversal().withRemote(
            DriverRemoteConnection("ws://gremlin-server:8182/gremlin", "g")
        )

    def clear_nodes(self):
        self.g.V().drop().iterate()
        return self

    def add_person(self, name: str):
        node = self.g.addV("person").property("name", name).next()
        return node

    def add_age(self, name: str, age: int):
        assert name and 0 <= age <= 150
        node = self.g.V().has("person", "name", name).property("age", age).next()
        return node

    def add_job(self, name: str, job: str):
        assert name and job
        node = self.g.V().has("person", "name", name).property("job", job).next()
        return node

    def get_name(self, v):
        name = self.g.V(v).values("name").toList()[0]
        return name

    def get_age(self, v):
        age = self.g.V(v).values("age").toList()[0]
        return age

    def add_knows(self, v1, v2, weight=0.75):
        edge = self.g.V(v1).addE("knows").to(v2).property("weight", weight).iterate()
        return edge

    def find_person_node(self, name: str):
        node = self.g.V().has("person", "name", name).next()
        return node

    def find_person_whom_knows(self, center: str):
        whom_knows = self.g.V().has("person", "name", center).out("knows").toList()[0]
        return whom_knows


if __name__ == "__main__":
    grp = GremlinProvider()
    grp.clear_nodes()

    # marko を登録
    v1 = grp.add_person("marko")
    assert grp.get_name(v1) == "marko"
    print("v1:", grp.get_name(v1))
    # v1: marko

    # stephen を登録
    v2 = grp.add_person("stephen")
    assert grp.get_name(v2) == "stephen"
    print("v2:", grp.get_name(v2))
    # v2: stephen

    # 年齢を追加・更新
    grp.add_age("marko", 35)  # insert
    grp.add_age("marko", 31)  # update
    grp.add_age("stephen", 32)

    # 職業を追加・更新
    grp.add_job("marko", "SWE")
    grp.add_job("stephen", "SWE")

    # リレーション（knows） を追加
    e1 = grp.add_knows(v1, v2, 0.1)
    print(e1)
    # [['V', v[34]], ['addE', 'knows'], ['to', v[35]], ['property', 'weight', 0.1], ['none']]

    # marko を検索
    marko = grp.find_person_node("marko")
    print("marko:", grp.get_name(marko))
    # marko: marko

    # marko が知っている人を検索
    v = grp.find_person_whom_knows("marko")
    print("marko knows:", grp.get_name(v))
    print("marko knows2:", grp.g.V(v1).outE().inV().values("name").toList()[0])
    # marko knows: stephen
    # marko knows2: stephen

    # ノードオブジェクトから年齢を取得
    print("marko.age:", grp.get_age(v1))
    assert grp.get_age(v1) == 31
    print("stephen.age:", grp.get_age(v2))
    assert grp.get_age(v2) == 32
    # marko.age: 31
    # stephen.age: 32

    # 職業が ”SWE" である人物の名前を取得(リスト)
    print("SWE:", grp.g.V().has("person", "job", "SWE").values("name").toList())
    # SWE: ['marko', 'stephen']

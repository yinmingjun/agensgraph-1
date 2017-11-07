import pytest

@pytest.fixture
def connection():
    import agensgraph
    return agensgraph.psycopg2.connect("dbname=iomed")


def test_basic_operation(connection):
    cur = connection.cursor()
    cur.execute("SET graph_path=snomed;")
    cur.execute("MATCH (a {id: 107008})-[r:IS_A*..5]->(b) RETURN a,r,b")
    result = cur.fetchone()
    assert result is not None

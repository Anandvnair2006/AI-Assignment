from neo4j import GraphDatabase


uri = "bolt://localhost:7687"

username = "neo4j"
password = "password"


driver = GraphDatabase.driver(
    uri,
    auth=(username, password)
)


with driver.session() as session:

    session.run(
        """
        CREATE (p:Place {name:'Goa'})
        CREATE (h:Hotel {name:'Beach Resort'})
        CREATE (p)-[:HAS_HOTEL]->(h)
        """
    )

    result = session.run(
        """
        MATCH (p:Place)-[:HAS_HOTEL]->(h)
        RETURN p.name, h.name
        """
    )

    for record in result:
        print(record)
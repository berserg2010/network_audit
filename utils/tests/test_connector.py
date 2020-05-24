from ..connector import Connector

class TestConnector:

    def test_instance(self):

        session = Connector(
            client="1.2.3.4",
            auth=("abc", "abc")
        )
        assert isinstance(session, Connector)

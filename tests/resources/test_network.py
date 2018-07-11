from resources.network import Network
import mock

def test_network_all():

    network_list_obj = mock.MagicMock()
    network_list_obj.id = 1
    network_list_obj.name = "test"

    client = mock.MagicMock()
    networks = mock.MagicMock()
    network_list = mock.MagicMock()
    network_list.return_value = [network_list_obj]
    
    networks.list = network_list
    client.networks = networks
    
    network = Network(client)
    actual_network_list = network.all()
    
    assert len(actual_network_list) == 1
    assert actual_network_list[0]["id"] == 1
    assert actual_network_list[0]["name"] == "test"
     
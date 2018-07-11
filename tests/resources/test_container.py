from resources.container import Container
import mock

def test_container_all():

    container_list_obj = mock.MagicMock()
    container_list_obj.id = 1
    container_list_obj.name = "neeraj"

    client = mock.MagicMock()
    containers = mock.MagicMock()
    container_list = mock.MagicMock()
    container_list.return_value = [container_list_obj]
    
    containers.list = container_list
    client.containers = containers
    
    container = Container(client)
    actual_container_list = container.all()
    
    assert len(actual_container_list) == 1
    assert actual_container_list[0]["id"] == 1
    assert actual_container_list[0]["name"] == "neeraj"
     
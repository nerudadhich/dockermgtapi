from resources.volume import Volume
import mock

def test_volume_all():

    volume_list_obj = mock.MagicMock()
    volume_list_obj.id = 1
    volume_list_obj.name = "neeraj"

    client = mock.MagicMock()
    volumes = mock.MagicMock()
    volume_list = mock.MagicMock()
    volume_list.return_value = [volume_list_obj]
    
    volumes.list = volume_list
    client.volumes = volumes
    
    volume = Volume(client)
    actual_volume_list = volume.all()
    
    assert len(actual_volume_list) == 1
    assert actual_volume_list[0]["id"] == 1
    assert actual_volume_list[0]["name"] == "neeraj"
     
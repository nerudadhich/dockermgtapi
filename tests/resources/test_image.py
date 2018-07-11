from resources.image import Image
import mock

def test_image_all():

    image_list_obj = mock.MagicMock()
    image_list_obj.id = 1
    image_list_obj.name = "test"

    client = mock.MagicMock()
    images = mock.MagicMock()
    image_list = mock.MagicMock()
    image_list.return_value = [image_list_obj]
    
    images.list = image_list
    client.images = images
    
    image = Image(client)
    actual_image_list = image.all()
    
    assert len(actual_image_list) == 1
    assert actual_image_list[0]["id"] == 1
     
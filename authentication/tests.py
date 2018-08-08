from django.test import TestCase

from PIL import Image
import tempfile
from django.test import TestCase
from .models import Image
from django.test import override_settings


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'jpeg')
    return temp_file


class PictureDummyTest(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # gettempdir() gets images from the temp file created running tests
    # overrides the default media directory to avoid dumping test images in that directory
    def test_dummy_test(self):
        temp_file = tempfile.NamedTemporaryFile()
        # create a temp file to store temp test images
        test_image = get_temporary_image(temp_file)
        # create a small square  and save it in the temp file
        # test_image.seek(0) --> this test an image as an attached
        # file thats in http request
        # test_image.seek(0)
        # response = self.client.put(
        #     self.reverse('upload_user_picture'),
        #     {'profile_picture': test_image})
        image = Image.objects.create(picture=test_image.name)
        # create an Image instance with test_image as its image field
        # test_image.name tells django where the image is located
        print("It Worked!, ", image.picture)
        # appears when the test is complete without errors
        self.assertEqual(len(Image.objects.all()), 1)


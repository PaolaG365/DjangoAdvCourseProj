import re
from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CharsValidator:
    """
    valid_chars: raw string
    message: str\n
    Checks if a string is made of valid chars only.
    If valid chars is not set will be alphanumeric and punctuation.
    Default message is 'Only letters, digits, spaces, and common punctuation symbols are allowed'.
    """
    def __init__(self, valid_chars=None, message=None):
        self.valid_chars = valid_chars
        self.message = message

    @property
    def valid_chars(self):
        return self.__valid_chars

    @valid_chars.setter
    def valid_chars(self, value):
        if value is None:
            self.__valid_chars = re.compile(r'^[a-zA-Z0-9\s!\"#$%&\'()*+,\-./:;=?@[\\\]^_`{|}~]*$')
        else:
            self.__valid_chars = re.compile(value)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Only letters, digits, spaces, and common punctuation symbols are allowed.'
        else:
            self.__message = value

    def __call__(self, value):
        if not self.valid_chars.match(value):
            raise ValidationError(f'{self.message} Input: {value}')


@deconstructible
class FileValidator:
    ALLOWED_EXTENSIONS = []

    def __init__(self, allowed_extensions=None):
        self.ALLOWED_EXTENSIONS = allowed_extensions or self.ALLOWED_EXTENSIONS

    def __call__(self, file):
        if not file:
            return

        file_extension = file.format.lower() if hasattr(file, 'format') else file.name.split('.')[-1]
        if file_extension not in self.ALLOWED_EXTENSIONS:
            raise ValidationError(
                f"Invalid file type: {file_extension}. Allowed types: {', '.join(self.ALLOWED_EXTENSIONS)}"
            )


@deconstructible
class ImageFileValidator(FileValidator):
    """
    Allowed extensions: jpg, jpeg, png, gif, webp
    """
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp']


@deconstructible
class VideoFileValidator(FileValidator):
    """
    Allowed extensions: mp4, mvk, mov, webm
    """
    ALLOWED_EXTENSIONS = ['mp4', 'mkv', 'mov', 'webm']

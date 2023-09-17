from io import FileIO

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from django_ffield.utils import meme_type

@deconstructible
class FileTypeValidator:
    """A file type validator
    """

    def __init__(self, allowd_types: list[str],disallowed_types=[]) -> None:
        """
        Parameters
        ----------
        allowed_types : list[str]
            types and sub-types that allowd file be
            example :
                `["image","pdf","mp4",...]`
        
        disallowed_types : list[str]
            types and sub-types that disallowed file be
            example :
                `["py","exe","bat",...]`
        
        """
        self.allowd_types = list(map(str.lower, set(allowd_types)))
        self.disallowed_types = list(map(str.lower, set(disallowed_types)))

    def __call__(self, file:FileIO) -> None:
        """called by django validator

        Parameters
        ----------
        file : FileIO
            the file input that passed by django to validate 

        Raises
        ------
        ValidationError
            when the file don't match by selected types this error raises to show to user
        """
        typ, formt = meme_type(file)
        
        # * to prevent forbidden upload files by user
        if typ not in self.allowd_types and formt not in self.allowd_types:
            raise ValidationError(
                f"Unsupported Format: The {formt} type is not in allowd supported formats. Supported formats: {self.allowd_types}. Unsupported formats: {self.disallowed_types}. "
            )
        elif typ in self.disallowed_types or formt in self.disallowed_types :
            raise ValidationError(
                f"Unsupported Format: The {formt} type is not supported formats. Unsupported formats: {self.disallowed_types}."
            )
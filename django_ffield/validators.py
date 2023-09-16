from io import FileIO

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from magic import from_buffer


def meme_type(file:FileIO) -> tuple[str, str]:
    """detect meme type of file by reading the first 2048 bytes of file

    Parameters
    ----------
    file : FileIO
        file you want to detect meme type of it

    Returns
    -------
    tuple[str, str]
        type and subtype of file for example ("Image","Png")
    """

    typ, subtyp = from_buffer(file.read(2048), True).split('/')
    return typ, subtyp


@deconstructible
class FileTypeValidator:
    """A file type validator
    """

    def __init__(self, types: list[str]) -> None:
        """
        Parameters
        ----------
        types : list[str]
            types and sub-types that allowd file be
            example :
                ["Image","PDF","mp4",...]
        """
        self.types = list(map(str.lower, set(types)))

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
        if typ not in self.types and formt not in self.types:
            raise ValidationError(
                f"Unsupported Format: The {formt} type is not supported. Supported formats: {self.types}."
            )
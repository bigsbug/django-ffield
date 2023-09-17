from io import FileIO
from django.db.models.fields.files import FieldFile
from magic import from_buffer

def meme_type(file:FileIO|FieldFile) -> tuple[str, str]:
    """detect meme type of file by reading the first `2048 bytes` of file

    Parameters
    ----------
    file : FileIO
        file you want to detect meme type of it in `rb` mode

    Returns
    -------
    tuple[str, str]
        type and subtype of file for example `("Image","png")`
    """

    typ, subtyp = from_buffer(file.read(2048), True).split('/')
    return typ, subtyp

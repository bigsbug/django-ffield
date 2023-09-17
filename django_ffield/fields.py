from typing import Any
from django.db.models.base import Model
from django.db.models.fields.files import FieldFile, FileField
from django_ffield.validators import FileTypeValidator
from django_ffield.utils import meme_type


class FiledFField(FieldFile):
    def __init__(self, instance: Model, field: FileField, name: str | None) -> None:
        super().__init__(instance, field, name)

    @property
    def mime_type(self) -> str:
        """return the mimetype of file

        Returns
        -------
        str
            mimetype : `'image/png'`
        """
        mime: str = '/'.join(meme_type(self))
        return mime

    @property
    def type(self) -> str:
        """return the type of file for example : `Video,Image,...`

        Returns
        -------
        str
            type of file
        """
        return meme_type(self)[0]

    @property
    def format(self) -> str:
        """return subtype of file or extention like `png,mp4,pdf,...`

        Returns
        -------
        str
            the subtype of file
        """
        return meme_type(self)[1]


class FileFField(FileField):
    """This field can accept a list of `allowd_types` as and `disallowd_types` input,
    allowing the user to pass only these specific allowd_types to the field,
    and don't allowd pass disallowd types to the filed.

    Parameters
    ----------
    FileField : Django FileField

    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.allowd_types: list[str] = kwargs.pop("allowd_types", [])
        self.disallowd_types: list[str] = kwargs.pop("disallowd_types", [])
        super().__init__(*args, **kwargs)

        if self.allowd_types or self.disallowd_types:
            self.validators.append(
                FileTypeValidator(allowd_types=self.allowd_types,
                                  disallowd_types=self.disallowd_types,)
            )

    attr_class = FiledFField

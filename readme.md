
  

# django-ffield

  

django-ffield is a Django package that provides additional functionality and control over Django model fields, specifically focusing on file fields. this guide will you through the package's features, installation process, and provide examples of how to use it effectively.

  

## Table of Contents

- [Installation](#installation)

- [Usage](#usage)

- [FileFField](#fileffield)

- [FiledFField](#filedffield)

- [Utility Functions](#utility-functions)

- [Validators](#validators)

- [Contributing](#contributing)

- [License](#license)

  

---

  

## Installation

  

You can install `django-ffield` via pip:

  

```bash

pip  install  django-ffield

```

  

## Usage

  

### FileFField

  

`FileFField` extends Django's `FileField` and allows you to specify accepted file types and disallowed types during field initialization.

  

#### Example:

  

```python

from django.db import models

from django_ffield.fields import FileFField

  

class  MyModel(models.Model):

image_field = FileFField(upload_to='images/', types=['image'])

pdf_field = FileFField(upload_to='pdfs/', types=['pdf'],
					disallowed_types=['image','video'])

video_field = FileFField(upload_to='videos/', types=['video'])

  

# Usage

my_instance = MyModel.objects.get(pk=1)

my_instance.image_field = 'example.png'  # Validates as it matches the 'image' type

my_instance.pdf_field = 'example.pdf'  # Validates as it matches the 'pdf' type

my_instance.video_field = 'example.mp4'  # Validates as it matches the 'video' type

```

  

### FiledFField

  

`FiledFField` is a field that extends Django's `FieldFile` and provides additional properties to access file-related information.

  

#### Example:

  

```python

from django.db import models

from django_ffield.fields import FiledFField

  

class  MyModel(models.Model):

file_field = FiledFField(upload_to='uploads/')

  

# Usage

my_instance = MyModel.objects.get(pk=1)

file = my_instance.file_field

  

# Accessing file properties

mime_type = file.mime_type # Returns the mimetype (e.g., 'image/png')

file_type = file.type # Returns the type of file (e.g., 'Image')

file_format = file.format # Returns the file format (e.g., 'png')

```

  

## Utility Functions

  

`django-ffield` provides a utility function for detecting file MIME types.

This function detects the MIME type of a file by reading the first 2048 bytes
##### note : the file should be opened in binary mode.

  

#### Example:

  

```python

from django_ffield.utils import meme_type

from django.core.files import File

  

with  open('example.png', 'rb') as  file:

type, subtype = meme_type(file)

print(f"Type: {type}, Subtype: {subtype}")

```

  

## Validators

  

`django-ffield` includes a custom file type validator that can be used with `FileFField`.

This validator ensures that the uploaded file's type is among the specified types.

  

#### Example:

  

```python

from django_ffield.validators import FileTypeValidator

  

class  MyModel(models.Model):

file_field = models.FileField(upload_to='uploads/', validators=[

		FileTypeValidator(
		allowd_types=['image', 'pdf', 'mp4'],
		disallowed_types = ["audio"],
		)

])

  

# Usage

my_instance = MyModel.objects.get(pk=1)

my_instance.file_field = 'example.mp3'  # This will raise a ValidationError since 'mp3' is not in the accepted types

```

  

## Contributing

  

Feel free to contribute to `django-ffield`.

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](https://github.com/bigsbug/django-ffield/blob/main/LICENSE) file for details.

  

---

  

Feel free to explore and utilize `django-ffield` to enhance your Django projects. If you have any questions, issues, or feature requests, please open an [issue](https://github.com/bigsbug/django-ffield/issues) on our GitHub repository. Happy coding!
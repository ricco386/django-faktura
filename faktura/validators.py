from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _


class FileSizeValidator(BaseValidator):
    message = _("The maximum file size that can be uploaded is %(limit_value)s MB.")
    code = "file_size"

    def compare(self, file, limit_value):
        filesize = file.size / (1024 * 1024)  # Convert to MB
        return filesize > limit_value

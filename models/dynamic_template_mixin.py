import re
from odoo import api, models, fields
from . import dynamic_template_utils as utils


class DynamicTemplateMixin(models.AbstractModel):
    _name = 'dynamic.template.mixin'
    _description = 'Dynamic Template Mixin'

    def update_dynamic_field(self, base_template):
        """
        Method to extract placeholders, find corresponding field values,
        and replace them in the template.
        """
        replace_field_value = ""
        for record in self:
            template_string = base_template or ""

            # Find all placeholders like {{object.field_name}}
            placeholders = re.findall(r'{{\s*object\.(.*?)\s*}}', template_string)

            for placeholder in placeholders:
                field_value = utils.get_model_field_value(record, placeholder)

                # Replace placeholders with actual field values
                template_string = template_string.replace(
                    f'{{{{object.{placeholder}}}}}', str(field_value)
                )

            # Save the rendered template
            replace_field_value = template_string

        return replace_field_value


import re
from datetime import date, datetime
from odoo import models


def get_model_field_value(obj, field_path):
    """
    Traverse and get field values even for nested relational fields like
    Example: `line_ids.product_id.name`. Handles date/datetime fields.
    """
    fields_chain = field_path.split('.')
    current_value = obj

    for index, field_name in enumerate(fields_chain):
        if not hasattr(current_value, field_name):
            current_value = ''
            break
        data = getattr(current_value, field_name)
        current_value = data if not isinstance(data, bool) else ''

        # Handle One2many or Many2many fields by recursing for each related record
        if isinstance(current_value, models.Model):
            if index < len(fields_chain) - 1 and isinstance(
                    getattr(current_value, fields_chain[index + 1], None), list
            ):
                current_value = ', '.join(
                    str(
                        get_model_field_value(record, '.'.join(fields_chain[index + 1:]))
                    ) for record in current_value
                )
                break
        elif isinstance(current_value, list) and current_value and isinstance(current_value[0], models.Model):
            current_value = ', '.join(
                str(
                    get_model_field_value(record, '.'.join(fields_chain[index + 1:]))
                ) for record in current_value
            )
            break

    # Format date or datetime at the end
    if isinstance(current_value, (date, datetime)):
        current_value = current_value.strftime('%Y-%m-%d %I:%M %p')

    return current_value

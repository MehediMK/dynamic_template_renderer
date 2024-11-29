# Dynamic Template Module

### **Overview**
The **Dynamic Template Module** provides a seamless way to dynamically render templates with placeholders in Odoo 17. Using this module, users can define templates with placeholders, which are automatically replaced with field values from models. It supports nested fields, One2many, Many2many relationships, and date/datetime formatting.

---

### **Key Features**
- Define and render dynamic/field value in templates/Html with placeholders.
- Support for nested field values (e.g., `{{object.field.product_id.name}}`).
- Works with relational fields (Fields, One2many, Many2many).
- Automatically formats date and datetime fields.
- Plug-and-play functionality with a mixin.

---

### **Installation**
1. Log in to your Odoo 17 instance.
2. Go to **Apps**.
3. Click **Update Apps List**.
4. Search for **Dynamic Template Module**.
5. Add this `dynamic_template_renderer` name in your module **depends list** in __manifest__.py file.
6. Inherit you Model like this => `_inherit = 'dynamic.template.mixin'`
---

### **Usage Guide**
Here’s the **Usage Guide** section written requirement:

---


#### **Step 1: Add the Mixin**
To use the dynamic template rendering functionality, inherit the mixin `dynamic.template.mixin` in your custom model:

```python
from odoo import models, fields, api

class YourModel(models.Model):
    _name = 'your.model'
    _inherit = 'dynamic.template.mixin'

    base_template = fields.Html(string="Base Template")
    next_template = fields.Html(string="Next Template")
    other_template = fields.Html(string="Rendered Base Template")
    render_template = fields.Html(string="Rendered Next Template")

    @api.onchange('base_template', 'next_template')
    def update_description(self):
        for rec in self:
            rec.other_template = self.update_dynamic_field(rec.base_template)
            rec.render_template = self.update_dynamic_field(rec.next_template)
```

#### **Step 2: Define Placeholders in Your Template Fields**
In the template fields (`base_template`, `next_template`, etc.), use the following placeholder format to dynamically render field values:
- **Basic Field:** `{{object.field_name}}`
- **Relational Field:** `{{object.related_field.sub_field}}`

---

### **Example Workflow**

#### **Dynamic Placeholders in a Template**
Imagine a model named `your.model` with the following fields:
- `name` (Char): Name of the user.
- `st_id` (Char): ID of the user.
- `address` (Char): Address of the user.

You define a template in the `base_template` field:
```html
Hello {{object.name}}, your ID is {{object.st_id}}. Your address is {{object.address}}.
```

#### **Expected Output**
When the record is saved, the `other_template` field will render the dynamic template:
```html
Hello John Doe, your ID is 12345. Your address is 456 Elm Street.
```

---

### **Advanced Usage**

#### **Relational Fields**
For fields in related models, use dot notation:
```html
Your product is {{object.line_ids.product_id.name}} with a price of {{object.line_ids.price_unit}}.
```

#### **Date and Datetime Fields**
Dates and datetimes are automatically formatted as `YYYY-MM-DD HH:MM AM/PM`:
```html
Today's date is {{object.create_date}}.
```
Output:
```html
Today's date is 2024-11-17 03:30 PM.
```

---

### **Using This in Your Model**
To implement this in your custom models, follow these steps:
1. **Inherit the Mixin**: Add `_inherit = 'dynamic.template.mixin'` in your model.
2. **Define Template Fields**: Create fields for raw templates (`base_template`, `next_template`) and rendered templates (`other_template`, `render_template`).
3. **Onchange Method**: Use the `update_dynamic_field` method in an `@api.onchange` function to update the rendered fields dynamically.

Here’s a simple example:
```python
@api.onchange('template_field')
def update_rendered_template(self):
    for record in self:
        record.rendered_template = self.update_dynamic_field(record.template_field)
```

---

### **Dependencies**
- **Base**: The module depends on the `base` module and does not require additional dependencies.

---

### **Customization**
This module is easily extensible. Developers can inherit the mixin and integrate it into any model to enable dynamic template rendering.

---

### **Support**
If you encounter any issues or have questions:
- Visit Our [Medium Profile](https://mehedi-khan.medium.com/).
- Email us at mehedikhan.cse@gmail.com.

---

### **License**
This module is licensed under the [OPL-1](LICENSE) license.

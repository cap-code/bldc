import frappe

def get_context(context):
    context.data = frappe.get_all('Website Item', filters={'published': 1}, fields=['*'])

import frappe

def get_context(context):
    context.no_cache = 1
    context.data = frappe.get_all('Website Item', filters={'published': 1}, fields=['*'])

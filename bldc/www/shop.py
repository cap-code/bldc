import frappe

def get_context(context):
    context.data = frappe.get_all('Website Item', filters={'published': 1}, fields=['*'])
    context.price = frappe.get_all('Item Price', filters={'price_list': 'Customer Selling'}, fields=['*'])

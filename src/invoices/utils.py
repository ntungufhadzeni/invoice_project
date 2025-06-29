def calculate_invoice_total(subtotal, vat_rate):
    vat_amount = subtotal * (vat_rate / 100)
    return subtotal + vat_amount

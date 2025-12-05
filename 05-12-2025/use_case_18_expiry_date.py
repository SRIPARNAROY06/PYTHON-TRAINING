from datetime import date,datetime,timedelta
products={
    "Milk":"2025-01-05",
    "Cheese":"2026-01-06",
    "Bread":"2025-12-12",
    "Mayo": "2025-12-16"
}

def expiry_date(products):
    today=datetime.today()
    soon=today+timedelta(days=14)
    result=[]

    for product,exp in products.items():
        exp_date=datetime.strptime(exp,"%Y-%m-%d")
        if today<=exp_date<=soon:
            result.append(product)

    return result

print(expiry_date(products))
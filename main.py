from currency import INRToUSDConverter

def main(temp_,currency_type):
    
    currency_converter = INRToUSDConverter(api_key='YOUR_API_KEY')
    # currency_type = request.session.get('currency')
    print('currency_type = ',currency_type)  
    try:
        if not currency_type:
            currency_type = ''
            # request.session['currency'] = currency_type

        if 'USD' in currency_type:
            for product in temp_:
                product.product.price_usd = currency_converter.convert_inr_to_usd(product.product.price)

        else:
            for product in temp_:
                product.product.price_usd = product.product.price
    except Exception as e:
        print(e)

    return temp_










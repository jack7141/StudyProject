

def store_to_xlsx(writer, list_key_name='records', sheet_name='sheet'):
    def inner(func):
        def wrapper(*args, **kwargs):            
            print(f'START {sheet_name}')
            response = func(*args, **kwargs)
            
            result_json = {list_key_name: response}
            writer.json_to_xlsx(json=result_json, list_key_name=list_key_name, sheet_name=sheet_name)
            
            print(f'FINISH {sheet_name}')                             
            return response
        return wrapper
    return inner    

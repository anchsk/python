http_status = 404

match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print("Bad request")
    case 404:
        print('Not Found')
    case 500 | 501:
        print('Server error')
    case _:
        print('Unknown')
        

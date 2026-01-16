def serve_chai(flavor):
    try:
        print(f'preparing {flavor} chai...')
        if flavor=='unknown':
            raise ValueError("We don't know the flavor")
    except ValueError as e:
        print('Error:',e)
    else:
        print(f"{flavor} chai is served")
    finally: #always run, close/clean db connection
        print("Next customer please!")

serve_chai("unknown")
# preparing unknown chai...
# Error: We don't know the flavor
# Next customer please!
serve_chai("masala")
# preparing masala chai...
# masala chai is served
# Next customer please!
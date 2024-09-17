def convert_strings_to_integers(func):
    def wrapper(a, b):
        print(a, b)
        try:
            a,b= int(a),int(b)
        except Exception as e:
            print(e)
        return func(a, b)

    return wrapper
@convert_strings_to_integers
def sum_function(a,b):
    return a+b
return_sum=sum_function(a=10,b="20")
print("sum of the number is :", return_sum)


##    Task 1

# def amount_payment(payment):
#     sum = 0
#     for i in payment:
#         if i > 0:
#             sum = sum + i                 
#     print(sum)    
#     return sum
    

def prepare_data(data):
    new_data = sorted(data)
    new_data.pop(0)
    new_data.pop()
    return new_data

prepare_data([2, 4, 5, 3])